import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(a_idx, b_idx):
	if len(c) == a_idx + b_idx:
		return 1

	if dp[a_idx][b_idx] != -1:
		return dp[a_idx][b_idx]

	dp[a_idx][b_idx] = 0
	if len(a) > a_idx and a[a_idx] == c[a_idx+b_idx]:
		dp[a_idx][b_idx] = solve(a_idx+1, b_idx) 
	
	if len(b) > b_idx and b[b_idx] == c[a_idx+b_idx]:
		dp[a_idx][b_idx] = max(dp[a_idx][b_idx], solve(a_idx, b_idx+1))
	
	return dp[a_idx][b_idx]

if __name__ == '__main__':
	N = int(input())
	for i in range(1, N+1):
		a, b, c = input().split()
		dp = [[-1 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
		ret = solve(0, 0)
		if ret:
			print(f'Data set {i}: yes')
		else:
			print(f'Data set {i}: no')