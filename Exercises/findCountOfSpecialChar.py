string = input("Enter the string here: ")
alphabet = 0
digit = 0
specialChar = 0

for i in range(len(string)):
    if string[i].isalpha():
        alphabet = alphabet + 1
    elif string[i].isdigit():
        digit = digit + 1
    else:
        specialChar = specialChar + 1

print("No of alphabet is: ", alphabet)
print("No of digit is: ", digit)
print("No of special character: ", specialChar)
