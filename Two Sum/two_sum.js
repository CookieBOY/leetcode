import { arr } from './array'

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    let numHash = {}
    // while loop
    console.time('loop')
    let i = 0
    while(true) {
        const currentNumber = nums.shift()
        if(numHash[target - currentNumber] !== undefined) {
            console.timeEnd('loop')
            return [numHash[target - currentNumber], i]
        }
        else {
            numHash[currentNumber] = i
            i++
        }
    }
}

console.log(twoSum(arr, 19999))