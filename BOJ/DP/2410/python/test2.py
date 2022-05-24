import sys
input = sys.stdin.readline

MOD = 1000000000
if __name__ == '__main__':
	N = int(input())
	dp = [0 for _ in range(N+1)]

	dp[0] = 1
	k = 0
	j = (1 << k)
	while j <= N:
		for i in range(1, N+1):
			if i >= j:
				dp[i] = (dp[i] + dp[i-j]) % MOD
		k += 1
		j = (1 << k)

	print(dp[N])