import sys
input = sys.stdin.readline

if __name__ == '__main__':
	H, Y = map(int, input().split())
	dp = [0 for _ in range(Y+6)]

	dp[0] = H
	for i in range(1, Y+1):
		dp[i] = max(int(dp[i-1] * 1.05), int(dp[i-3] * 1.2), int(dp[i-5] * 1.35))
	
	print(dp[Y])