class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for char in s:
            if char in open_par:
                stack.append(char)
            elif stack and char == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


"""    
obj = Solution()
print(obj.isValid('({[)]'))
"""