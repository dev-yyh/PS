import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N, T = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]
	dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

	for i in range(1, N+1):
		K, S = arr[i-1]
		for j in range(T+1):
			if j < K:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-K] + S)
	
	print(dp[N][T])