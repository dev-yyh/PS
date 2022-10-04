import sys
input = sys.stdin.readline
MOD = 10007
MAX = 52
if __name__ == '__main__':
	N = int(input())
	dp = [[0] * (MAX+1) for _ in range(MAX+1)]

	for i in range(MAX+1):
		dp[i][0] = 1
		for j in range(1, MAX+1):
			dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
	
	ans = 0
	for i in range(1, N+1):
		if N-4*i < 0:
			break
		if i % 2:
			ans = (ans + dp[13][i] * dp[52-4*i][N-4*i]) % MOD
		else:
			ans = (ans - (dp[13][i] * dp[52-4*i][N-4*i]) % MOD + MOD) % MOD
	
	print(ans)
	