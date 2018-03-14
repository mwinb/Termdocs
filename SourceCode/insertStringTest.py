line = "My name Is EnterHere"
word = "EnterHere"
newWord = "Michael"
index = line.find(word)
line = line[:index] + newWord + line[index+len(word):]
print line
