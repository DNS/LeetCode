

def func1 (s:str, p:str) -> bool:
	# string length
	sl = len(s)
	pl = len(p)
	
	# fill with false, except 0,0 for empty match '' return true
	dp = [[False for _ in range(pl+1)] for _ in range(sl+1)]
	dp[0][0] = True

	#print(dp)
	for j in range(1, pl+1):
		if p[j-1] == '*':
			dp[0][j] = dp[0][j-1]
	
	for i in range(1, sl+1):
		for j in range(1, pl+1):
			if p[j-1] == '*':
				dp[i][j] = dp[i][j-1] or dp[i-1][j]
			elif p[j-1] == '?' or s[i-1] == p[j-1]:
				dp[i][j] = dp[i - 1][j - 1]

	#for i in range(1, sl+1):
		
		
		
	return dp[sl][pl]
	
	

b = func1('aa', 'a')
b = func1('aa', '*')
b = func1('cb', '?a')


print(b)







