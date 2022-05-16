import sys
input = sys.stdin.readline

if __name__ == '__main__':
	N, K = map(int, input().split())
	lamp = [0] + list(map(int, input().split()))
	dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
	
	for length in range(1, N):
		for start in range(1, N - length + 1):
			end = start + length
			dp[start][end] = float('inf')
			for i in range(start, end):
				dp[start][end] = min(dp[start][end], dp[start][i] + dp[i+1][end] + (lamp[start] != lamp[end]))
	
	print(dp[1][N])