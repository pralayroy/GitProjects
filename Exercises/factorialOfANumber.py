#num = 1
num = int(input('Enter the number : '))
factorial = 1
if num < 0:
    print("Sorry can't do factorial for negative no")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("Factorial of :", num, "is", factorial)


