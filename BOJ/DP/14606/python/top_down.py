import sys
input = sys.stdin.readline

def dfs(h):
	if h <= 1:
		return 0
	if dp[h] != -1:
		return dp[h]
	
	dp[h] = 0
	mid = h//2
	dp[h] = max(dp[h], dfs(mid) + dfs(h-mid) + mid*(h-mid))
	
	return dp[h]

if __name__ == "__main__":
	N = int(input())
	dp = [-1 for _ in range(N+1)]

	print(dfs(N))