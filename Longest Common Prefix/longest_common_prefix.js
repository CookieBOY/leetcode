/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
    let commonPrefix = ''
    for(let i = 0; i<strs[0].length; i++) {
        for(let word of strs) {
            if(word[i] !== strs[0][i])
                return commonPrefix
        }   
        commonPrefix += strs[0][i]            
    }
    return commonPrefix
};

console.log(longestCommonPrefix(["dog","racecar","car"]))
console.log(longestCommonPrefix(["flower","flow","flight"]))