import re


def specialChar(str):
    regex = re.compile('[@!$%^&*()+<>?/\.{}|`:~=]')
    if regex.search(str) is None:
        print("String has not special character")
    else:
        print("String has special character")


# if __name__ = '__main__':
str = "Pr@l@y"
specialChar(str)

