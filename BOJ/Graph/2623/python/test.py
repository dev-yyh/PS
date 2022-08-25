import sys
from collections import deque
input = sys.stdin.readline

def solve():
	q = deque()
	for i in range(1, N+1):
		if in_degree[i] == 0:
			q.append(i)
	
	ret = []
	while q:
		cur = q.popleft()
		ret.append(cur)

		for next in graph[cur]:
			in_degree[next] -= 1
			if in_degree[next] == 0:
				q.append(next)
	
	if len(ret) == N:
		for r in ret:
			print(r)
	else:
		print(0)
	
if __name__ == '__main__':
	N, M = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(M)]
	graph = [[] for _ in range(N+1)]
	in_degree = [0] * (N+1)
	for a in arr:
		n = a[0]
		for i in range(1, n):
			graph[a[i]].append(a[i+1])
			in_degree[a[i+1]] += 1
	solve()
	
