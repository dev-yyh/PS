import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = 1000000000

def dijkstra(s):
	dist = [INF for _ in range(N)]
	q = []
	heapq.heappush(q, (0, s))
	dist[s] = 0
	while q:
		c_d, cur = heapq.heappop(q)
		if dist[cur] < c_d:
			continue

		for next in graph[cur]:
			cost = c_d + graph[cur][next]
			if dist[next] == cost:
				path[next].append(cur)
			elif dist[next] > cost:
				dist[next] = cost
				path[next] = [cur]
				heapq.heappush(q, (cost, next))
	if dist[D] == INF:
		return -1
	else:
		return dist[D]

def remove_edge(d):
	q = deque()
	q.append(d)
	while q:
		cur = q.popleft()
		for next in path[cur]:
			if graph[next][cur] != INF:
				graph[next][cur] = INF
				q.append(next)

if __name__ == '__main__':
	while True:
		N, M = map(int, input().split())
		if N == 0 and M == 0:
			break
		
		S, D = map(int, input().split())
		graph = [dict() for _ in range(N)]
		path = [[] for _ in range(N)]

		for _ in range(M):
			U, V, P = map(int, input().split())
			graph[U][V] = P

		if dijkstra(S) == -1:
			print(-1)
			continue
		remove_edge(D)
		print(dijkstra(S))