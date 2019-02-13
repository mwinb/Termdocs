class Document:
    swap_extension = "~swap"
    path = ""
    swap_path = ""
    position = 0

    def __init__(self, path):
        self.path = path
        self.swapPath = path + self.swap_extension
    
    def get_path(self):
        return self.path

    def set_path(self, new_path):
        self.path = new_path
        self.swap_path = new_path + self.swap_extension
        return True

    def getPosition(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position
        return True
