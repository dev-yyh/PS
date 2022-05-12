import sys
input = sys.stdin.readline

def dfs (a, b, c):
	if a < 0:
		return dfs(0, b, c)
	if b < 0:
		return dfs(a, 0, c)
	if c < 0:
		return dfs(a, b, 0)
	
	if a == 0 and b == 0 and c == 0:
		return 0
	
	if dp[a][b][c] != -1:
		return dp[a][b][c]
	dp[a][b][c] = float('inf')

	dp[a][b][c] = min(dp[a][b][c], dfs(a-9, b-3, c-1)+1)
	dp[a][b][c] = min(dp[a][b][c], dfs(a-9, b-1, c-3)+1)
	dp[a][b][c] = min(dp[a][b][c], dfs(a-3, b-9, c-1)+1)
	dp[a][b][c] = min(dp[a][b][c], dfs(a-3, b-1, c-9)+1)
	dp[a][b][c] = min(dp[a][b][c], dfs(a-1, b-9, c-3)+1)
	dp[a][b][c] = min(dp[a][b][c], dfs(a-1, b-3, c-9)+1)

	return dp[a][b][c]

if __name__ == "__main__":
	N = int(input())
	scv = list(map(int, input().split()))
	while len(scv) < 3:
		scv.append(0)

	h1, h2, h3 = scv	
	dp = [[[-1 for _ in range(h3+1)] for _ in range(h2+1)] for _ in range(h1+1)]

	print(dfs(h1, h2, h3))
