// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21
 

// Constraints:

// -231 <= x <= 231 - 1

function reverse(x: number) {
    if(x === 0 ) {
        return x
    }
    let isNeg = false
    if(x < 0) {
        isNeg = true
    }
    const newS = x.toString().replace(new RegExp(/0*$/), '');
    let reverse = '';
    for(let i = newS.length - 1 ; i >= 0; i--){
        reverse += newS[i];
    }
    if(isNeg) {
        reverse = reverse.replace('-','')
        reverse = '-'+reverse
    }
    const result = Number(reverse);
    if((result > Math.pow(2, 31) - 1) || (result < -Math.pow(2, 31)) ) return 0 
    else return result;
}
