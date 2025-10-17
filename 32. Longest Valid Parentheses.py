
class Solution:
	def longestValidParentheses (self, s: str) -> int:
		self.count = 0
		self.a = 0
		self.s = s
		self.solve()
		return self.count
		

	def solve (self):
		while self.a < len(self.s)-1 :
			if self.s[self.a:self.a+2] == '()':
				self.s = self.s[0:self.a] + self.s[self.a+2:len(self.s)]
				self.count += 2
				self.a = 0
			else:
				self.a += 1

text = '())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))('
s = Solution()
s.longestValidParentheses(text)
print( s.count )

