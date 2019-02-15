from document import Document
from document_reader import DocumentReader
from document_writer import DocumentWriter
from document_printer import DocumentPrinter

TEST_IN_PATH = "test_in.txt"
TEST_OUT_PATH = "test_out.txt"
PRINT_OFFSET = 0


def main():
    lines = []
    last_index = 0
    test_doc = Document(TEST_IN_PATH)
    doc_tests(test_doc)

    test_reader = DocumentReader(TEST_IN_PATH)
    test_printer = DocumentPrinter(PRINT_OFFSET)

    lines = test_reader.get_lines()
    last_index = len(lines) - 1
    test_doc.set_lines(lines)
    assert lines == test_doc.lines

    print_divider()
    test_printer.set_offset(20)
    test_printer.print_document(lines, last_index)
    print_divider()
    last_index = last_index - 20
    test_printer.print_document(lines, last_index)

def print_divider():
    print("__________________________")

def doc_tests(document):
    document.to_string()
    print_divider()
    document.set_path("IM_NOT_A_REAL_PATH")
    document.to_string()
    print_divider()
    document.set_path(TEST_IN_PATH)
    document.to_string()




main()




