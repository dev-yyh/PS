import sys
input = sys.stdin.readline

def check_cur_state(state):
	for i in range(M):
		if (state & (3<<i)) == (3<<i):
			return False
	return True

def check_pre_state(state, line, idx):
	if no_seat[line] & (1<<idx):
		return False
	if idx > 0 and state & (1<<(idx-1)):
		return False
	if idx < M-1 and state & (1<<(idx+1)):
		return False
	return True

def solve(n, prev):
	if n == N:
		return 0
	if dp[n][prev] != -1:
		return dp[n][prev]
	
	dp[n][prev] = 0
	for curr in range(1<<M):
		cnt = 0
		flag = True
		if not check_cur_state(curr):
			continue
		for j in range(M):
			if curr & (1<<j):
				cnt += 1
				if not check_pre_state(prev, n, j):
					flag = False
					break
		if flag == True:
			dp[n][prev] = max(dp[n][prev], solve(n+1, curr)+cnt)
		
	return dp[n][prev]

if __name__ == "__main__":
	C = int(input())

	for _ in range(C):
		N, M = map(int, input().split())
		seat = [input().rstrip() for _ in range(N)]
		no_seat = [0 for _ in range(N)]
		for i in range(N):
			for j in range(M):
				if seat[i][j] == 'x':
					no_seat[i] |= (1 << j)

		dp = [[-1 for _ in range(1<<M)] for _ in range(N)]
		print(solve(0, 0))