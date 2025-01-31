/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
	if (x < -(2**31) ) return 0
	if (x > (2**31-1) ) return 0
	
	s = x.toString()
	
	a = s.split('').reverse()
	if (a[0] == '0' && a.length>1)
		a.shift()
	
	a = a.join('')
	
	if (a.match('-')) {
		a = a.replace('-', '')
		a = '-' + a
	}
	
	z = parseInt(a)
	if (z < -(2**31) ) return 0
	if (z > (2**31-1) ) return 0
	
	return z
};