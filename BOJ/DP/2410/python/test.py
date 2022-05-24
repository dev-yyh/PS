import sys
input = sys.stdin.readline

MOD = 1000000000
if __name__ == '__main__':
	N = int(input())
	nums = [2**i for i in range(21)]
	dp = [0 for _ in range(N+1)]

	dp[0] = 1
	k = 0
	for num in nums:
		if num > N: continue
		for i in range(num, N+1):
				dp[i] = (dp[i] + dp[i-num]) % MOD

	print(dp[N])