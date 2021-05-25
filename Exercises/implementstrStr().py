class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        size_needle = len(needle)
        size_haystack = len(haystack)
        if size_needle == 0:
            return 0
        while i< size_haystack and size_haystack-i+1 >= size_needle:
            if haystack[i] == needle[j]:
                temp = i
                while j < size_needle and i < size_haystack and needle[j] == haystack[i]:
                    i = i + 1
                    j = j + 1
                if j == size_needle:
                    return temp
                i = temp + 1
                j = 0
            else:
                i = i + 1
        return -1