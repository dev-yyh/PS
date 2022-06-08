import sys
input = sys.stdin.readline

def dfs(l, r):
	if l >= r:
		return 0
	
	if dp[l][r] != -1:
		return dp[l][r]
	
	dp[l][r] = 0
	if (DNA[l] == 'a' and DNA[r] =='t') or (DNA[l] == 'g' and DNA[r] == 'c'):
		dp[l][r] = dfs(l+1, r-1) + 2
	
	for m in range(l, r):
		dp[l][r] = max(dp[l][r], dfs(l, m)+ dfs(m+1, r))
	
	return dp[l][r]

if __name__ == "__main__":
	DNA = input().rstrip()
	size = len(DNA)
	dp = [[-1 for _ in range(size)] for _ in range(size)]

	print(dfs(0, size-1))