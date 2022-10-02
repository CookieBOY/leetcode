class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        x ={}
        for i in range(len(nums)):
            if(target - nums[i]) in x:
                return(x[target - nums[i]],i)
            else:
                x[nums[i]] = i

classInstance = Solution()
print(classInstance.twoSum(nums=[3,3],target=6))