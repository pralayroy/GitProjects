def alphaCount_rec(inputStr, cur_char, count):
    if len(inputStr) == 0:
        return cur_char + str(count)

    if inputStr[0] == cur_char:
        return alphaCount_rec(inputStr[1:], cur_char, count + 1)

    return cur_char + str(count) + alphaCount_rec(inputStr[1:], inputStr[0], 1)


def alphaCount(inputStr):
    if len(inputStr) == 0:
        return ""
    return alphaCount_rec(inputStr[1:], inputStr[0], 1)


inputStr = 'aaabbefa'
print(alphaCount(inputStr))