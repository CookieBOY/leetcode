/**
 * @param {string} s
 * @return {number}
 */
 var romanToInt = function(s) {
    let symbolToValueMap = {
        'I': 1, 'V': 5, 'X': 10, 'L':50,
        'C': 100, 'D': 500, 'M': 1000
    }

    let number = 0
    s = s.split('')
    while(s.length) {
        const currentSymbol = s.shift()
        if(symbolToValueMap[currentSymbol] < symbolToValueMap[s[0]])
            number -= symbolToValueMap[currentSymbol]
        else
            number += symbolToValueMap[currentSymbol]
    }

    return number
};

console.log(romanToInt('MCMXCIV'))