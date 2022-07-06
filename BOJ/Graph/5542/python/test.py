import sys
import heapq
input = sys.stdin.readline

def find(x):
	if parent[x] == x:
		return x
	parent[x] = find(parent[x])
	return parent[x]

def union(x, y):
	x = find(x)
	y = find(y)
	parent[x] = y

if __name__ == "__main__":
	N, M, K, Q = map(int, input().split())
	graph = [[] for _ in range(N+1)]
	edge = []
	parent = [i for i in range(N+1)]

	for i in range(M):
		a, b, c = map(int, input().split())
		graph[a].append((b, c))
		graph[b].append((a, c))
		edge.append([0, (a,b)])
	
	d = [float('inf') for _ in range(N+1)]
	hq = []
	for _ in range(K):
		k = int(input())
		d[k] = 0
		heapq.heappush(hq, (0, k))

	while hq:
		dist, u = heapq.heappop(hq)
		if d[u] > dist:
			continue

		for v, w in graph[u]:
			if d[v] > dist + w:
				d[v] = dist + w
				heapq.heappush(hq, (d[v], v))

	for i in range(M):
		u, v = edge[i][1]
		edge[i][0] = min(d[u], d[v])
	edge.sort(reverse=True)
	
	q = [set() for _ in range(N+1)]
	for i in range(Q):
		x, y = map(int, input().split())
		q[x].add(i)
		q[y].add(i)

	ret = [0 for _ in range(N+1)]
	for i in range(M):
		u, v = edge[i][1]
		lo = find(u)
		hi = find(v)
		if lo == hi:
			continue
		if len(q[lo]) > len(q[hi]):
			lo ,hi = hi, lo
		for next in q[lo]:
			if next in q[hi]:
				ret[next] = edge[i][0]
				q[hi].remove(next)
			else:
				q[hi].add(next)
		union(lo, hi)
	
	for i in range(Q):
		print(ret[i])
