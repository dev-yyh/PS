import sys
input = sys.stdin.readline

# OOOO (0), OOXX (1), OXXO (2), XOOX (3), XXOO (4)
def solve(n):
	dp = [[0 for _ in range(6)] for _ in range(n+2)]

	dp[0][0] = 1
	dp[1][0] = 1
	dp[1][1] = 1
	dp[1][3] = 1
	dp[1][4] = 1
	for i in range(2, n+1):
		dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]
		dp[i][1] = dp[i-1][0] + dp[i-1][4]
		dp[i][2] = dp[i-1][3] 
		dp[i][3] = dp[i-1][0] + dp[i-1][2]
		dp[i][4] = dp[i-1][0] + dp[i-1][1]
	
	return dp[n][0]

if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		N = int(input())
		print(solve(N))
