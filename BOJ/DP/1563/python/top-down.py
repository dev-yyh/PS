import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

MOD = 1000000
def dfs(n, l, a):
	if l >= 2 or a >= 3:
		return 0
	if n == N:
		return 1
	
	if dp[n][l][a] != -1:
		return dp[n][l][a]
	
	dp[n][l][a] = dfs(n+1, l+1, 0) + dfs(n+1, l, a+1) + dfs(n+1, l, 0)

	return dp[n][l][a] % MOD

if __name__ == "__main__":
	N = int(input())
	dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N)]
	print(dfs(0, 0, 0))