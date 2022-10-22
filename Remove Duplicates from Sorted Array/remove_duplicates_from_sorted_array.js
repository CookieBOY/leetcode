/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
  for(n=1; n<nums.length; n++) {
      console.log(nums)
      if(nums[n] === nums[n-1]) {
        nums.splice(n,1)
        n = n - 1
      }       
  }
};

console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,3,4]))
console.log(removeDuplicates([1,1,2]))