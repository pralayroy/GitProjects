#Using loop

string = 'Pralay'
revstring = ""
index = len(string)
while index > 0:
    revstring += string[index - 1]
    index = index - 1
print("Reversed string is: ", revstring)

