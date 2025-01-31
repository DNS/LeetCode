/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
	x = parseInt(s)
	if (x < -(2**31) ) x = -(2**31)
	if (x > (2**31-1) ) x = (2**31-1)
	
	if (! x) { return 0 }
	
	return x
};