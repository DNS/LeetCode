from typing import *


class Solution:
	def __init__ (self):
		self.retval = []
		self.words = []
		self.joined = ''
		self.s_len = 0
		self.words_len = 0
		self.joined_length = 0
	
	def findSubstring (self, s: str, words: List[str]) -> List[int]:
		self.s = s
		self.s_len = len(s)
		self.words = words
		self.words_len = len(self.words)
		self.joined_length = len(''.join(words))
		
		self.permute(self.words, 0, self.words_len )
		
		# remove duplicates
		seen = set()
		self.retval = [x for x in self.retval if not (x in seen or seen.add(x))]
		return self.retval
	
	def swap (self, arr, a, b) :
		arr[a], arr[b] = arr[b], arr[a]
	
	def permute (self, arr, left, right) :
		j = ''.join(arr)
		if j == self.joined:
			return
			
		if left == (right-1):
			self.joined = ''.join(arr)
			self.findIndex()
		else:
			for i in range(left, right) :
				self.swap(arr, left, i)
				self.permute(arr, left + 1, right)
				self.swap(arr, left, i)		# backtrack
	
	
	def findIndex (self) :
		for i in range(self.s_len-self.joined_length+1) :
			#print(self.s[i:i+self.joined_length], i+self.joined_length)
			if self.s[i:i+self.joined_length] == self.joined:
				print(i)
				self.retval.append(i)
	




if __name__ == "__main__":
	#arr = [1, 2, 3]
	#n = len(arr)
	#permute(arr, 0, n - 1)
	
	# []
	#text = "wordgoodgoodgoodbestword"
	#words = ["word","good","best","word"]
	
	# [9, 0]
	#text = "barfoothefoobarman"
	#words = ["foo","bar"]
	
	# [9, 6, 12]
	#text = "barfoofoobarthefoobarman"
	#words = ["bar","foo","the"]
	
	# [8]
	#text = "wordgoodgoodgoodbestword"
	#words = ["word","good","best","good"]
	
	# []
	#text = "fffffffffffffffffffffffffffffffff"
	#words = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]
	
	# [935]
	text = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
	words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
	
	s = Solution()
	s.findSubstring(text, words)
	print(s.retval)

# permutation too slow !

