import sys
from collections import deque
input = sys.stdin.readline

def get_dist(start, end):
	q = deque()
	q.append((start, 0))

	while q:
		cur, cost = q.popleft()

		for next, time in graph[cur]:
			d[next] = max(d[next], cost+time)
			in_degree[next] -= 1
			if in_degree[next] == 0:
				q.append((next, d[next]))
	return d[end]

def get_edge_cnt(end):
	q = deque()
	q.append(end)
	visited = set()

	cnt = 0
	while q:
		cur = q.popleft()
		
		for prev, time in r_graph[cur]:
			if d[cur] - time == d[prev]:
				cnt += 1
				if not prev in visited:
					visited.add(prev)
					q.append(prev)
	return cnt

if __name__ == '__main__':
	n = int(input())
	m = int(input())
	graph = [[] for _ in range(n+1)]
	r_graph = [[] for _ in range(n+1)]
	d = [0 for _ in range(n+1)]
	in_degree = [0 for _ in range(n+1)]
	for _ in range(m):
		a, b, c = map(int, input().split())
		graph[a].append((b, c))
		r_graph[b].append((a, c))
		in_degree[b] += 1
	
	start, end = map(int, input().split())
	print(get_dist(start, end))
	print(get_edge_cnt(end))
