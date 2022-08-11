import sys
from heapq import *
input = sys.stdin.readline
INF = 100000000

def solve(start, end):
	q = [(0, start)]
	dist[start] = 0
	while q:
		cost, cur = heappop(q)
		if dist[cur] < cost:
			continue
		if cur == end:
			break
		for next, time in graph[cur]:
			if cost + time < dist[next]:
				dist[next] = cost + time
				heappush(q, (dist[next], next))
	print(dist[end])
if __name__ == '__main__':
	N = int(input())
	M = int(input())
	graph = [[] for _ in range(N+1)]
	dist = [INF] *(N+1)

	for _ in range(M):
		u, v, w = map(int, input().split())
		graph[u].append((v, w))
	
	start, end = map(int, input().split())
	solve(start, end)

	