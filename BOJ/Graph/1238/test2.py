# Use Floyd-Warshall Algorithm (Timeout)
import sys
input = sys.stdin.readline
INF = 100000000

if __name__ == '__main__':
	N, M, X = map(int, input().split())
	graph = [[] for _ in range(N+1)]

	dist = [[INF] * (N+1) for _ in range(N+1)]
	for _ in range(M):
		u, v, t = map(int, input().split())
		dist[u][v] = t
	
	for k in range(1, N+1):
		for i in range(1, N+1):
			for j in range(1, N+1):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

	max_value = 0
	for i in range(1, N+1):
		max_value = max(max_value, dist[i][X]+dist[X][i])
	
	print(max_value)