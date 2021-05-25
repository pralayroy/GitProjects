class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        d = {}
        result = 0
        while j < len(s):
            if s[j] not in d or i > d[s[j]]:
                result = max(result, (j - i + 1))
                d[s[j]] = j
            else:
                i = d[s[j]] + 1
                result = max(result, (j - i + 1))
                j -= 1
            j += 1
        return result


obj = Solution()
print(obj.lengthOfLongestSubstring("abcbacbb"))