list = [1, 8, 10, 16, 23, 77, 60]
even_count = 0
odd_count = 0
for num in list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even count is: ", even_count)
print("Odd count is: ", odd_count)

