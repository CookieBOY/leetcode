from copyreg import constructor
from sys import prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:     
        commonPrefix = min(strs, key=len)
        for word in strs: 
            prefix = str('')
            for firstWordChar, secondWordChar in zip(word, commonPrefix):
                if firstWordChar == secondWordChar: 
                    prefix += firstWordChar
                else:
                    commonPrefix = prefix
                    break        
            commonPrefix = prefix
        return commonPrefix

classInstance = Solution()
# print(classInstance.longestCommonPrefix(["dog","racecar","car"]))
# print(classInstance.longestCommonPrefix(["flower","flow","flight"]))
print(classInstance.longestCommonPrefix(["ab", "a"]))
# print(classInstance.longestCommonPrefix(["cir","car"]))