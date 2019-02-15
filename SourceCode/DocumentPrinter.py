import document.py

class DocumentPrinter(document):

    def __init__(self, offset):
        self.offset = offset
    
    def set_offset(self, offset):
        self.offset = offset
    
    def get_offset(self):
        return self.offset
    
    def get_first_line(last_line, offset):
        first_line = 0
        if offset != first_line
            first_line = last_line - offset
        return first_line

    
    def print_document(self, document):
        current_line = self.get_first_line(last_line, offset)
        while(current_line <= last_line):
            print(str(current_line) + ": " + document.lines[current_line])
            current_line += 1
    


