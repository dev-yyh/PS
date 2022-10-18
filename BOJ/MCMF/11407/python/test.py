import sys
from collections import deque
input = sys.stdin.readline

class Graph:
	def __init__(self, n):
		self.graph = [[] for _ in range(n+1)]
		self.flow = [[0] * (n+1) for _ in range(n+1)]
		self.capacity = [[0] * (n+1) for _ in range(n+1)]
		self.cost = [[0] * (n+1) for _ in range(n+1)]

	def add(self, a, b, c, cost):
		self.graph[a].append(b)
		self.graph[b].append(a)
		self.capacity[a][b] = c
		self.cost[a][b] = cost
		self.cost[b][a] = -cost
	
	def bfs(self, src, sink, path):
		isQueue = [False] * (sink + 1)
		cost = [float('inf') for _ in range(sink + 1)]
		q = deque()
		q.append(src)
		cost[src] = 0
		isQueue[src] = True

		while q:
			cur = q.popleft()
			isQueue[cur] = False

			for next in self.graph[cur]:
				if self.capacity[cur][next] - self.flow[cur][next] > 0 and cost[next] > cost[cur] + self.cost[cur][next]:
					cost[next] = cost[cur] + self.cost[cur][next]
					path[next] = cur
					if not isQueue[next]:
						q.append(next)
						isQueue[next] = True
			
		if path[sink] == -1:
			return False

		return True
	
	def solve(self, src, sink):
		path = [-1] * (sink + 1)
		ret = 0
		cnt = 0
		while self.bfs(src, sink, path):
			cnt += 1
			i = sink
			while i != src:
				ret += self.cost[path[i]][i]
				self.flow[path[i]][i] += 1
				self.flow[i][path[i]] -= 1
				i = path[i]
			path = [-1] * (sink + 1)
		
		return cnt, ret

if __name__ == '__main__':
	N, M = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	C = [list(map(int, input().split())) for _ in range(M)]
	D = [list(map(int, input().split())) for _ in range(M)]

	src = 2 * 100
	sink = 2 * 100 + 1
	graph = Graph(sink)
	for i in range(N):
		graph.add(i, sink, A[i], 0)
	
	for i in range(M):
		for j in range(N):
			if C[i][j] > 0:
				graph.add(i+100, j, C[i][j], D[i][j])
	
	for i in range(M):
		graph.add(src, i+100, B[i], 0)
	
	cnt , ans = graph.solve(src, sink)
	print(cnt)
	print(ans)
