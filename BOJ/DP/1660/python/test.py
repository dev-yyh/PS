import sys
input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	s = 0
	i = 1
	arr = []
	while s <= N:
		s += i*(i+1)//2
		arr.append(s)
		i += 1
	
	dp = [float('inf') for _ in range(N+1)]
	dp[0] = 0
	for a in arr:
		for i in range(a, N+1):
			dp[i] = min(dp[i], dp[i-a]+1)
	
	print(dp[N])


