Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have <b>exactly one solution</b>, and you may not use the same element twice.

You can return the answer in any order.

<b>Example 1:</b>
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

<b>Example 2:</b>
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

<b>Example 3:</b>
```
Input: nums = [3,3], target = 6
Output: [0,1]
``` 

<b>Constraints:</b>
<ul>
    <li>2 <= nums.length <= 104 </li>
    <li>-109 <= nums[i] <= 109</li>
    <li>-109 <= target <= 109</li>
    <li><b>Only one valid answer exists.</b></li>
</ul>