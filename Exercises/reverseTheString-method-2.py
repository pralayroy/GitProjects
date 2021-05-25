# Using Slicing
# Strings can be reversed using slicing. To reverse a string, we simply create a slice that starts
# with the length of the string, and ends at index 0

string = 'pralay'
stringlength = len(string)
slicedString = string[stringlength:: -1]
print("Reversed string is: ", slicedString)

