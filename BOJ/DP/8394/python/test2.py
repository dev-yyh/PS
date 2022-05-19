# 메모리 초과 발생 256MB 초과
import sys
input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	dp = [[0 for _ in range(2)] for _ in range(n+1)]
	dp[1][0] = 1
	dp[1][1] = 0
	for i in range(2, n+1):
		dp[i][0] = (dp[i-1][0] + dp[i-1][1])%10
		dp[i][1] = (dp[i-1][0])%10

	print((dp[n][0] + dp[n][1])%10)