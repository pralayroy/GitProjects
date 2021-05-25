class Solution:
    def __init__(self, data, target):
        self.data = data
        self.target = target

    def twoSum(self, data, target):
        dict_l = {}
        size = len(data)
        for i, num in enumerate(data):
            test = target - num
            if test not in dict_l:
                dict_l[num] = i
            else:
                return [dict_l[test], i]


#data1 = [2,7,11,15]
#targer1 = 9
S = Solution([2,7,11,15,13], 28)
print(S.twoSum([2,7,11,15,13], 28))
