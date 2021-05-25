string = ["roy"]
repeat = [3]
res = [''.join(sub * ele1 for sub in ele2) for ele1 in repeat for ele2 in string]
print(res)