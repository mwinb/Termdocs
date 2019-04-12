from lib.user_input import UserInput
 
def main():
    prompt = UserInput()
    path = prompt.path()
    print(str(path))
    print(prompt.cmd(12))
 
main()
