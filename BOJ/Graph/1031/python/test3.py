import sys
from collections import deque
input = sys.stdin.readline

MAX = 105
class Graph:
	def __init__(self, n):
		self.graph = [[] for _ in range(n)]
		self.capacity = [[0] * n for _ in range(n)]
		self.flow = [[0] * n for _ in range(n)]
	
	def add(self, a, b, c):
		self.graph[a].append(b)
		self.graph[b].append(a)
		self.capacity[a][b] = c
	
	def max_flow(self, src, sink):
		flow_sum = 0
		while 1:
			parent = [-1] * MAX
			q = deque()
			q.append(src)
			while q:
				cur = q.popleft()
				for next in self.graph[cur]:
					if self.capacity[cur][next] > self.flow[cur][next] and parent[next] == -1:
						q.append(next)
						parent[next] = cur
			if parent[sink] == -1:
				break

			i = sink
			while i != src:
				s = parent[i]
				e = i
				self.flow[s][e] += 1
				self.flow[e][s] -= 1
				i = parent[i]
			flow_sum += 1
		return flow_sum
	
	def chg_flow(self, src, sink):
		parent = [-1] * MAX
		q = deque()
		q.append(src)

		while q:
			cur = q.popleft()
			for next in self.graph[cur]:
				if cur < src or (cur == src and next < sink):
					continue
				if self.capacity[cur][next] > self.flow[cur][next] and parent[next] == -1:
					q.append(next)
					parent[next] = cur
		if parent[sink] == -1:
			return
		self.flow[src][sink] = 0
		self.flow[sink][src] = 0

		i = sink
		while i != src:
			s = parent[i]
			e = i
			self.flow[s][e] += 1
			self.flow[e][s] -= 1
			i = parent[i]
		return

if __name__ == '__main__':
	N, M = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))

	graph = Graph(MAX)
	src = 101
	sink = 102

	for i in range(N):
		graph.add(src, i, A[i])
	
	for i in range(M):
		graph.add(50+i, sink, B[i])
	
	for i in range(N):
		for j in range(M):
			graph.add(i, 50+j, 1)
	
	if graph.max_flow(src, sink) != sum(B):
		print(-1)
		exit()

	for i in range(N):
		for j in range(M):
			if graph.flow[i][j+50] != 1: 
				continue
			graph.chg_flow(i, j+50)

	for i in range(N):
		for j in range(M):
			print(graph.flow[i][j+50], end='')
		print()
