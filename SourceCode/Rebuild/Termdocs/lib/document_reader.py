from Classes import document
class DocumentReader:
    
    def __init__(self):
        pass

    def read_document(self, path):
        try:
            lines = []
            with open(path, 'r+') as f:
                for line in f.readlines():
                    lines.append(line)
            return lines
        except Exception as exception:
            print("\n-- Exception: " + str(exception) + " --")
            print("-- Press any key to continue --\n")
            return []
