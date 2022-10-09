class Solution:
    def isValid(self, s: str) -> bool:
        BRACKETS_MAPPING = { '{': '}', '[':']','(':')' }
        open = list()
        for bracket in s:
            if bracket in BRACKETS_MAPPING:
                open.append(BRACKETS_MAPPING[bracket])
            elif not(len(open)) or bracket != open.pop():
                return False
        return not(len(open))

            



classInstance = Solution()
print(classInstance.isValid("()"))
print(classInstance.isValid("()[]{}"))
print(classInstance.isValid("(]"))
print(classInstance.isValid("{[]}"))
print(classInstance.isValid("(])"))
print(classInstance.isValid("]"))