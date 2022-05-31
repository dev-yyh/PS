import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur):
		q = deque()
		q.append(cur)

		while q:
			cur =q.popleft()
			for next in graph[cur]:
				ret[next] += ret[cur]
				q.append(next)

if __name__ == '__main__':
	n, m = map(int, input().split())
	P = list(map(int, input().split()))
	graph = [[] for _ in range(n+1)]
	for i in range(n):
		cur = i+1
		parent = P[i]
		if parent == -1:
			continue
		graph[parent].append(cur)

	ret = [0 for _ in range(n+1)]
	for _ in range(m):
		i, w = map(int, input().split())
		ret[i] += w
	
	bfs(1)
	print(*ret[1:])



