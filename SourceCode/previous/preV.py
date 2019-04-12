#Created by Michael Winberry Feb 5 2017
#Version Created April 13 2018
#Termdocs Text Editor

import os
import sys
import platform
import subprocess

class Document(object):
    
    def __init__(self):
        self.path = ""
        self.lines = []
        self.swapPath = ""
        self.copy = []
        self.cmd = ""
        self.start = 0
        self.end = 0
        self.position = 0
        self.kill = False
        self.defaultStart = 0
        self.undo = []
        self.redo = []
        self.indent = 0
        self.spaces = ""
        
    def reset(self):
        self.path = ""
        self.lines = []
        self.swapPath = ""
        self.copy = []
        self.cmd = ""
        self.start = 0
        self.end = 0
        self.position = 0
        self.kill = False
        self.defaultStart = 0
        self.undo = []
        self.redo = []
        self.indent = 0
        self.spaces = ""
    
    def getPath(self):
        return str(self.path)
    
    def getLength(self):
        return len(self.lines) - 1
    
    def chooseIndent(self, position):
        prevTab = self.getTabs(position)
        print "Previous Tab: " + str(prevTab)
        indent = raw_input("Enter # of Tabs: ")
        self.setIndent(indent)
 
    def setSpaces(self):
        indent = self.indent;
        spaces = ""
         
        for i in range(indent):
            spaces += "    "
         
        self.spaces = spaces
        return spaces
     
         
    def setIndent(self, indent):
        try:
            if int(indent) >= 0:
                self.indent = int(indent)
                self.spaces = ""
                for i in range(self.indent):
                    self.spaces += "    "
            else:
                raise Exception
        except Exception:
            print "----Invalid Input----"
 
    def reindentLine(self, lineNum):
        self.chooseIndent(lineNum)
        self.lines[lineNum] = self.spaces + self.lines[lineNum].strip() + "\n"
    def indentPlus(self):
        self.indent += 1
        self.spaces += "    "
 
    def indentMinus(self):
        if self.indent > 0:
            self.indent -= 1
            self.spaces = ""
            for i in range(self.indent):
                self.spaces += "    "
        else:
            print "----Indent Already Set to 0----"
 
    def startUp(self):
        if len(sys.argv)-1 >= 1:
            self.path = str(self.checkPath(str(os.path.abspath(sys.argv[1]))))
            if self.path != "Fail":
                self.lines = self.fillArray(self.path)
                del sys.argv[1]
            else:
                self.path = ""
                del sys.argv[1]
                self.startUp()
            
        else:
            self.path = str(self.getDirectory())
            if self.path != "Fail":
                self.lines = self.fillArray(self.path)
            else:
                self.path = ""
                self.kill = True
                return
            
        if not self.lines:
            self.cNewCmd()
        
        self.createSwap()
        self.undo = self.fillArray(self.path)
        self.redo = self.fillArray(self.path)
            
    def printDocument(self):
        self.clear()
        print self.path
        if platform.system() == "Windows" and self.position > 20 and self.cmd != "-vl":
            self.start = self.position - 20
        elif platform.system() == "Windows" and self.cmd != "-vl":
            self.start = self.defaultStart
 
        for i in range(int(self.start), int(self.position+1)):
            print str(i) + ": " + self.lines[i]
        
    def getCmd(self):
        position = self.position
        self.cmd = str(raw_input(str(position+1) + ": " + self.spaces))

    def getStartEnd(self) :
        try:
            startTemp = int(raw_input("Enter Starting Line #: "))
            endTemp = int(raw_input("Enter Ending Line #: "))
            if startTemp >= (len(self.lines)) or startTemp < 0:
                raise Exception
            elif endTemp >= (len(self.lines)) or endTemp < 0:
                raise Exception
            else:
                self.start = startTemp
                self.end = endTemp
        except Exception:
            print "----Start and End Must Be Valid Line #'s----"
            raw_input("Press Any Key to Continue")
            self.getStartEnd()
    
    def executeCommand(self):
        cmd = self.cmd
        if cmd == "-pst":
            changeIndent = raw_input("Change Indent of Items to Paste? y/n")
             
            if (changeIndent == 'y' or changeIndent == 'Y'):
                changeFlag = True
            else:
                changeFlag = False
                 
            for i in range(len(self.copy)):
                print "Line to be Pasted: " + self.copy[i]
                if(changeFlag):
                    self.chooseIndent(self.position)
                if self.position < len(self.lines)-1:
                    self.lines.insert(self.position+1, self.spaces + self.copy[i])
                else:
                    self.lines.append(self.spaces + self.copy[i])
                self.position += 1
            
        elif cmd == "-q":
            self.clear()
            self.promptSave()
            self.kill = True
            return self.kill
 
        elif cmd == "-h":
            self.helpMenu()
 
        elif cmd == "-id":
            self.chooseIndent(self.position)
 
        elif cmd == "-idp":
            self.indentMinus()
 
        elif cmd == "-t":
            self.indentPlus()
 
        elif cmd == "-ida":
            self.setIndent(self.getTabs(self.position))
             
        elif cmd == "-on":
            self.promptSave()
            tempPath = self.getDirectory()
            if tempPath != "Fail":
                self.deleteSwap()
                sys.argv.append(tempPath)
                self.reset()
                self.startUp()
            else:
                self.deleteSwap()
                self.kill = True
                self.path = ""
                return self.kill
                
        elif cmd == "-cp":
            self.copy = []
            self.copy.append(str(raw_input("Store Input: ")))
        
        elif cmd == "-ccl":
            self.copy = []
            self.copy.append(self.stripCopy(self.position))
            
        elif cmd == "-cs":
            self.copy = []
            self.getStartEnd()
            tempCount = self.start
            while(tempCount <= self.end):
                self.copy.append(self.stripCopy(tempCount))
                tempCount += 1
            self.start = self.defaultStart
        
        elif cmd == "-ud":
            self.redo = self.fillArray(self.path)
            self.lines = self.undo
            self.save(self.path, self.lines)
        
        elif cmd == "-rd":
            self.undo = self.fillArray(self.path)
            self.save(self.path, self.redo)
            self.lines = self.fillArray(self.path)
        
        elif cmd == "-stab":
            for i in range(len(self.lines)):
                self.lines[i] = self.replaceTabs(self.lines[i])
             
        elif cmd == "-sct":
            self.lines[self.position] = self.replaceTabs(self.lines[self.position])
             
        elif cmd == "-sst":
            self.getStartEnd()
            tempCount = self.start
            while(tempCount <= self.end):
                self.lines[tempCount] = self.replaceTabs(self.lines[tempCount])
                tempCount += 1
            self.start = self.defaultStart
                 
        elif cmd == "-rtl":
            self.reindentLine(self.position)
         
        elif cmd == "-rts":
            self.getStartEnd()
            tempCount = self.start
            while(tempCount <= self.end):
                self.reindentLine(tempCount)
                tempCount += 1
            self.start = self.defaultStart
             
        elif cmd == "-vl":
            self.clear()
            defaultPosition = self.position
            self.position = len(self.lines)-1
            self.printDocument()
            raw_input("Press Any Key to Continue")
            self.position = defaultPosition
        
        elif cmd == "-v":
            self.clear()
            for i in range(len(self.lines)):
                print self.lines[i]
            raw_input("Press Any Key to Continue")
            
        elif cmd == "-vs":
            self.getStartEnd()
            self.clear()
            self.position = self.end
            self.printDocument()
            raw_input("Press Any Key to Continue")
            self.start = self.defaultStart
        
        elif cmd == "-ps":
            self.getStartEnd()
            self.clear()
            for i in range(int(self.start), int(self.end+1)):
                print self.lines[i]
            raw_input("Press Any Key to Continue")
            self.start = self.defaultStart
            
        elif cmd == "-o":
            self.clear()
            self.programOpen(self.path)
            raw_input("Save and Close Program." + "\n" + "Press Any Key to Continue")
            self.lines = self.fillArray(self.path)
            self.save(self.path, self.lines)
        
        elif cmd == "-rld":
            self.clear()
            self.lines = self.fillArray(self.path)
            self.save(self.path, self.lines)
         
        elif cmd == "-end":
            self.position = len(self.lines)-1
            
        elif cmd == "-begin":
            self.position = 0
        
        elif cmd == "-i":
            self.undo = self.fillArray(self.path)
            insertPos = self.getLineNumber()
            print str(insertPos) + ": " + self.lines[insertPos]
            self.chooseIndent(insertPos)
            inp = raw_input(str(insertPos) + ": " + self.spaces)
            self.lines.insert(insertPos, self.spaces + str(inp) + '\n')
            self.save(self.path, self.lines)
        
        elif cmd == "-rs":
            self.undo = self.fillArray(self.path)
            self.getStartEnd()
            self.clear()
            self.replaceSelection(self.start, self.end)
            self.save(self.path, self.lines)
            self.start = self.defaultStart
        
        elif cmd == "-rep":
            self.undo = self.fillArray(self.path)
            selection = self.getLineNumber()
            self.replaceSelection(selection, selection)
            self.save(self.path, self.lines)
            
        elif cmd == "-rcl":
            self.undo = self.fillArray(self.path)
            self.replaceSelection(self.position, self.position)
            self.save(self.path, self.lines)
        
        elif cmd == "-del":
            self.undo = self.fillArray(self.path)
            selection = self.getLineNumber()
            self.deleteSelection(selection, selection)
            self.save(self.path, self.lines)
            self.position = selection-1
        
        elif cmd == "-ds":
            self.undo = self.fillArray(self.path)
            self.getStartEnd()
            self.clear()
            self.deleteSelection(self.start, self.end)
            self.save(self.path, self.lines)
            self.position = self.start-1
            self.start = self.defaultStart
        
        elif cmd == "-dcl":
            self.undo = self.fillArray(self.path)
            self.deleteSelection(self.position, self.position)
            self.save(self.path, self.lines)
            self.position = self.position-1
            
        elif cmd == "-b":
            if(self.position == 0):
                self.position = len(self.lines)-1
            else:
                self.position = self.position-1
            self.setIndent(self.getTabs(self.position))
        
        elif cmd == "-g":
            self.position = int(self.getLineNumber())
        
        elif cmd == "-f":
            try:
                inp = str(raw_input("Find: "))
                self.clear()
                for i in range(len(self.lines)):
                    if(self.lines[i].find(inp) != -1):
                        print str(i) + ": " + self.lines[i]
                raw_input("Press Any Key To Continue")
            except Exception:
                print "----Invalid Input----"
                raw_input("Continue? (Hit Enter) ")
        
        elif cmd == "-fr":
            try:
                inp = str(raw_input("Find and Replace: "))
                self.clear()
                for i in range(len(self.lines)):
                    if(self.lines[i].find(inp) != -1):
                        self.replaceSelection(i,i)
            except Exception:
                print "----Invalid Input----"
                raw_input("Continue? (Hit Enter) ")

        elif cmd == "-exp":
            prompt = raw_input("Open After Exporting? (y/n): ")
            if prompt == "y" :
                self.save(self.path, self.lines)
                tempPath = self.getDirectory()
                if tempPath != "Fail":
                    self.save(tempPath, self.lines)
                    self.deleteSwap()
                    sys.argv.append(tempPath)
                    self.startUp()
            else:
                tempPath = self.getDirectory()
                if tempPath != "Fail":
                    self.save(tempPath, self.lines)
        
        elif cmd == "-run":
            killSwitch = False
            while(killSwitch == False):
                self.run()
                quit = raw_input("Continue? y/n")
                if quit == "n":
                    killSwitch = True
        
        elif cmd == "-oe":
            tempPath = self.getDirectory()
            if tempPath != "Fail":
                self.programOpen(tempPath)
            
        elif self.position == (len(self.lines)-1) and cmd != "":
            self.undo = self.fillArray(self.path)
            self.lines.append(self.spaces + str(cmd) + '\n')
            self.save(self.path, self.lines)
            self.position += 1
            self.setIndent(self.getTabs(self.position))
            
        elif self.position < (len(self.lines)-1) and cmd != "":
            self.undo = self.fillArray(self.path)
            self.lines.insert(self.position+1, self.spaces + str(cmd) + '\n')
            self.save(self.path, self.lines)
            self.position += 1
            self.setIndent(self.getTabs(self.position))
        
        elif cmd == "" and self.position < (len(self.lines)-1):
            self.position += 1
        
        elif cmd == "" and self.position == (len(self.lines)-1):
            self.position = 0
        
        else:
            self.position += 1
            
        if cmd == "":
            self.setIndent(self.getTabs(self.position))
         
        if(self.position > (len(self.lines)-1)):
            self.position = 0
             
        self.save(self.path, self.lines)
        lines = self.fillArray(self.path)
         
        return self.kill

    def helpMenu(self):
        self.clear()
        print "-------------------------------------------"
        print "-| Write Text and Hit Enter to Insert    |-"
        print "-| Your Text on the Line Shown on the    |-"
        print "-| Bottom Left Corner of the Terminal    |-"
        print "-------------------------------------------"
        print "-| Hit Enter At Any Time While the Input |-"
        print "-| Line is Empty to View Next Line       |-"
        print "-------------------------------------------"
        print "-| -q       |Quit Program / oneLine Mode  -"
        print "-------------------------------------------"
        print "-| -run     |Takes a Terminal/CMD Command -"
        print "-------------------------------------------"
        print "-| -rld     |Reloads from document        -"
        print "-------------------------------------------"
        print "-| -o       |Opens in Default Program     -"
        print "-------------------------------------------"
        print "-| -b       |Moves to Previous Line       -"
        print "-------------------------------------------"
        print "-| -g       |Goes to Specified Line       -"
        print "-------------------------------------------"
        print "-| -f       |Finds inputed text           -"
        print "-------------------------------------------"
        print "-| -fr      |Finds and replaces lines     -"
        print "-|          |containing passed value      -"
        print "-------------------------------------------"
        print "-| -i       |Inserts at Chosen Line       -"
        print "-------------------------------------------"
        print "-| -id      |Requests and Sets # of Tabs  -"
        print "-------------------------------------------"
        print "-| -idp     |Removes 4 spaces from indent -"
        print "-------------------------------------------"
        print "-| -t       |Adds 4 space to the indent   -"
        print "-------------------------------------------"
        print "-| -ida     |Sets Indent to Match Previous-"
        print "-------------------------------------------"
        print "-| -vs      |Print Selection, Insert      -"
        print "-|          |Starts at End of Selection   -"
        print "-------------------------------------------"
        print "-| -rs      |Replaces Selection One Line  -"
        print "-|          |At a Time                    -"
        print "-------------------------------------------"
        print "-| -ds      |Deletes Selection            -"
        print "-------------------------------------------"
        print "-| -ps      |View Selection w/o Line #'s  -"
        print "-------------------------------------------"
        print "-| -dcl     |Deletes Current Line         -"
        print "-------------------------------------------"
        print "-| -del     |Deletes Specified Line       -"
        print "-------------------------------------------"
        print "-| -rcl     |Replaces Current Line        -"
        print "-------------------------------------------"
        print "-| -rep     |Replaces Specified Line      -"
        print "-------------------------------------------"
        print "-| -stab    |Replaces all leading tabs    -"
        print "-|          |with four spaces             -"
        print "-------------------------------------------"
        print "-| -sct     |Replace current lines tabs   -"
        print "-|          |with 4 spaces                -"
        print "-------------------------------------------"
        print "-| -sst     |Replaces selections tabs     -"
        print "-|          |with 4 spaces                -"
        print "-------------------------------------------"
        print "-| -rtl     | Reindent Current Line       -"
        print "-------------------------------------------"
        print "-| -rts     | Reindent Selection of Lines -"
        print "-------------------------------------------"
        print "-| -exp     |Exports Current File to New  -"
        print "-------------------------------------------"
        print "-| -end     |Jump to End                  -"
        print "-------------------------------------------"
        print "-| -begin   |Jump to Beginning            -"
        print "-------------------------------------------"
        print "-| -vl      |View Whole Doc With Line #'s -"
        print "-------------------------------------------"
        print "-| -v       |View Without Line #'s        -"
        print "-------------------------------------------"
        print "-| -ud      |Undo Last Change             -"
        print "-------------------------------------------"
        print "-| -rd      |Redo Last Change             -"
        print "-------------------------------------------"
        print "-| -cp      |Store Text for Insert        -"
        print "-------------------------------------------"
        print "-| -cs      |Store Selection for Insert   -"
        print "-------------------------------------------"
        print "-| -ccl     |Copy Current Line for Insert -"
        print "-------------------------------------------"
        print "-| -pst     |Paste to Current line        -"
        print "-------------------------------------------"
        print "-| -oe      |Open Separate Doc in Default -"
        print "-|          |Program                      -"
        print "-------------------------------------------"
        print "-| -on      |Open New File                -"
        print "-------------------------------------------"
        raw_input("Press Any Key to Return to Document")
    
    def replaceSelection(self, start, end):
        tempCount = start
        while(tempCount <= end):
            print "Replace? (n) to Return without Changes"
            print str(tempCount) + ": " + self.lines[tempCount]
            self.chooseIndent(tempCount)
            inp = str(raw_input(str(tempCount) + ": " + self.spaces))
            if inp != "n":
                self.lines[tempCount] = self.spaces + inp + '\n'
                self.save(self.path, self.lines)
                
            tempCount +=1
    
    def deleteSelection(self, start, end):
        tempCount = start
        review = raw_input("Review before deleting? y/n: ")
        if review == "y" or review == "Y":
            while(tempCount <= end):
                print "Delete? (n) to Return without Changes"
                print str(start) + ": " + self.lines[start]
                inp = str(raw_input(str(tempCount) + ": "))
                if inp != "n":
                    del self.lines[start]
                else:
                    start += 1
                tempCount +=1
        else:
            while(tempCount <= end):
                del self.lines[start]
                tempCount += 1
    
    def getLineNumber(self):
        try:
            position = int(raw_input("Enter Line Number: "))
            if position < 0 or position > (len(self.lines)-1):
                raise Exception
            else:
                return position
        except Exception:
            print "----Invalid Input----"
            raw_input("Press Any Key To Continue")
            return self.position
    
    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    
    def programOpen(self, path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Linux":
            subprocess.Popen(["xdg-open", path])
        else:
            subprocess.Popen(["open", path])
        
        
    def promptSave(self):
        answer = raw_input("Save before quiting?(y/n)")
        if answer != "n" and answer != "N":
            self.save(self.path, self.lines)
        else:
            self.lines = []
            self.lines = self.fillArray(self.swapPath)
            self.save(self.path, self.lines)
    
    def deleteSwap(self):
        if self.path != "":
            os.remove(self.swapPath)
    
    def save(self,path,lines):
        with open(str(path), 'w+') as f:
            for i in range(len(lines)):
                f.write(str(lines[i]))
    
    def checkPath(self,path):
        try:
            if(os.path.isfile(path)):
                return str(path)
            elif(os.path.isdir(path) == False):
                return path
            else:
                raise Exception
        except Exception:
            print "---Invalid File Path----"
            raw_input("Press Any Key to Continue")
            return "Fail"
    
    def getDirectory(self):
        print "Enter Path to Item You Wish to Open or Create"
        print "*Including Extension ie '.txt'"
        path = str(raw_input("Enter Full Path or (n): "))
        if path == "n" or path == "":
            path = "Fail"
        else:
            path = self.checkPath(str(path))
        return path
    
    def createSwap(self):
        self.swapPath = str(self.path) + "-swap"
        self.save(self.swapPath, self.lines)
    
    
    def fillArray(self,path):
        try:
            lines = []
            with open(str(path), 'r+') as f:
                for line in f.readlines():
                    lines.append(line)
            return lines
        except Exception:
            return []
            
    def cNewCmd(self):
        if not self.lines:
            self.clear()
            print(str(self.path))
            lineZ = str(raw_input("0: "))
            with open(str(self.path), 'w+') as f:
                f.write(lineZ + '\n')
            self.lines.append(str(lineZ) + '\n')
        
    def run(self):
        try:
            cmd = raw_input("Enter Command to run in Terminal / CMD Prompt: ")
            os.system(str(cmd))
            
        except Exception:
            print "----Invalid Command----"
            raw_input("Continue? (Hit Enter) ")
            
    
    def getKill(self):
        return self.kill
                    
    def stripCopy(self, position):
        tempCopy = self.lines[position]
        tempCount = 0
        copy = ""

        for i in tempCopy:
            if i == " ":
                tempCount += 1
            elif i == "\t":
                tempCount += 1
            else:
                break
        for i in range(tempCount, len(tempCopy)):
            copy += tempCopy[i]
        return copy

    def getTabs(self, position):
        tempCount = 0
        for i in self.lines[position]:
            if i == " ":
                tempCount += 1
            elif i == "\t":
                tempCount += 4
            else:
                break
        if tempCount > 0:
            tempCount = tempCount/4
            return tempCount
        else:
            return 0
    def replaceTabs(self, line):
        chars = [];
        for i in line:
            if i == "\t":
                chars.append("    ")
            else:
                chars.append(i)
        line = ""
        for i in range(len(chars)):
            line += chars[i]
        return str(line)
         
def main():
    termdoc = Document()
    termdoc.startUp()
    kill = termdoc.getKill()
    
    while(kill != True):
        termdoc.printDocument()
        termdoc.getCmd()
        termdoc.executeCommand()
        kill = termdoc.getKill()
    
    if termdoc.path != "":
        termdoc.deleteSwap()
    raise SystemExit
            
main()
    


