import sys
input = sys.stdin.readline

MOD = 987654321
if __name__ == "__main__":
	N = int(input())
	dp = [0 for _ in range(N+1)]
	dp[0] = 1

	for i in range(2, N+1, 2):
		for j in range(0, i, 2):
			dp[i] = (dp[i] + dp[j] * dp[i-j-2]) % MOD
		
	print(dp[N])