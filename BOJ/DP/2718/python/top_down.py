import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
# OOOO (0), OOXX (1), OXXO (2), XOOX (3), XXOO (4)
def solve(n, state):
	if n < 0:
		return 0
	if n == 0:
		if state == 0:
			return 1
		return 0

	if dp[n][state] != -1:
		return dp[n][state]
	
	dp[n][state] = 0
	if state == 0:
		dp[n][state] = solve(n-2, 0) + solve(n-1, 0) + solve(n-1, 1) + solve(n-1, 3) + solve(n-1, 4)
	elif state == 1:
		dp[n][state] = solve(n-1, 0) + solve(n-1, 4)
	elif state == 2:
		dp[n][state] = solve(n-1, 3)
	elif state == 3:
		dp[n][state] = solve(n-1, 0) + solve(n-1, 2)
	else:
		dp[n][state] = solve(n-1, 0) + solve(n-1, 1)
	
	return dp[n][state]

if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		N = int(input())
		dp = [[-1 for _ in range(5)] for _ in range(N+1)]
		print(solve(N, 0))
