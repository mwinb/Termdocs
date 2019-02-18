class DocumentPrinter():

    def __init__(self, lines):
        self.lines = lines

    def print_document(self, lines):
        count = 1
        for line in lines:
            print(str(count) + ": " + line)
            count += 1



