#Created by Michael Winberry Feb 5 2017
#Version Created April 20 2017
#Terminal Docs Work station and Line by Line editor
#For education and personal use only
 
import os
import sys
import platform
import subprocess
 
def main():
    clear()
    
    if(len(sys.argv)-1 >= 1):
        checkPath = sys.argv[1]
        del sys.argv[1]
    else:
        checkPath = os.getcwd()
    if(os.path.isfile(checkPath)):
        path = str(os.path.abspath(checkPath))
        swapPath = path + "-swap"
        lines = fillArray(path)
        save(swapPath,lines)
        position = 0
  
    elif(os.path.exists(checkPath) == False):
        path = cNewCmd(os.path.abspath(checkPath))
        swapPath = path + "-swap"
        lines = fillArray(path)
        save(swapPath,lines)
        position = 0

    else:
        path = cNew()
        swapPath = path + "-swap"
        lines = fillArray(path)
        save(swapPath,lines)
        position = 0

    saveState = writer(swapPath,path,lines,0,position)

    swapPath = saveState[1]
 
    if (saveState[0] == True):
        deleteSwap(swapPath)
    else:
        lines = fillArray(swapPath)
        save(path,lines)
        deleteSwap(swapPath)
        
    raise SystemExit

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
        if(lines == []):
            with open(path,'w+') as f:
                f.write(str(raw_input("Enter First Line: ")) + "\n")
        if(start < 0):
            start = 0;
        count = start
        
        if(position > len(lines)-1):
            position = len(lines)-1
            
        print "Help Menu (-h)"
        
        while( count <= position):
            print str(count) + ": " + lines[count]
            count += 1
        inp = raw_input(str(position+1) + ": ")
            
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
        
    killSwitch = 0
    
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
        
def executeCommand(swapPath,path,lines,position,inp,copy,undoStack,redoStack):
    if(str(inp) == "-paste"):
        inp = copy
    if(str(inp) == "-q"):
        clear()
        return [1,swapPath,path,lines,0,position,copy,undoStack,redoStack]
    
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
        print "-| -pSelect |Prints Selection, Insert     -"
        print "-|          |Starts at End of Selection   -"
        print "-------------------------------------------"
        print "-| -rSelect |Replaces Selection One Line  -"
        print "-|          |At a Time                    -"
        print "-------------------------------------------"
        print "-| -dSelect |Deletes Selection            -"
        print "-------------------------------------------"
        print "-| -vSelect |View Selection Without Lines -"
        print "-------------------------------------------"
        print "-| -dcl     |Deletes Current Line         -"
        print "-------------------------------------------"
        print "-| -delete  |Deletes Specified Line       -"
        print "-------------------------------------------"
        print "-| -rcl     |Replaces Current Line        -"
        print "-------------------------------------------"
        print "-| -replace |Replaces Specified Line      -"
        print "-------------------------------------------"
        print "-| -exp     |Exports Current File to New  -"
        print "-------------------------------------------"
        print "-| -oe      |Opens New Program in Default -"
        print "-|          |Environment                  -"
        print "-------------------------------------------"
        print "-| -end     |Jump to End                  -"
        print "-------------------------------------------"
        print "-| -begin   |Jump to Beginning            -"
        print "-------------------------------------------"
        print "-| -viewL   |View Whole Doc With Line #'s -"
        print "-------------------------------------------"
        print "-| -view    |View Without Line #'s        -"
        print "-------------------------------------------"
        print "-| -undo    |Undo Last Change             -"
        print "-------------------------------------------"
        print "-| -redo    |Redo Last Change             -"
        print "-------------------------------------------"
        print "-| -copy    |Store Text for Insert        -"
        print "-------------------------------------------"
        print "-| -cSelect |Store Selection for Insert   -"
        print "-------------------------------------------"
        print "-| -ccl     |Copy Current Line for Insert -"
        print "-------------------------------------------"
        print "-| -paste   |Paste to Current line        -"
        print "-------------------------------------------"
        
        raw_input("Continue? (Hit Enter) ")
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp) == "-copy"):
        copy = str(raw_input("Store Input: "))
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
   
    elif(str(inp) == "-ccl"):
        copy = str(lines[position])
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp) == "-cSelect"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            end = int(raw_input("Enter Ending Line: "))
            count = start
            copy = ""
            if (end > (len(lines)-1)):
                raise Exception
            if (start < 0):
                raise Exception
            while(count <= end):
                copy += str(lines[count])
                count += 1
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Selection----"
            print "---- No Changes Made ----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp) == "-undo"):
        redoStack = fillArray(path)
        save(path,undoStack)
        lines = fillArray(path)
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
 
    elif(str(inp) == "-redo"):
        undoStack = fillArray(path)
        save(path,redoStack)
        lines = fillArray(path)
        position += 1
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
        

    elif(str(inp)== "-viewL"):
        clear()
        for i in range(len(lines)-1):
            print str(i) + ": " + lines[i]
            if (i % 100 == 0 and i != 0):
                inp = raw_input("Continue? (n) ")
                if (str(inp) == "n"):
                    return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]

        raw_input("Continue? (Hit Enter) ")
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]

    elif(str(inp)== "-view"):
        clear()
        for i in range(len(lines)-1):
            print lines[i]
            if (i % 100 == 0 and i != 0):
                inp = raw_input("Continue? (n) ")
                if (str(inp) == "n"):
                    return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
        raw_input("Continue? (Hit Enter) ")
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp)=="-vSelect"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            end   = int(raw_input("Enter Ending Line:   "))
            clear()
            count = start
            while (count <= end):
                print lines[count]
                count += 1
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,position-20,position,copy]
        except Exception:
            print "----Invalid Entry----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
 
    
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
    
    elif(str(inp) == "-end"):
        return [0,swapPath,path,lines,len(lines)-20,len(lines)-1,copy,undoStack,redoStack]
    
    elif(str(inp) == "-begin"):
        return [0,swapPath,path,lines,0,0,copy,undoStack,redoStack]
    
    elif(str(inp) == "-pSelect"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            end = int(raw_input("Enter Ending Line: "))
            clear()
            return [0,swapPath,path,lines,start,end,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Entry----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,len(lines)-20,len(lines)-1,copy]
 
    elif(str(inp) == "-rSelect"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            count = start
            end = int(raw_input("Enter Ending Line: "))
            clear()
            undoStack = fillArray(path)
            while(count <= end):
                print("Replace? (n) to Return without Changes")
                print(str(count) + ": " + lines[count])
                inp = raw_input(str(count) + ": ")
                if (str(inp) != "n"):
                    lines[count] = str(inp) + '\n'
                    count += 1
                    save(path,lines)
                else:
                    count += 1
            return [0,swapPath,path,lines,end-20,end,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Entry-----"
            raw_input("Continue? (Hit Enter) ")
            undoStack = fillArray(path)
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
 
    elif(str(inp)== "-replace"):
        try:
            selection = int(raw_input("Enter Line # to Replace: "))
            print(str(selection) + ": " + lines[selection])
            inp = raw_input(str(selection) + ": ")
            if(inp != ""):
                undoStack = fillArray(path)
                lines[selection] = str(inp) + '\n'
                save(path,lines)
                return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
            else:
                inp2 = raw_input("Delete? (y) ")
                if(inp2 == "y"):
                    del lines[selection]
                    undoStack = fillArray(path)
                    save(path,lines)
                    undoStack = fillArray(path)
                    return [0,swapPath,path,lines,position-20,position,copy]
                else:
                    print "----No Changes Made----"
                    raw_input("Continue? (Hit Enter) ")
                    return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
        except Exception:
            print "----No Changes Made----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp) == "-rcl"):
        print(str(position) + ": " + lines[position])
        inp = raw_input(str(position) + ": ")
        if(inp != ""):
            undoStack = fillArray(path)
            lines[position] = str(inp) + '\n'
            save(path,lines)
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
        else:
            inp2 = raw_input("Delete? (y) ")
            if(inp2 == "y"):
                undoStack = fillArray(path)
                del lines[position]
                save(path,lines)
                return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
            else:
                print "----No Changes Made----"
                raw_input("Continue? (Hit Enter) ")
                return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp) == "-delete"):
        try:
            inp = int(raw_input("Line Number: "))
            print(str(inp) + ": " + lines[inp])
            inp2 = raw_input("Delete? (y) ")
            if (inp2 == "y"):
                undoStack = fillArray(path)
                del lines[inp]
                save(path, lines)
                return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
            else:
                print "----No Changes Made----"
                raw_input("Continue? (Hit Enter) ")
                return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Entry----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp)== "-dSelect"):
        try:
            start = int(raw_input("Enter Starting Line: "))
            end = int(raw_input("Enter Ending Line: "))
            count = start
            if (end > (len(lines)-1)):
                raise Exception
            if (start < 0):
                raise Exception
            undoStack = fillArray(path)
            
            while(count <= end):
                del lines[start]
                count += 1
            save(path,lines)
            if(position > (len(lines)-1)):
                return [0,swapPath,path,lines,len(lines)-20,len(lines)-1,copy,undoStack,redoStack]
            else:
                return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
        except Exception:
            print "----Invalid Selection----"
            print "---- No Changes Made ----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp)=="-dcl"):
        print str(position) + ": " + lines[position]
        undoStack = fillArray(path)
        del lines[position]
        save(path,lines)
        if(position > len(lines)-1):
            position = (len(lines)-1)
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp)=="-b"):
        if(position == 0):
            position = len(lines) -1
        else:
            position = position - 1
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]

    elif(str(inp) == "-g"):
        try:
            inp = raw_input("Enter Line Number: ")
            position = goTo(inp,position)
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
        except Except:
            print "----Invalid Input----"
            raw_input("Continue? (Hit Enter) ")
            return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]

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
    
    elif(str(inp) == "-oe"):
        path2 = openPath()
        programOpen(path2)
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp) == "-run"):
        killSwitch = 0
        while(killSwitch == 0):
            run()
            inp = raw_input("Continue? y/n")
            if(inp == 'n'):
                clear()
                killSwitch = 1
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(position == len(lines)-1 and str(inp) != ""):
        undoStack = fillArray(path)
        lines.append(str(inp) + '\n')
        save(path,lines)
        position +=1
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(position < len(lines) and str(inp) != ""):
        undoStack = fillArray(path)
        lines.insert(position+1, str(inp) + '\n')
        save(path,lines)
        position +=1
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp) == "" and position < (len(lines)-1)):
        position +=1
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    
    elif(str(inp) == "" and position == (len(lines)-1)):
        position = 0
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
    else:
        return [0,swapPath,path,lines,position-20,position,copy,undoStack,redoStack]
       
 
def deleteSwap(path):
    os.remove(path)
    return
 

def getDirectory():
    try:
        print("Enter Path to Item You Wish to Open or Create")
        print("*Including Extension ie '.txt'")
        path = raw_input("Enter Full Path or (n): ")
        if(path == "n"):
            raise SystemExit
        elif(os.path.isfile(path)):
            return path
        elif(os.path.isdir(path) == False):
		return path
        else:
            raise Exception
    except Exception:
        print "----Invalid File Path----"
        raw_input("Continue? (Hit Enter) ")
        main()
 
def cNew():
    try:
        nPath = getDirectory()
        if(os.path.exists(nPath)):
            return nPath
        else:
            with open(nPath, 'w+') as f:
                f.write(" " + '\n')
            return nPath
    except Exception:
        print "----Invalid Option----"
        raw_input("Continue? (Hit Enter) ")
        main()
    
def cNewCmd(path):
    with open(path, 'w+') as f:
        f.write(" " + '\n')
    return path

def fillArray(path):
    try:
        lines = []
        with open(path, 'r+') as f:
            for line in f.readlines():
                lines.append(line)
        return lines
    except Exception:
        print("----File Does Not Exist----")
        raw_input("Continue? (Hit Enter) ")
        main()
 

       
def goTo(newPos, oldPos):
    try:
        position = int(newPos)
        return position
    except Exception:
        print "----Invalid Entry----"
        print "----Returning to Last Position-----"
        raw_input("Continue? (Hit Enter) ")
        return oldPos

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
    
 
def save(path,lines):
    with open(path, 'w+') as f:
        for i in range(len(lines)):
            f.write(str(lines[i]))
    return
            
def programOpen(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Linux":
        subprocess.Popen(["xdg-open", path])
    else:
        subprocess.Popen(["open", path])
    return
 
def run():
    try:
        cmd = raw_input("Enter Command to run in Terminal / CMD Prompt: ")
        os.system(str(cmd))
        return
    except Exception:
        print "----Invalid Command----"
        raw_input("Continue? (Hit Enter) ")
        return

def clear():
    for i in range(100):
        print "\n"
    return
        
main()
 
