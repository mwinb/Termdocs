class DocumentReader:
    path = ""

    def __init__(self, path):
        self.path = path

    def read_lines(self):
        lines = []
        try:
            with open(self.path, 'r+') as f:
                for line in f.readlines():
                    lines.append(line)
            return lines
        except Exception as exception:
            print("\n-- Exception: " + exception + " --")
            print("-- Press any key to continue --\n")
            return []
