class Document:
    swap_extension = "~swap"
    path = ""
    swap_path = ""
    position = 0
    lines = []

    def __init__(self, path):
        self.path = path
        self.swap_path = path + self.swap_extension

    def to_string(self):
        print("Path: " + self.path)
        print("Swap: " + self.swap_path)
        print("Position: " + str(self.position))
