import sys
from collections import deque
input = sys.stdin.readline

def solve():
	q = deque()
	q.append((0, 0, 0))

	visited[0][0] = True
	while q:
		a_idx, b_idx, c_idx = q.popleft()

		if len(a) > a_idx and a[a_idx] == c[c_idx] and not visited[a_idx+1][b_idx]:
			q.append((a_idx+1, b_idx, c_idx+1))
			visited[a_idx+1][b_idx] = True
		
		if len(b) > b_idx and b[b_idx] == c[c_idx] and not visited[a_idx][b_idx+1]:
			q.append((a_idx, b_idx+1, c_idx+1))
			visited[a_idx][b_idx+1] = True

	if c_idx == len(c):
		return True
	else:
		return False

if __name__ == '__main__':
	N = int(input())
	for i in range(1, N+1):
		a, b, c = input().split()
		visited = [[False for _ in range(len(b)+1)] for _ in range(len(a)+1)]
		ret = solve()
		if ret:
			print(f'Data set {i}: yes')
		else:
			print(f'Data set {i}: no')