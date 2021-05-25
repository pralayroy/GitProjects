"""
def checkTheString(str1, str2):
    if str2 in str1:
        print(str2, "- String is present")
    else:
        print("String is not present")


checkTheString("Hello Pralay", "Pralay")
"""


def checkStringPresent(str, substr):
    loc = str.find(substr)
    if loc == -1:     # if string is not present it will return -1
        print(substr, "- string is not present")
    else:
        print(substr, loc, "- string is present")  # If found, this method returns the location of
                                                   # the first occurrence of the substring


str1 = "Hello Pralay"
str2 = "Pralay"
# checkStringPresent(str1, str2)
checkStringPresent(str1, "That")
