class Solution:
    def removeElement(self, nums, val):
        count = 0
        size = len(nums)
        for i in range(size):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count + 1
        return count

obj = Solution()
list = [1,2,3,4]
val = 2
print(obj.removeElement(list, val))