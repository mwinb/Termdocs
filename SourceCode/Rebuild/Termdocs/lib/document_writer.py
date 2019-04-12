class DocumentWriter:
    def __init__(self):
        pass

    def write(self, document):
        path = document.path
        lines = document.lines
        try:
            with open(path, 'w+') as f:
                for i in range(len(lines)):
                    f.write(str(lines[i]))
        except Exception as exception:
            print("\n-- Exception: " + exception + " ---")
            input("-- Press any key to continue. --")


