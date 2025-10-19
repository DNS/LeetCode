import re

class Solution:
	def longestValidParentheses (self, s: str) -> int:
		print(s)
		b = s
		c = re.sub(r'\(\)', '..', b)
		while True:
			b = c
			c = re.sub(r'\((\.+?)\)', r'.\1.', b)
			if c == b:
				break
		print(c)
		self.s = c
		return self.count()

	
	def count (self):
		count = 0
		largest = [0]
		for i in range(len(self.s)):
			if self.s[i] == '.':
				count += 1
				if i >= len(self.s) - 1:
					largest.append(count)
			else:
				largest.append(count)
				count = 0
			#print(i)
		
		
		
		val_max = 0
		#for i in largest:
		#	if val_max < i:
		#		val_max = i
		
		val_max = max(largest)
		
		#print(self.s)
		print(val_max)
		return val_max


#t = '())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))('
t = ')(((((()())()()))()(()))('
s = Solution()
s.longestValidParentheses(t)
'''
)(((((()())()()))()(()))(
)(......................(	ok


)(((((....)....))..(..))(
)....(..................(	wrong
).((((.........))......)(
'''
	
