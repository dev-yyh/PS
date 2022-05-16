import sys
input = sys.stdin.readline

def solve(start, end):
	if start == end:
		return 0
	
	if dp[start][end] != -1:
		return dp[start][end]
	
	dp[start][end] = float('inf')
	for i in range(start, end):
		dp[start][end] = min(dp[start][end], solve(start, i) + solve(i+1, end) + (lamp[i] != lamp[end]))
	return dp[start][end]

if __name__ == '__main__':
	N, K = map(int, input().split())
	lamp = [0] + list(map(int, input().split()))
	dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
	
	print(solve(1, N))