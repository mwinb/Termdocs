class DocumentReader:
    lines = []

    def __init__(self, path):
        self.lines = self.read_lines(path)

    def get_lines(self):
        return self.lines
    
    def set_lines(self, path):
        self.lines = self.read_lines(path)

    def read_lines(self, path):
        try:
            lines = []
            with open(path, 'r+') as f:
                for line in f.readlines():
                    lines.append(line)
            return lines
        except Exception:
            return []
