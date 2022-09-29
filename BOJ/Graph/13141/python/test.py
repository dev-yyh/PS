import sys
input = sys.stdin.readline
INF = 10000000

def solve():
	for k in range(1, N+1):
		for i in range(1, N+1):
			for j in range(1, N+1):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
	
	ans = INF
	for v in range(1, N+1):
		time = 0
		for edge in edges:
			s, e, l = edge
			time = max(time, l + dist[v][e] + dist[v][s])
		ans = min(ans, time)
	return ans / 2

if __name__ == '__main__':
	N, M = map(int, input().split())
	
	dist = [[INF] * (N+1) for _ in range(N+1)]
	edges = []
	for i in range(1, N+1):
		dist[i][i] = 0

	for _ in range(M):
		S, E, L = map(int, input().split())
		edges.append((S, E, L))
		if dist[S][E] == INF or dist[S][E] > L:
			dist[S][E] = L
			dist[E][S] = L

	print(solve())