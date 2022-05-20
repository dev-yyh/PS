import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve(start, end):
	if start >= end:
		return 0

	if dp[start][end] != -1:
		return dp[start][end]

	dp[start][end] = float('inf')
	if nums[start] == nums[end]:
		dp[start][end] = solve(start+1, end-1)
	else:
		dp[start][end] = min(solve(start+1, end), solve(start, end-1)) + 1
	
	return dp[start][end]

if __name__ == '__main__':
	N = int(input())
	nums = list(map(int, input().split()))
	dp = [[-1 for _ in range(N)] for _ in range(N)]
	
	print(solve(0, N-1))