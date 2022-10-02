class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        elif x<10: return True
        return x == int(''.join(list(reversed(list(str(x))))))

classInstance = Solution()
print(classInstance.isPalindrome(121))