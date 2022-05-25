import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(c):
	if c <= 0:
		return 0

	if dp[c] != -1:
		return dp[c]
	
	dp[c] = float('inf')
	for cost, customer in L:
		dp[c] = min(dp[c], solve(c-customer) + cost)

	return dp[c]

if __name__ == '__main__':
	C ,N = map(int, input().split())
	L = [list(map(int, input().split())) for _ in range(N)]
	dp = [-1 for _ in range(C+1)]

	print(solve(C))