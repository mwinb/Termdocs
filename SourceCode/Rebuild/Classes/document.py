class Document:
    swap_extension = "~swap"
    path = ""
    swap_path = ""
    position = 0
    lines = []

    def __init__(self, path):
        self.path = path
        self.swap_path = path + self.swap_extension
    
    def get_path(self):
        return self.path
    
    def get_swap_path(self):
        return self.swap_path

    def set_path(self, new_path):
        self.path = new_path
        self.swap_path = new_path + self.swap_extension
        return True

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position
        return True
    
    def set_lines(self, lines):
        self.lines = lines
    
    def get_lines(self):
        return self.lines

    def to_string(self):
        print("Path: " + self.path)
        print("Swap: " + self.swap_path)
        print("Position: " + str(self.position))
