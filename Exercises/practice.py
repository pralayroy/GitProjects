"""
lst = [1,2,3,4,5,6,7,8,9]
t = iter(x**x for x in lst)
print(next(t), next(t))
next(t)
print(next(t))

class demo():
    def __repr__(self):
        return 'prla'
    def __str__(self):
        return 'str'

s = demo()
s

x = 3
t = 4*3
print(t)

l1 = [2,4,6]
l2 =[-2,-4,-6]
for i in zip(l1,l2):
    print(i)


def f(x):
    def f1(a,b):
        print("hello")
        if b==0:
            print("No")
        return f(a,b)
    return f1

@f
def f(a,b):
    return a%b
f(4,0)


import re
p = re.compile('\d+')
print(p.findall("I met him once at 11 a.m on 4th July 1889"), end="")
p = re.compile('\d')
print(p.findall("I went to him at 11 a.m"))

n = 'abcd'
n[-1] = 'z'

class cha:
    def __init__(self,x, y,z):
        self.a = x+y+z
x = cha(1,2,3)
y = getattr(x,'a')
setattr(x,'a', y+1)
print(x.a)


import re
t = re.split('\w+', 'hello, hello, hello.')
print(t)

a = {5,6,7,8}
b ={8,6,5,7}
print(a==b)


def sam(a, b, c,d):
    print(a+b)

n = [1,2,3,4]
sam(*n)

x =4
for j in range(x):
    for i in range(x):
        print(i)
        x = 2


try:
    if '1'!=1:
        raise ("SomeError")
    else:
        print("No error")
except "Error":
    print("some error")

t = 32.00
[round((x-32)*5/9) for x in t]

any([2>8, 4>2, 1>2])
"""
lst = [1,2,3]* -20