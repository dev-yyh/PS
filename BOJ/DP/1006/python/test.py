import sys

input = sys.stdin.readline
def solve():
	for i in range(2, N+1):
		outer = 1 if e[0][i-1] + e[0][i] <= W else 2
		inner = 1 if e[1][i-1] + e[1][i] <= W else 2
		both = 1 if e[0][i] + e[1][i] <= W else 2
		dp[0][i] = min(dp[1][i-1] + outer, dp[2][i-1] + 1)
		dp[1][i] = min(dp[0][i-1] + inner, dp[2][i-1] + 1)
		dp[2][i] = min(dp[2][i-1] + both,dp[2][i-2] + inner + outer, dp[0][i] + 1, dp[1][i] + 1)
	return 
if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		N, W = map(int, input().split())
		e = [[0]+list(map(int, input().split())) for _ in range(2)]
		dp = [[0 for _ in range(10000+1)] for _ in range(3)]
		ans = float('inf')
		#0 inner ,1 outer, 2 both
		dp[0][1] = dp[1][1] = 1
		dp[2][1] = 1 if e[0][1] + e[1][1] <= W else 2
		solve()
		ans = min(ans, dp[2][N])
		if e[0][N] + e[0][1] <= W:
			dp = [[0 for _ in range(10000+1)] for _ in range(3)]
			dp[0][1] = 1
			dp[1][1] = float('inf')
			dp[2][0] = float('inf')
			dp[2][1] = 2
			solve()
			ans = min(ans, dp[1][N])
		if e[1][N] + e[1][1] <= W:
			dp = [[0 for _ in range(10000+1)] for _ in range(3)]
			dp[0][1] = float('inf')
			dp[1][1] = 1
			dp[2][0] = float('inf')
			dp[2][1] = 2
			solve()
			ans = min(ans, dp[0][N])
		if e[0][N] + e[0][1] <= W and e[1][N] + e[1][1] <= W:
			dp = [[0 for _ in range(10000+1)] for _ in range(3)]
			dp[0][1] = float('inf')
			dp[1][1] = float('inf')
			dp[2][0] = float('inf')
			dp[2][1] = 2
			solve()
			ans = min(ans, dp[2][N-1])

		print(ans)

