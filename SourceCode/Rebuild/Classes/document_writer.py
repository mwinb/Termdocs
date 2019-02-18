class DocumentWriter:
    lines = []
    path = ""

    def __init__(self, document):
        self.lines = document.lines
        self.path = document.path

    def write(self):
        try:
            with open(self.path, 'w+') as f:
                for i in range(len(self.lines)):
                    f.write(str(self.lines[i]))
        except Exception as exception:
            print("\n-- Exception: " + exception + " ---")
            input("-- Press any key to continue. --")


