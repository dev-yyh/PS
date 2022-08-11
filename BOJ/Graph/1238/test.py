# Use Dijkstra's Algorithm (Success)
import sys
import heapq
input = sys.stdin.readline
INF = 100000000

def solve(start, graph):
	dist = [INF for _ in range(N+1)]
	h = []
	heapq.heappush(h, (0, start))
	dist[start] = 0

	while h:
		cost, cur = heapq.heappop(h)

		for next, time in graph[cur]:
			if cost + time < dist[next]:
				dist[next] = cost + time
				heapq.heappush(h, (dist[next], next))
	return dist

if __name__ == '__main__':
	N, M, X = map(int, input().split())
	graph = [[] for _ in range(N+1)]
	r_graph = [[] for _ in range(N+1)]

	for _ in range(M):
		u, v, t = map(int, input().split())
		graph[u].append((v, t))
		r_graph[v].append((u, t))

	dist = solve(X, graph)
	r_dist = solve(X, r_graph)

	max_value = 0
	for i in range(1, N+1):
		max_value = max(max_value, dist[i]+r_dist[i])
	
	print(max_value)
