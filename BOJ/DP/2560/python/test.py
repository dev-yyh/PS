import sys
input = sys.stdin.readline

MOD = 1000
if __name__ == '__main__':
	a, b, d, N = map(int, input().split())
	dp = [0 for _ in range(N + d + 1)]

	dp[0] = 1
	for i in range(1, N+1):
		dp[i] = (dp[i-1] + dp[i-a] - dp[i-b] + MOD) % MOD

	if N-d >= 0:	
		print((dp[N]-dp[N-d])%MOD)
	else:
		print(dp[N]%MOD)