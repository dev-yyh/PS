import sys
input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	nums = list(map(int, input().split()))
	dp = [[0 for _ in range(N)] for _ in range(N)]

	for length  in range(1, N):
		for start in range(N-length):
			end = start + length
			if nums[start] == nums[end]:
				dp[start][end] = dp[start+1][end-1]
			else:
				dp[start][end] = min(dp[start+1][end], dp[start][end-1]) + 1
	
	print(dp[0][N-1])