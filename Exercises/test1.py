# Sort dictionary by values
dict = {'a': 2, 'b':4,'c':5, 'd':1}
sorted_dict = {}
sorted_keys = sorted(dict, key=dict.get)
for i in sorted_keys:
    sorted_dict[i] = dict[i]
print(sorted_dict)

