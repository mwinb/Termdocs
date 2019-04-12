 
class UserInput:
    def __init__(self):
        pass
     
    def path(self):
        new_path = input("Enter path of new Document or n: ")
        return new_path
     
    def cmd(self, position):
        new_cmd = input(str(position) + ": ")
        return new_cmd
         
    def start(self):
        new_starting_line = input("Starting Line: ")
        return new_starting_line
     
    def end(self):
        new_ending_line = input("Ending Line: ")
        return new_ending_line
     
 
