# (문자열 길이 - 최장길이 팰린드롬)으로 구하는 방법
import sys
input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	nums = list(map(int, input().split()))
	dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

	for i  in range(1, N+1):
		for j in range(1, N+1):
			if nums[-i] == nums[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	
	print(N - dp[N][N])