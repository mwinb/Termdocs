# Terminal Docs Lite ie termdocs

Terminal Docs Lite (ie termdocs for quick terminal calling)
 
**Should you use Termdocs or Terminal Docs:**
 
Terminal Docs offers a file explorer and is recommended for casual users or as a no install needed text editor/viewer for Mac and Windows when away from personal computer. 
 
TermDocs offers a command line only version that is half the size, more convienent, and faster, if you are comfortable working strictly within a shell, and do not mind a manual install (Covered in instructions). 
 
Termdocs maintains most of the features of Terminal Docs except "-oe" command and the file explorer. -oe removed because it is easier to use the built in "-run" command to handle possible path input errors than to do it natively. 

**About Terminal Docs and Terminal Docs Lite:**
 
Terminal Docs is a line by line text-editor,text-reader,and general purpose workstation. It allows for active insertion, replacement, deletion, and running Terminal/Windows cmd/shell commands for compiling and testing while using. Terminal Docs was written using Python 2.7 and compiled for Mac with py2app, linux and Windows with pyinstaller. In order to pass terminal paths to the Mac version, download termdocs-Mac, extract and follow instructions to install. Termdocs was compiled for all platforms using pyinstaller.

**Example Commands:**

Enter -h to view all commands. 

Enter -o to open into default program and move back and forth between full ide and TerminalDocs for a more complete user experience. 

Enter -run to run Terminal Commands

**Typing text and entering it on the current line does not replace the text previously on this line, it simply inserts new text to current line and pushes old line down. In order to replace a line of text use one of the replace commands: -rcl (replaces current line), -rep (prompts for line # to replace), -rs (prompts for starting line # of begining and end of section to replace line by line).**
 
-created by Michael Winberry
 
-mwinb.github.io
 
-mwinberry0101@gmail.com


**Example of what to enter for path if using outside of command prompt or Unix/linux terminal**
 
**Windows:  termdocs.exe \users\yourusername\desktop\Instructions.txt**
 
**Mac/Linux:  termdocs ~/Desktop/Instructions.txt**
