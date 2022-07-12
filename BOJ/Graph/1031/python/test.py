import sys
from collections import deque
input = sys.stdin.readline

class Graph:
	def __init__(self, n):
		self.size = n
		self.graph = [[] for _ in range(n)]
		self.capacity = [[0]*n for _ in range(n)]
		self.flow = [[0]*n for _ in range(n)]
	
	def add(self, a, b, c):
		self.graph[a].append(b)
		self.graph[b].append(a)
		self.capacity[a][b] = c
	
	def max_flow(self, start, end):
		flow_sum = 0
		while 1:
			parent = [-1] * self.size
			q = deque()
			q.append(start)
			while q:
				cur = q.popleft()
				for next in self.graph[cur]:
					if self.capacity[cur][next] > self.flow[cur][next] and parent[next] == -1:
						q.append(next)
						parent[next] = cur
			if parent[sink] == -1:
				break

			i = end
			while i != start:
				s = parent[i]
				e = i
				self.flow[s][e] += 1
				self.flow[e][s] -= 1
				i = parent[i]
			flow_sum += 1
		return flow_sum
	
	def chg_flow(self, start, end):
		self.flow[src][start] -= 1; self.flow[start][src] += 1
		self.flow[start][end] -= 1; self.flow[end][start] += 1
		self.flow[end][sink] -= 1; self.flow[sink][end] += 1

		parent = [-1] * self.size
		parent[src] = src
		q = deque()
		q.append(src)

		flag = False
		while q:
			cur = q.popleft()
			for next in self.graph[cur]:
				if self.capacity[cur][next] > self.flow[cur][next] and parent[next] == -1:
					q.append(next)
					parent[next] = cur
					if next == sink:
						flag = True
						break
		
		if not flag:
			self.flow[src][start] += 1; self.flow[start][src] -= 1
			self.flow[start][end] += 1; self.flow[end][start] -= 1
			self.flow[end][sink] += 1; self.flow[sink][end] -= 1	
		else:
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

	graph = Graph(N+M+2)
	src = 0
	sink = N+M+1

	for i in range(1,N+1):
		graph.add(src, i, A[i-1])
	
	for i in range(1, M+1):
		graph.add(i+N, sink, B[i-1])
	
	for i in range(1, N+1):
		for j in range(1, M+1):
			graph.add(i, j+N, 1)
	
	if sum(A) != sum(B):
		print(-1)
		exit()

	if graph.max_flow(src, sink) != sum(B):
		print(-1)
		exit()

	for i in range(1, N+1):
		for j in range(1, M+1):
			graph.capacity[i][j+N] = 0
			if graph.flow[i][j+N] != 1: 
				continue
			graph.chg_flow(i, j+N)
	
	ans = []
	for i in range(1, N+1):
		ans.append([graph.flow[i][j+N] for j in range(1, M+1)])
	
	for a in ans:
		print(''.join(map(str, a)))
