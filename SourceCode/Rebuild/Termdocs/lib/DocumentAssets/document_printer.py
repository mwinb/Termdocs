class DocumentPrinter():

    def __init__(self):
        pass

    def with_numbers(self, lines, start, end, spacing):
        current = start
        while(current <= end):
            print(str(current + 1) + ": " + lines[current] + spacing)
            current += 1

    def without_numbers(self, lines, start, end, spacing):
        current = start
        while(current <= end):
            print(lines[current] + spacing)
            current += 1


