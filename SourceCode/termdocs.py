#Created by Michael Winberry Feb 5 2017
#Version Created Sep 22 2017
#Terminal Docs Lite Work station and Line by Line editor

 
import os
import sys
import platform
import subprocess


 
def main():
    clear()
    
    #checks number of cmd line args [1] is the position of the path
    if(len(sys.argv)-1 >= 1):
        checkPath = sys.argv[1]
        del sys.argv[1]
    #if no path sets path to current working directory
    else:
        checkPath = os.getcwd()

    #checks if path is an existing file
    #Uses path as document. Fills array and begins writer function
 
    if(os.path.isfile(checkPath)):
        path = str(os.path.abspath(checkPath))
        swapPath = path + "-swap"
        lines = fillArray(path)
        save(swapPath,lines)
        position = 0
 
    #creates file sys arg (passed path) if does not exist and is path is not DIR
    elif(os.path.isdir(checkPath) == False):
        path = str(os.path.abspath(checkPath))
        cNewCmd(path)
        swapPath = path + "-swap"
        lines = fillArray(path)
        save(swapPath,lines)
        position = 0

    # Uses manual input to create or open file
    else:
        path = getDirectory()
        swapPath = path + "-swap"
        lines = fillArray(path)
        save(swapPath,lines)
        position = 0

    #writer function is initiated
    #Returned array determines if changes will be saved
    saveState = writer(swapPath,path,lines,0,position)

    swapPath = saveState[1]
 

    #handles saving changes
    #if changes are saved swap is deleted
    #if changes are not saved, swap is written to original and then deleted
    if (saveState[0] == True):
        deleteSwap(swapPath)
    else:
        lines = fillArray(swapPath)
        save(path,lines)
        deleteSwap(swapPath)
        
    raise SystemExit

#Moves through array line by line while allowing for cmds to be entered
def writer(swapPath,path,lines,start,position):
    killSwitch = 0
    copy = ""
    undoStack = []
    redoStack = []
    undoStack = fillArray(path)
    redoStack = fillArray(path)
    
    while(killSwitch == 0):
        clear()
        save(path,lines)
        lines = fillArray(path)
        print path
        print "Help Menu (-h)"
        if(lines == []):
            with open(path,'w+') as f:
                f.write(str(raw_input("0: ")) + "\n")
            lines = fillArray(path)
            start = 0
            position = 1
            clear()
            print path
            print "Help Menu (-h)"
        if(start < 0):
            start = 0;
        count = start
        
        #sets position to 0 if end of document is reached
        if(position > len(lines)-1):
            position = 0
        #prints line numbers in front of doc lines
        #prints current line
        while( count <= position):
            print str(count) + ": " + lines[count]
            count += 1
        #prints current line number + 1 for active insertion
        inp = raw_input(str(position+1) + ": ")
            
        #Calls cmd function to handle input / lack there of for next line
        parameters = executeCommand(swapPath,path,lines,position,inp,copy,undoStack,redoStack)
        killSwitch = parameters[0]
        swapPath = parameters[1]
        path = parameters[2]
        lines = parameters[3]
        start = parameters[4]
        position = parameters[5]
        copy = parameters[6]
        undoStack = parameters[7]
        redoStack = parameters[8]
        
    #resets kill switch after loop is broken
    killSwitch = 0
    
    #prompts to save
    while(killSwitch == 0):
        inp = raw_input("Save? (y/n) ")
        if (inp == "y"):
            saveState = True
            killSwitch = 1
        elif (inp == "n"):
            saveState = False
            killSwitch = 1 
        else:
            print "-----Invalid Entry-----"
            
    parameters = [saveState,swapPath]
    return parameters
        
#Handles all posible commands returning parameters array
def executeCommand(swapPath,path,lines,position,inp,copy,undoStack,redoStack):
 
    #pastes text stored by "copy" on current line
    if(str(inp) == "-pst"):
        inp = copy
 
    #breaks cmnd input loop inside writer function, prompts for save
    if(str(inp) == "-q"):
        clear()
        return [1,swapPath,path,lines,0,position,copy,undoStack,redoStack]
    
    #prints command list
    elif(str(inp)=="-h"):
        clear()
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
        print "-| -o       |Opens in Default Program     -"
        print "-------------------------------------------"
        print "-| -b       |Moves to Previous Line       -"
        print "-------------------------------------------"
        print "-| -g       |Goes to Specified Line       -"
        print "-------------------------------------------"
        print "-| -ps      |Prints Selection, Insert     -"
        print "-|          |Starts at End of Selection   -"
        print "-------------------------------------------"
        print "-| -rs      |Replaces Selection One Line  -"
        print "-|          |At a Time                    -"
        print "-------------------------------------------"
        print "-| -ds      |Deletes Selection            -"
        print "-------------------------------------------"
        print "-| -vs      |View Selection Without Lines -"
        print "-------------------------------------------"
        print "-| -dcl     |Deletes Current Line         -"
        print "-------------------------------------------"
        print "-| -del     |Deletes Specified Line       -"
        print "-------------------------------------------"
        print "-| -rcl     |Replaces Current Line        -"
        print "-------------------------------------------"
        print "-| -rep     |Replaces Specified Line      -"
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
        
        raw_input("Continue? (Hit Enter) ")
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
    
#saves user input to be pasted
    elif(str(inp) == "-cp"):
        copy = str(raw_input("Store Input: "))
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
   
#stores current line to be pasted
    elif(str(inp) == "-ccl"):
        copy = str(lines[position])
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
    
#stores a selection to be pasted
    elif(str(inp) == "-cs"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            end = int(raw_input("Enter Ending Line: "))
            tempCount = start
            copy = ""
            if (end > (len(lines)-1)):
                raise Exception
            if (start < 0):
                raise Exception
            while(tempCount <= end):
                copy += str(lines[tempCount])
                tempCount += 1
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Selection----"
            print "---- No Changes Made ----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
    
#undoes last change
    elif(str(inp) == "-ud"):
        redoStack = fillArray(path)
        save(path,undoStack)
        lines = fillArray(path)
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#redoes last undo
    elif(str(inp) == "-rd"):
        undoStack = fillArray(path)
        save(path,redoStack)
        lines = fillArray(path)
        position += 1
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        

#prints entire doc w/ line #'s 
    elif(str(inp)== "-vl"):
        clear()
        for i in range(len(lines)):
            print str(i) + ": " + lines[i]

        raw_input("Continue? (Hit Enter) ")
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]

#prints entire document w/o line #'s
    elif(str(inp)== "-v"):
        clear()
        for i in range(len(lines)):
            print lines[i]

        raw_input("Continue? (Hit Enter) ")
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]

#prints selection w/o line #'s
    elif(str(inp)=="-vs"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            end   = int(raw_input("Enter Ending Line:   "))
            clear()
            while (start <= end):
                print lines[start]
                start += 1
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Entry----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]

#opens current document in default program (i.e. netbeans, intellij, xcode, wordpad)
    elif(str(inp)=="-o"):
        clear()
        programOpen(path)
        continueInp = raw_input("Continue? (q) to Quit: ")
        if(continueInp == "q"):
            return [1,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        else:
            lines = fillArray(path)
            save(path,lines)
            return [0,swapPath,path,lines,len(lines)-20,len(lines)-1,copy,undoStack,redoStack]

#jumps to last line
    elif(str(inp) == "-end"):
        return [0,swapPath,path,lines,len(lines)-20,len(lines)-1,copy,undoStack,redoStack]

#jumps to first line
    elif(str(inp) == "-begin"):
        return [0,swapPath,path,lines,0,0,copy,undoStack,redoStack]

#prints selection w/ line #'s
    elif(str(inp) == "-ps"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            end = int(raw_input("Enter Ending Line: "))
            return [0,swapPath,path,lines,start,end,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Entry----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]

#replaces selection one line at a time
    elif(str(inp) == "-rs"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            tempCount = start
            end = int(raw_input("Enter Ending Line: "))
            clear()
            undoStack = fillArray(path)
            while(tempCount <= end):
                print("Replace? (n) to Return without Changes")
                print(str(tempCount) + ": " + lines[tempCount])
                inp = raw_input(str(tempCount) + ": ")
                if (str(inp) != "n"):
                    lines[tempCount] = str(inp) + '\n'
                    tempCount += 1
                    save(path,lines)
                else:
                    tempCount += 1
            return [0,swapPath,path,lines,end-20,end,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Entry-----"
            raw_input("Continue? (Hit Enter) ")
            undoStack = fillArray(path)
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#replaces chosen line #
    elif(str(inp)== "-rep"):
        try:
            selection = int(raw_input("Enter Line # to Replace: "))
            print(str(selection) + ": " + lines[selection])
            inp = raw_input(str(selection) + ": ")
            if(inp != ""):
                undoStack = fillArray(path)
                lines[selection] = str(inp) + '\n'
                save(path,lines)
                return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
            else:
                inp2 = raw_input("Delete? (y) ")
                if(inp2 == "y"):
                    del lines[selection]
                    undoStack = fillArray(path)
                    save(path,lines)
                    undoStack = fillArray(path)
                    return [0,swapPath,path,lines,0,position,copy, undoStack, redoStack]
                else:
                    print "----No Changes Made----"
                    raw_input("Continue? (Hit Enter) ")
                    return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        except Exception:
            print "----No Changes Made----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#replaces current line
    elif(str(inp) == "-rcl"):
        print(str(position) + ": " + lines[position])
        inp = raw_input(str(position) + ": ")
        if(inp != ""):
            undoStack = fillArray(path)
            lines[position] = str(inp) + '\n'
            save(path,lines)
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        else:
            inp2 = raw_input("Delete? (y) ")
            if(inp2 == "y"):
                undoStack = fillArray(path)
                del lines[position]
                save(path,lines)
                return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
            else:
                print "----No Changes Made----"
                raw_input("Continue? (Hit Enter) ")
                return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#deletes inputed line #
    elif(str(inp) == "-del"):
        try:
            inp = int(raw_input("Line Number: "))
            print(str(inp) + ": " + lines[inp])
            inp2 = raw_input("Delete? (y) ")
            if (inp2 == "y"):
                undoStack = fillArray(path)
                del lines[inp]
                save(path, lines)
                return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
            else:
                print "----No Changes Made----"
                raw_input("Continue? (Hit Enter) ")
                return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Entry----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#deletes chosen range of lines
    elif(str(inp)== "-ds"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            end = int(raw_input("Enter Ending Line: "))
            tempCount = start
            if (end > (len(lines)-1)):
                raise Exception
            if (start < 0):
                raise Exception
            undoStack = fillArray(path)
            
            while(tempCount <= end):
                del lines[start]
                tempCount += 1
            save(path,lines)
            if(position > (len(lines)-1)):
                return [0,swapPath,path,lines,len(lines)-20,len(lines)-1,copy,undoStack,redoStack]
            else:
                return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Selection----"
            print "---- No Changes Made ----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#deletes current line
    elif(str(inp)=="-dcl"):
        print str(position) + ": " + lines[position]
        undoStack = fillArray(path)
        del lines[position]
        save(path,lines)
        if(position > len(lines)-1):
            position = (len(lines)-1)
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#Goes back one line
    elif(str(inp)=="-b"):
        if(position == 0):
            position = len(lines) -1
        else:
            position = position - 1
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#jumps to chosen line number
    elif(str(inp) == "-g"):
        try:
            inp = raw_input("Enter Line Number: ")
            position = goTo(inp,position)
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        except Except:
            print "----Invalid Input----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#exports to new document, and then opens
    elif(str(inp) == "-exp"):
        expPath = exp(lines)
        inp = raw_input("Open New? (y) ")
        if (inp == "y"):
            deleteSwap(swapPath)
            undoStack = []
            redoStack = []
            save(path,lines)
            lines = fillArray(expPath)
            swapPath = expPath + "-swap"
            save(swapPath,lines)
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
        else:
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
    
#executes input as a cmd/terminal cmd
    elif(str(inp) == "-run"):
        killSwitch = 0
        while(killSwitch == 0):
            run()
            inp = raw_input("Continue? y/n")
            if(inp == 'n'):
                clear()
                killSwitch = 1
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]

#opens new file in default program.
    elif(str(inp) == "-oe"):
        try:
            tempPath = getDirectory()
            programOpen(tempPath)
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]

        except Except:
            print "----Invalid Input----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]

#appends new line to document when current line is last line
    elif(position == len(lines)-1 and str(inp) != ""):
        undoStack = fillArray(path)
        lines.append(str(inp) + '\n')
        save(path,lines)
        position +=1
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]


#inserts new line if current line is not last line
    elif(position < len(lines) and str(inp) != ""):
        undoStack = fillArray(path)
        lines.insert(position+1, str(inp) + '\n')
        save(path,lines)
        position +=1
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#increases position if no new text is inserted (moves to next line in doc)
    elif(str(inp) == "" and position < len(lines)-1):
        position +=1
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
 
#moves to begining of document if no text is entered after last line
    elif(str(inp) == "" and position == len(lines)-1):
        position = 0
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
    else:
        return [0,swapPath,path,lines,0,position,copy,undoStack,redoStack]
       
#removes swap path when after saving in main function
def deleteSwap(path):
    os.remove(path)
    return

#prompts for directory path when none has been enter in cmd line (called from main/writer export)
def getDirectory():
    try:
        print "Enter Path to Item You Wish to Open or Create"
        print "*Including Extension ie '.txt'"
        path = raw_input("Enter Full Path or (n): ")
        if(path == "n"):
            raise SystemExit
        elif(os.path.isfile(path)):
            return path
        elif(os.path.isdir(path) == False):
            cNewCmd(path)
            return path
        else:
            raise Exception
    except Exception:
        print "----Invalid File Path----"
        raw_input("Continue? (Hit Enter) ")
        main()

#creates new document if path doesn't exist and allows entry of first line
def cNewCmd(path):
    print(path)
    lineZ = raw_input("0: ")
    with open(path, 'w+') as f:
        f.write(lineZ + '\n')
    return 

#fills array line x line from document
def fillArray(path):
    try:
        lines = []
        with open(path, 'r+') as f:
            for line in f.readlines():
                lines.append(line)
        return lines
    except Exception:
        print "----File Does Not Exist----"
        raw_input("Continue? (Hit Enter) ")
        main()
 
#sets position to new user entered line #
def goTo(newPos, oldPos):
    try:
        position = int(newPos)
        return position
    except Exception:
        print "----Invalid Entry----"
        print "----Returning to Last Position-----"
        raw_input("Continue? (Hit Enter) ")
        return oldPos

#writes lines to new document Called from writer -exp
def exp(lines):
    try:
        newPath = getDirectory()
        with open(newPath, 'w+') as f:
            for i in range(len(lines)):
                f.write(str(lines[i]))
        return newPath
    except Exception:
        print "----Invalid File----"
        raw_input("Continue? (Hit Enter) ")
        return
    
#Writes lines to document after changes
def save(path,lines):
    with open(path, 'w+') as f:
        for i in range(len(lines)):
            f.write(str(lines[i]))
    return

#Handles opening in default program (writer -o) for each os
def programOpen(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Linux":
        subprocess.Popen(["xdg-open", path])
    else:
        subprocess.Popen(["open", path])
    return

#runs shell/cmd command
def run():
    try:
        cmd = raw_input("Enter Command to run in Terminal / CMD Prompt: ")
        os.system(str(cmd))
        return
    except Exception:
        print "----Invalid Command----"
        raw_input("Continue? (Hit Enter) ")
        return
 
#forces blank lines to clear shell
def clear():
	if platform.system() == 'Windows':
		os.system('cls');
	else:
		os.system('clear');
	return

main()
