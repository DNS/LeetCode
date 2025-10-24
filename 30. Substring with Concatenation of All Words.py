

class Solution:
	def findSubstring(self, s: str, words: list[str]) -> list[int]:
		# Basic checks
		if not s or not words:
			return []

		word_len = len(words[0])
		words_cnt = len(words)
		total_len = word_len * words_cnt

		# Build a frequency map of the words we need
		need = {}
		for w in words:
			need[w] = need.get(w, 0) + 1

		result = []

		# We slide a window of size *total_len* but we start the scan
		# at every possible offset inside a word (0 … word_len‑1).
		# This avoids generating every permutation.
		for offset in range(word_len):
			left = offset               # start of the current window
			matched = 0                 # how many words are matched so far
			have = {}                   # frequency of words inside the window

			# Walk through the string in steps of *word_len*
			for right in range(offset, len(s) - word_len + 1, word_len):
				cur_word = s[right:right + word_len]

				# If the word is not part of *words*, reset the window
				if cur_word not in need:
					have.clear()
					matched = 0
					left = right + word_len
					continue

				# Add current word to the window count
				have[cur_word] = have.get(cur_word, 0) + 1
				matched += 1

				# If we have more copies of *cur_word* than needed,
				# shrink the window from the left until it is valid again
				while have[cur_word] > need[cur_word]:
					left_word = s[left:left + word_len]
					have[left_word] -= 1
					matched -= 1
					left += word_len

				# When the window size equals the total length,
				# we found a valid start index
				if matched == words_cnt:
					result.append(left)

		# Remove possible duplicates (kept for compatibility with original code)
		return sorted(set(result))


# -------------------------------------------------------------------------

# Example usage with the huge test case from the original script
if __name__ == "__main__":
	text = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
	words = ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]

	sol = Solution()
	print(sol.findSubstring(text, words))


'''
fastest way !

text = 'aaabbbcccdddeee'
words = ['bbb','ccc']

#1 first find substring 'bbb' then 'ccc', 
#2 if found then what is the next word in that text (also remove the found from temporary words), if the next word not found repeat to #1

aaa[bbb][ccc]dddeee
     1    2         (ok)

aaabbb[ccc][ddd]eee
        1    X      (skip)

'''


'''

BEST WAY, using regex to find index!
$text = 'aaabbbcccdddeee'
$words = @('bbb','ccc')
# find and return substring index
$words | %{ [Regex]::Match($text, $_) }
# find substring range 3 to 6
$([Regex]::Match($text, '^(.{3,6})')).Value

'''




