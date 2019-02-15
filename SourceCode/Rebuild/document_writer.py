class DocumentWriter:
    path = ""

    def __init__(self, path):
        self.path = path

    def set_path(self, path):
        self.path = path
    
    def get_path(self):
        return self.path
    
    def write(self, lines):
        try:
            with open(self.path, 'w+') as f:
                for i in range(len(lines)):
                    f.write(str(lines[i]))
        except Exception:
            print("Exception: " + Exception)
            return -1





    
