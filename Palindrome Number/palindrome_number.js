/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    if(x<0) return false
    else if(x<10) return true
    return x === parseInt(x.toString().split('').reverse().join(''), 10)
};

console.log(isPalindrome(121))