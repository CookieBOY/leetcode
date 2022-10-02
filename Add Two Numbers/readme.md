You are given two <b>non-empty</b> linked lists representing two non-negative integers. The digits are stored in <b>reverse order</b>, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

<b>Example 1:</b>
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```
<b>Example 2:</b>
```
Input: l1 = [0], l2 = [0]
Output: [0]
```
<b>Example 3:</b>
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```
<b>Constraints:</b>
<ul>
    <li>The number of nodes in each linked list is in the range [1, 100].</li>
    <li>0 <= Node.val <= 9</li>
    <li>It is guaranteed that the list represents a number that does not have leading zeros.</li>