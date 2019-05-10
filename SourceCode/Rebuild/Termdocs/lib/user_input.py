 
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
     
    def tab_width(self):
        print("Number of spaces or 0 for tab")
        new_tab_width = input("#: ")
        return new_tab_width
 
    def line_spacing(self):
        print("Number of additional line breaks to be displayed between lines.")
        new_line_spacing = input("#: ")
        return new_line_spacing

    def offset(self):
        print("Offset is the number of lines shown on screen")
        new_offset = input("#: ")
        return new_offset

    def line_number(self):
        new_line = input("Line #: ")
        return new_line

    def swap_exists(self):
        print("Document may be open in termdocs.")
        continue_result = input("Continue at your own risk y/n: ")
        return continue_result
