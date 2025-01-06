/**
 * @param {string} s
 * @return {number}
 */


/*
 * The algorithm for myAtoi(string s) is as follows:

 * Whitespace: Ignore any leading whitespace (" ").
 * Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
 * Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
 * Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
 */

var myAtoi = function(s) {
    let pos = true;
    let num = "";
    let digits = true;
    let digit_prev_detect = false;
    let pos_prev_detect = false;

    for (let i=0; i<s.length; i++){
        if (!digits) {
            break;
        }
        switch (s[i]){
            case " ":
                if (digit_prev_detect || pos_prev_detect){
                    digits = false;
                    break;
                }
                break;
            case "-":
                if (digit_prev_detect || pos_prev_detect){
                    digits = false;
                    break;
                }
                pos = false;
                pos_prev_detect = true
                break;
            case "+":
                if (digit_prev_detect || pos_prev_detect){
                    digits = false;
                    break;
                }
                pos_prev_detect = true
                break;
            default:
                if (s[i] >= "0" && s[i] <= "9"){
                    digit_prev_detect = true;
                    num += s[i];
                } else {
                    digits = false;
                    break;
                }
        }
    }

    let retnum = pos ? parseInt(num) : -1 * parseInt(num);
    if (retnum < -2147483648){
        retnum = -2147483648;
    } else if (retnum > 2147483647){
        retnum = 2147483647
    }

    return retnum ? retnum : 0;
};

console.log(myAtoi("   +0 123"));
