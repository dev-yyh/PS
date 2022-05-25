import sys
input = sys.stdin.readline

if __name__ == '__main__':
	C ,N = map(int, input().split())
	L = [list(map(int, input().split())) for _ in range(N)]
	dp = [float('inf') for _ in range(C+1)]

	dp[0] = 0
	for i in range(1, C+1):
		for cost, customer in L:
			if i-customer < 0:
				dp[i] = min(dp[i], dp[0] + cost)
			else:
				dp[i] = min(dp[i], dp[i-customer] + cost)
	
	print(dp[C])