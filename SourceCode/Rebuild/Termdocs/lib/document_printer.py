class DocumentPrinter():

    def __init__(self, offset):
        self.offset = offset

    def print_document(self, lines):
        count = 1
        for line in range(self.offset):
            print(str(count) + ": " + lines[line])
            count += 1



