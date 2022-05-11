import sys
input = sys.stdin.readline

if __name__ == "__main__":
	T = int(input())
	
	dp = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(101)]

	dp[1][0][1] = 1
	dp[1][0][0] = 1
	
	for i in range(2, 101):
		for j in range(i):
			if i == 0:
				dp[i][j][1] += dp[i-1][j][0]
			else:
				dp[i][j][1] += dp[i-1][j][0] + dp[i-1][j-1][1]
			dp[i][j][0] += dp[i-1][j][0] + dp[i-1][j][1]
	
	for _ in range(T):
		n, k = map(int, input().split())
		print(dp[n][k][0] + dp[n][k][1])
