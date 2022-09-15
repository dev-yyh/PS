import sys
from collections import deque
input = sys.stdin.readline

def make_tree(root):
	q = deque()
	q.append((root, 0))
	parent[root] = 0
	level[root] = 0
	while q:
		cur, cost = q.popleft()
		for next, t in graph[cur]:
			if parent[next] != -1:
				continue
			level[next] = level[cur] + 1
			parent[next] = cur
			dist[next] = cost+t
			q.append((next, cost+t))

def lca(a, b):
	if a == 1 or b == 1:
		return 1
	
	if level[a] < level[b]:
		a, b = b, a
	
	while level[a] != level[b]:
		a = parent[a]
	
	while a != b:
		a = parent[a]
		b = parent[b]
	
	return a

if __name__ == '__main__':
	N = int(input())
	graph = [[] for _ in range(N+1)]
	parent = [-1 for _ in range(N+1)]
	dist = [0 for _ in range(N+1)]
	level = [0 for _ in range(N+1)]
	for _ in range(N-1):
		u, v, c = map(int, input().split())
		graph[u].append((v, c))
		graph[v].append((u, c))
	
	make_tree(1)

	M = int(input())
	for _ in range(M):
		a, b = map(int, input().split())
		ret = dist[a] + dist[b] - 2*dist[lca(a, b)]
		print(ret)