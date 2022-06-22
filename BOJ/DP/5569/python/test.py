import sys
input = sys.stdin.readline

MOD = 100000
if __name__ == '__main__':
	w, h = map(int, input().split())
	dp = [[[0 for _ in range(4)] for _ in range(w+1)] for _ in range(h+1)]
#0 UpUp, 1 RightRight, 2 UpRight, 3 RightUp
	for i in range(1, h+1):
		dp[i][1][0] =1
	for i in range(1, w+1):
		dp[1][i][1] = 1

	for i in range(2, h+1):
		for j in range(2, w+1):
			dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][3]) % MOD
			dp[i][j][1] = (dp[i][j-1][1] + dp[i][j-1][2]) % MOD
			dp[i][j][2] = dp[i][j-1][0]
			dp[i][j][3] = dp[i-1][j][1]
	
	print(sum(dp[h][w]) % MOD)