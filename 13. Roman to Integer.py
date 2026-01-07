class Solution:
	def romanToInt(self, s: str) -> int:
		answer :int = 0
		number :int = 0
		previous :int = 0
		
		roman :dict = {
			'I': 1,
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500,
			'M': 1000,
		}
		
		print(roman['M'])
		
		for i in range(len(s), 0, -1):
			c = s[i-1]
			number = roman[c]
			
			if number < previous:
				answer -= number
			else:
				answer += number
			
			previous = number
			
		return answer


