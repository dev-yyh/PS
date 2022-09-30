import sys
import heapq
input = sys.stdin.readline
INF = 1000000000

def daijkstra():
	q = []
	heapq.heappush(q, (0, S, 0))
	dist[S][0] = 0
	ret = INF
	while q:
		cost, cur, cnt = heapq.heappop(q)

		flag = False
		for i in range(cnt):
			if dist[cur][i] < cost:
				flag = True
				break

		if flag or dist[cur][cnt] < cost or cnt >= N:
			continue

		if cur == D:
			ret = min(ret, dist[cur][cnt])
			continue

		for next, n_cost in graph[cur]:
			if dist[next][cnt+1] > cost + n_cost:
				dist[next][cnt+1] = cost + n_cost
				heapq.heappush(q, (dist[next][cnt+1], next, cnt + 1))
	
	return ret

def solve(t):
	ans = INF
	for i in range(1, N+1):
		ans = min(ans, dist[D][i] + t * i)

	return ans

if __name__ == '__main__':
	N, M, K = map(int, input().split())
	S, D = map(int, input().split())

	graph = [[] for _ in range(N+1)]
	for _ in range(M):
		a, b, w = map(int, input().split())
		graph[a].append((b, w))
		graph[b].append((a, w))
	
	dist = [[INF] * (N+1) for _ in range(N+1)]
	print(daijkstra())
	
	sum = 0
	for i in range(K):
		sum += int(input())
		print(solve(sum))