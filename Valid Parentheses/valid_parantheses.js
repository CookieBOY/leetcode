/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    const BRACKETS_MAPPING = { '{': '}', '[':']','(':')' }
    s = s.split('')
    let open = []
    while(s.length) {
        if(s[0] in BRACKETS_MAPPING)
            open.push(BRACKETS_MAPPING[s[0]])
        else if(s[0] !== open.pop())
            return false
        s.shift()
    }
    return !open.length
};

console.log(isValid("()"))
console.log(isValid("()[]{}"))
console.log(isValid("(]"))
console.log(isValid("{[]}"))
console.log(isValid("(])"))