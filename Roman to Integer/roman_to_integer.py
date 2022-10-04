class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToValueMap = {
        'I': 1, 'V': 5, 'X': 10, 'L':50,
        'C': 100, 'D': 500, 'M': 1000
        }
        
        number = 0
        for index, _val in enumerate(s):
            if (index + 1 < len(s)) and (symbolToValueMap[s[index]] < symbolToValueMap[s[index + 1]]):
                number -= symbolToValueMap[s[index]]
            else: 
                number += symbolToValueMap[s[index]]
        return number


classInstance = Solution()
print(classInstance.romanToInt('MCMXCIV'))