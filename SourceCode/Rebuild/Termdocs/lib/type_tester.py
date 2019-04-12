class TypeTester:
    def __init__(self):
        pass
     
    def integer(self, value):
        try:
            int(value)
            return True
        except:
            input("Input Expected Integer and got: " + str(type(value)))
            return False
