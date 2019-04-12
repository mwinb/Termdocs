
from lib.type_tester import TypeTester
 
def main():
    tester = TypeTester()
    tester.integer(23)
    tester.integer("sdflkj")
    tester.integer([])
 
main()
