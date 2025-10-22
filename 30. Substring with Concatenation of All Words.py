from typing import *


class Solution:
	def __init__ (self):
		self.retval = []
		self.words = []
		
	def findSubstring (self, s: str, words: List[str]) -> List[int]:
		self.s = s
		
		
		self.words = words
		
		
		self.permute(self.words, 0, len(self.words) - 1 )
		
		# remove duplicates
		seen = set()
		self.retval = [x for x in self.retval if not (x in seen or seen.add(x))]
		return self.retval

	def swap (self, arr, a, b) :
		arr[a], arr[b] = arr[b], arr[a]

	def permute (self, arr, left, right) :
		#print(arr)
		if left == right:
			joined = ''.join(arr)
			#print(joined)
			self.findIndex(joined)
		else:
			for i in range(left, right + 1) :
				self.swap(arr, left, i)
				self.permute(arr, left + 1, right)
				self.swap(arr, left, i)  # backtrack
	
	
	def findIndex (self, joined) :
		joined_length = len(joined)
		for i in range(len(self.s)-joined_length+1) :
			#print(self.s[i:i+joined_length])
			if self.s[i:i+joined_length] == joined:
				#print(i)
				self.retval.append(i)
				
		




if __name__ == "__main__":
	#arr = [1, 2, 3]
	#n = len(arr)
	#permute(arr, 0, n - 1)
	
	#text = "wordgoodgoodgoodbestword"
	#words = ["word","good","best","word"]
	
	#text = "barfoothefoobarman"
	#words = ["foo","bar"]
	
	#text = "barfoofoobarthefoobarman"
	#words = ["bar","foo","the"]
	
	#text = "wordgoodgoodgoodbestword"
	#words = ["word","good","best","good"]
	
	text = "fffffffffffffffffffffffffffffffff"
	words = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]
	
	s = Solution()
	s.findSubstring(text, words)
	print(s.retval)

