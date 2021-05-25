string = "pralay is a good boy"
result = ''
K = '*'
N = 5
for idx, ele in enumerate(string):
    if idx % N == 0 and idx != 0:
        result = result + K
    else:
        result = result + ele
print("New string: ", str(result))
