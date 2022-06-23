import sys
import heapq
input = sys.stdin.readline

def solve(src, dst):
	q = []
	heapq.heappush(q, (0, src, price[src]))
	while q:
		cost, cur, c_price= heapq.heappop(q)

		if cur == dst:
			return cost
		if dp[cur][c_price] < cost:
			continue
		for next, dist in graph[cur]:
			n_price = min(c_price, price[next])
			if dp[next][n_price] > cost + dist * c_price:
				dp[next][n_price] = cost + dist * c_price
				heapq.heappush(q, (dp[next][n_price], next, n_price))
	
	return min(dp[dst])

if __name__ == '__main__':
	N, M = map(int, input().split())
	price = [0] + list(map(int, input().split()))
	dp = [[float('inf') for _ in range(max(price)+1)] for _ in range(N+1)]
	
	graph = [[] for _ in range(N+1)]
	for _ in range(M):
		a, b, c = map(int, input().split())
		graph[a].append((b, c))
		graph[b].append((a, c))
	
	print(solve(1, N))