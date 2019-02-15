class DocumentReader:
    lines = []
    path = ""

    def __init__(self, path):
        self.path = path
        self.lines = self.read_lines()

    def get_lines(self):
        return self.lines

    def set_lines(self, path):
        self.lines = self.read_lines()

    def read_lines(self):
        lines = []
        try:
            with open(self.path, 'r+') as f:
                for line in f.readlines():
                    lines.append(line)
            return lines
        except Exception:
            print("Exception: " + Exception)
            return []
