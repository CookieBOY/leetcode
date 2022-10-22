class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nonDuplicateIndex = 0
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            else:
                nums[nonDuplicateIndex] = nums[i]
                nonDuplicateIndex += 1
        return nonDuplicateIndex


classInstance = Solution()
print(classInstance.removeDuplicates([0,0,1,1,1,2,2,3,3,3,4]))
print(classInstance.removeDuplicates([1,1,2]))