
class Solution:
	def longestValidParentheses (self, s: str) -> int:
		self.s = s
		self.solve()
		
		return self.count()
		

	def count (self):
		count = 0
		largest = []
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
		for i in largest:
			if val_max < i:
				val_max = i
		
		#print(self.s)
		print(val_max)
		return val_max
		
		
	def solve (self):
		if len(self.s):
			return
		
		i = 0
		while i < len(self.s) - 1 :
			# find () pattern
			if self.s[i:i+2] == '()':
				self.s = substr_replace(self.s, '..', i, i+2)
				i = 0
				#self.count += 2
				#print('a')
			
			else:
				i += 1
		
		i = 0
		while i < len(self.s) :
			# find (...) pattern
			if self.s[i:i+1] == '(':
				j = i + 1
				#print('b ' + str(i))
				while j < len(self.s) :
					#print('c')
					#print( f"{j} " + self.s[j:j+1] )
					if self.s[j:j+1] == '.':
						print('d ' + str(j) + ' ' + self.s)
						
						j += 1
						if j >= len(self.s):
							i = len(self.s)
							break
						#break
					elif self.s[j:j+1] == ')' :
						self.s = substr_replace(self.s, '.', i, i+1)
						self.s = substr_replace(self.s, '.', j, j+1)
						i = 0
						#print('e')
						break
					elif self.s[j:j+1] == '(' :
						i += 1
						j += 1
						
						print('f: ' + str(j))
						if j >= len(self.s):
							i = len(self.s)
							break
						break
					#print('z')
			else:
				i += 1
		

# substr_replace(self.s, '..', i, i+2)
def substr_replace (string_input: str, string_replace: str, start: int, end: int) -> str:
	return string_input[:start] + string_replace + string_input[end:]

#text = '('
text = '(()'
#text = '(()((('
#text = '())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))('
#text = '()(())'
s = Solution()
s.longestValidParentheses(text)
#print( s.count )
print( s.s )

#())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))(
#())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))(
#..)............................)))........)....)........)........)......)..........)))(
#..)............................)))........)....)........)........)......)..........)))(


