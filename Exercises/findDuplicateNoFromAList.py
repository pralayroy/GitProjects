def duplicate(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


x = [1, 2, 5, 1, 7, 10, 2, 7]
print(duplicate(x))
