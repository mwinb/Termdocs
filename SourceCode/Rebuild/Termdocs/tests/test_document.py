import unittest
from lib.document import Document
 
test_path = "tests/test_in.txt"
class TestDocument(unittest.TestCase):
    def test_document(self):
        document = Document(test_path)
        self.assertEqual(document.path, test_path, "Document path should be : " + test_path)
 
    def test_document_swap(self):
        document = Document(test_path)
        self.assertEqual(document.swap_path, test_path + "~swap", "Document swap path should be : " + test_path + "~swap")
if __name__ == '__main__':
    unittest.main()
