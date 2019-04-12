class DocumentPrinter():

    def __init__(self):
        pass

    def print(self, document):
        count = 0
        start = document.position - document.offset
        end = document.position
        lines = document.lines
         
        if end < 0:
            end = 0
        if start < 0 or start > end:
            start = 0
             
        while(count <= end):
            print(str(count+1) + ": " + lines[count])
            count += 1



