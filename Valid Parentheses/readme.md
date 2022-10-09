Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

<strong>Example 1:</strong>
<pre>
<strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

<strong>Example 2:</strong>
<pre>
<strong>Input: s = "()[]{}"</strong>
<strong>Output: true</strong>
</pre>

<strong>Example 3:</strong>
<pre>
<strong>Input: s = "(]"</strong>
<strong>Output: false</strong>
</pre> 

<strong>Constraints:</strong>
<ol>
    <li>1 <= s.length <= 104</li>
    <li>s consists of parentheses only '()[]{}'.</li>
</ol>