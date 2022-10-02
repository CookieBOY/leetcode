Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, <code>121</code> is a palindrome while <code>123</code> is not.
 

<b>Example 1:</b>
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```
<b>Example 2:</b>
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
<b>Example 3:</b>
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 ```

<b>Constraints:</b>
<ul>
    <li>
        <code>
            -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1
        </code>
    </li>
</ul>

</b>Follow up:</b> Could you solve it without converting the integer to a string?