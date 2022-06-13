import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	dp = [0 for _ in range(N+3)]

	dp[2] = 2
	for i in range(3, N+1):
		dp[i] = 3*dp[i-1]
	
	print(dp[N])