import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	dp = [0 for _ in range(N+3)]
	dp[1] = 0
	dp[2] = 1
	for i in range(3, N+1):
		mid = i//2
		dp[i] = max(dp[i], (i-mid)*mid + dp[i-mid] + dp[mid])

	print(dp[N])