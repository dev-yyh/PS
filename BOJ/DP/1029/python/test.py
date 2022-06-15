import sys
input = sys.stdin.readline

def dfs(cur, price, mask):
	if mask == (1<<N)-1:
		return 0
	if dp[cur][price][mask] != -1:
		return dp[cur][price][mask]
	
	dp[cur][price][mask] = 0
	for next in range(N):
		if mask & (1<<next):
			continue
		if price <= arr[cur][next]:
			dp[cur][price][mask] = max(dp[cur][price][mask], dfs(next, arr[cur][next], mask|(1<<next)) + 1)
	return dp[cur][price][mask]

if __name__ == "__main__":
	N = int(input())
	arr = [list(map(int, input().rstrip())) for _ in range(N)]
	dp = [[[-1 for _ in range(1<<N)] for _ in range(10)] for _ in range(N)]

	print(dfs(0, 0, 1<<0)+1)
