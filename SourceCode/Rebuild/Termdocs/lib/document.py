class Document:
    swap_extension = "~swap"
    path = ""
    swap_path = ""
    position = 0
    offset = 0
    lines = []

    def __init__(self, path):
        self.path = path
        self.swap_path = path + self.swap_extension

    def to_string(self):
        print("Path: " + self.path)
        print("Swap: " + self.swap_path)
        print("Position: " + str(self.position))
        print("offset: " + str(self.offset))
     
    def set_offset(self, new_offset):
        if new_offset < 0:
            new_offset = 0
        if new_offset >= len(self.lines)-1:
            new_offset = 0
        self.offset = new_offset
         
    def set_position(self, new_position):
        if new_position > len(self.lines):
            new_position = len(self.lines) - 1
        if new_position < 0:
            new_position = 0
        self.position = new_position
