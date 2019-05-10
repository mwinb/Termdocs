import os

class InputTester:
    continue_string = "Press any key to continue."
    def __init__(self):
        pass
     
    def integer(self, value):
        try:
            int(value)
            return True
        except:
            return False

    def in_bounds(self, value, document):
        test_result = False
        if value >= 0 and value < len(document.lines):
            test_result = True
        return test_result

    def valid_path(self, new_path):
        test_result = False
        if os.path.isfile(new_path):
            test_result = True
        return test_result

    def valid_swap(self, new_swap_path):
        test_result = True
        if os.path.isfile(new_swap_path):
            test_result = False
        return test_result

