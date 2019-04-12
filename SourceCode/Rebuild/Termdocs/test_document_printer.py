from lib.document import Document
from lib.document_printer import DocumentPrinter
 
def main():
    document = Document("TestPath")
    printer = DocumentPrinter()
    document.lines = ["1", "2", "3", "4"]
    for i in range(3):
        printer.print(document)
        print("_______________")
        document.set_position(document.position + 1)
    for i in range(4):
        document.set_offset(document.offset + 1)
        printer.print(document)
        print("______________")
    document.set_offset(0)
    document.set_position(0)
    for i in range(4):
        DocumentPrinter().print(document)
        print("___________________")
        document.set_position(document.position + 1)
    document.set_position(100)
    DocumentPrinter().print(document)
    document.set_offset(100)
main()
