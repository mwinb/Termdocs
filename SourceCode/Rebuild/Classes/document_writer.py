class DocumentWriter:
    lines = []
    path = ""

    def __init__(self, lines, path):
        self.lines = lines
        self.path = path
    
    def set_path(self, path):
        self.path = path
    
    def get_path(self):
        return self.path
    
    def set_lines(self, lines):
        return self.lines
    
    def get_lines(self):
        return self.lines

    def write(self):
        try:
            with open(self.path, 'w+') as f:
                for i in range(len(self.lines)):
                    f.write(str(self.lines[i]))
        except Exception as exception:
            print("\n-- Exception: " + exception + " ---")
            input("-- Press any key to continue. --")


