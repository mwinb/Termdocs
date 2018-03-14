class Document:
    path = "";
    lines = [];
    swapPath = this.path + "-swap";
    copy = "";
    cmd = "";
    start = 0;
    end = 0;
    position = 0;
    
    def printDocument():
        for i in range(this.position):
            print(i + ": " + lines);
    
    def getCmd():
        return str(raw_input(this.position + ": ");
    
    def getStartEnd() :
        try:
            startTemp = int(raw_input("Enter Starting Line #: "));
            endTemp = int(raw_input("Enter Ending Line #: "));
            if this.startTemp >= (len(this.lines)) or this.start < 0:
                raise Exception;
            elif this.endTemp >= (len(this.lines)) or this.end < 0:
                raise Exception
            else:
                this.start = startTemp;
                this.end = endTemp;
        except Exception:
            print "----Invalid File Path----";
            raw_input("Press Any Key to Continue");
    
    def executeCommand():
        this.clear();
        this.printDocument();
        this.cmd = getCmd();
        
        this.save();
        return 0;

    
    def helpMenu():
        this.clear();
        print "-------------------------------------------";
        print "-| Write Text and Hit Enter to Insert    |-";
        print "-| Your Text on the Line Shown on the    |-";
        print "-| Bottom Left Corner of the Terminal    |-";
        print "-------------------------------------------";
        print "-| Hit Enter At Any Time While the Input |-";
        print "-| Line is Empty to View Next Line       |-";
        print "-------------------------------------------";
        print "-| -q       |Quit Program / oneLine Mode  -";
        print "-------------------------------------------";
        print "-| -run     |Takes a Terminal/CMD Command -";
        print "-------------------------------------------";
        print "-| -o       |Opens in Default Program     -";
        print "-------------------------------------------";
        print "-| -b       |Moves to Previous Line       -";
        print "-------------------------------------------";
        print "-| -g       |Goes to Specified Line       -";
        print "-------------------------------------------";
        print "-| -f      |Finds inputed text           -";
        print "-------------------------------------------";
        print "-| -i      |Inserts at Chosen Line       -";
        print "-------------------------------------------";
        print "-| -ps      |Prints Selection, Insert     -";
        print "-|          |Starts at End of Selection   -";
        print "-------------------------------------------";
        print "-| -rs      |Replaces Selection One Line  -";
        print "-|          |At a Time                    -";
        print "-------------------------------------------";
        print "-| -ds      |Deletes Selection            -";
        print "-------------------------------------------";
        print "-| -vs      |View Selection Without Lines -";
        print "-------------------------------------------";
        print "-| -dcl     |Deletes Current Line         -";
        print "-------------------------------------------";
        print "-| -del     |Deletes Specified Line       -";
        print "-------------------------------------------";
        print "-| -rcl     |Replaces Current Line        -";
        print "-------------------------------------------";
        print "-| -rep     |Replaces Specified Line      -";
        print "-------------------------------------------";
        print "-| -exp     |Exports Current File to New  -";
        print "-------------------------------------------";
        print "-| -end     |Jump to End                  -";
        print "-------------------------------------------";
        print "-| -begin   |Jump to Beginning            -";
        print "-------------------------------------------";
        print "-| -vl      |View Whole Doc With Line #'s -";
        print "-------------------------------------------";
        print "-| -v       |View Without Line #'s        -";
        print "-------------------------------------------";
        print "-| -ud      |Undo Last Change             -";
        print "-------------------------------------------";
        print "-| -rd      |Redo Last Change             -";
        print "-------------------------------------------";
        print "-| -cp      |Store Text for Insert        -";
        print "-------------------------------------------";
        print "-| -cs      |Store Selection for Insert   -";
        print "-------------------------------------------";
        print "-| -ccl     |Copy Current Line for Insert -";
        print "-------------------------------------------";
        print "-| -pst     |Paste to Current line        -";
        print "-------------------------------------------";
        print "-| -oe      |Open Separate Doc in Default -";
        print "-|          |Program                      -";
        print "-------------------------------------------";
        raw_input("Press Any Key to Return to Document");
    
    def goTo():
        try:
            this.position = str(raw_input("Enter Line Number: "));
        except Exception:
            print "----Invalid Input----";
            raw_input("Press Any Key to Return to Document");
    
    def clear():
        if platform.system() == 'Windows':
            os.system('cls');
        else:
            os.system('clear');
    
    def programOpen():
        if platform.system() == "Windows":
            os.startfile(this.path);
        elif platform.system() == "Linux":
            subprocess.Popen(["xdg-open", this.path]);
        else:
            subprocess.Popen(["open", this.path]);
        raw_input("Save and Close Program." + "\n" + "Press Any Key to Continue");
    
    def save():
        with open(this.path, 'w+') as f:
            for i in range(len(lines)):
                f.write(str(lines[i]));
    
    def getDirectory():
        try:
            print "Enter Path to Item You Wish to Open or Create";
            print "*Including Extension ie '.txt'";
            path = raw_input("Enter Full Path or (n): ");
            if(path == "n"):
                raise SystemExit;
            elif(os.path.isfile(path)):
                this.path = path;
                this.lines = fillArray();
            elif(os.pathisdir(path) == False):
                this.path = path;
                cNewCmd();
            else:
                raise Exception
        except Exception:
            print "----Invalid File Path----";
            raw_input("Press Any Key to Continue");
    
    def cNewCmd():
        print(this.path)
        if not lines:
            lineZ = raw_input("0: ");
            with open(this.path, 'w+') as f:
                f.write(lineZ + '\n');
        else:
            with open(path, 'w+') as f:
                for i in range(len(lines)):
                    f.write(lines[i]);
    
        
        
        
    