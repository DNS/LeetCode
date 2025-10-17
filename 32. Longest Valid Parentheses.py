
class Solution:
	def longestValidParentheses (self, s: str) -> int:
		self.count = 0
		i = 0
		self.s = s
		self.solve()
		return self.count
		

	def solve (self):
		i = 0
		while i < len(self.s)-1 :
			# find () pattern
			if self.s[i:i+2] == '()':
				self.s = substr_replace(self.s, '..', i, i+2)
				i = 0
				#self.count += 2
				#print('a')
			
			else:
				i += 1
		
		i = 0
		while i < len(self.s)-1 :
			# find (...) pattern
			if self.s[i:i+1] == '(':
				j = i + 1
				print('b')
				while j < len(self.s)-1 :
					#print('c')
					if self.s[j:j+1] == '.':
						print('d')
						j += 1
					elif self.s[j:j+1] == ')' :
						self.s = substr_replace(self.s, '.', i, i+1)
						self.s = substr_replace(self.s, '.', j, j+1)
						i = 0
						print('e')
						break
					elif self.s[j:j+1] == '(' :
						#i = 0
						print('f: ' + str(j))
						break
					#print('z')
			else:
				i += 1
		

# substr_replace(self.s, '..', i, i+2)
def substr_replace (string_input: str, string_replace: str, start: int, end: int) -> str:
	return string_input[:start] + string_replace + string_input[end:]




text = '())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))('
s = Solution()
s.longestValidParentheses(text)
print( s.count )
print( s.s )

#())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))(
#())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))(
#..)....((......))..............)))(..(..)))....)........)(((..))))......)..........)))(

