from lib.user_input import UserInput
from lib.document import Document
 
def main():
    prompt = UserInput()
    path = prompt.path()
    document = Document(path)
    print(str(path))
    print(document.path)
    print(prompt.cmd(12))
    document.set_offset(prompt.start())
    document.set_position(prompt.end())
    print("________________")
    print(document.offset)
    print(document.position)
 
main()
