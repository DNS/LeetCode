/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
	var value = 0
    for (var i=0; i<s.length; i++) {
		if      (s[i] == 'C' && s[i+1] == 'M') { value += -100+1000; i++ }
		else if (s[i] == 'M') value += 1000
		else if (s[i] == 'C' && s[i+1] == 'D') {value += -100+500; i++ }
		else if (s[i] == 'D') value += 500
		else if (s[i] == 'X' && s[i+1] == 'C') { value += -10+100; i++ }
		else if (s[i] == 'C') value += 100
		else if (s[i] == 'X' && s[i+1] == 'L') {value += -10+50; i++ }
		else if (s[i] == 'L') value += 50
		else if (s[i] == 'I' && s[i+1] == 'X') { value += -1+10; i++ }
		else if (s[i] == 'X') value += 10
		else if (s[i] == 'V') value += 5
		else if (s[i] == 'I' && s[i+1] == 'V') { value += -1+5; i++ }
		else if (s[i] == 'I') value += 1
	}
	
	return value
};