 
class UserInput:
    def __init__(self):
        pass
     
    def path(self):
        new_path = input("Enter path of new Document or n: ")
        return new_path
     
    def cmd(self, position):
        new_cmd = input(str(position) + ": ")
        return new_cmd
     
 
