import sys
input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	dp = [0 for _ in range(N+1)]
	dp[0] = 1
	dp[1] = 1
	for i in range(2, N+1):
		dp[i] = dp[i-1] + 2*dp[i-2]
	
	if N % 2 == 1:
		ret = (dp[N] + dp[(N-1)//2])//2
	else:
		ret = (dp[N] + dp[N//2] + dp[(N-2)//2]*2)//2
	
	print(ret)