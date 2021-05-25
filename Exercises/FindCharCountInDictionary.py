string = "Pralay Roy"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for key, value in char_count.items():
    if value > 1:
        char_count[key] = value
print(char_count)


"""
for key, value in duplicates.items():
    if value not in duplicates:
        duplicates[value] = key
    else:
        duplicates[value].append(key)
print(duplicates)
"""
