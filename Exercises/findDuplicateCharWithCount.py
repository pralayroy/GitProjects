string = 'Pralay Roy'
duplicates = {}
for char in string:
    if char in duplicates:
        duplicates[char] += 1
    else:
        duplicates[char] = 1
for key, value in duplicates.items():
    if value > 1:
        print(key, '::', value)

