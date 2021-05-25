class Solution:
    def removeDuplicates(self, nums):
        result = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[result] = nums[i]
                result += 1
        return result


s = Solution()
nums = [1, 3, 3, 5, 5]
print(s.removeDuplicates(nums))
