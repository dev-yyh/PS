import sys
import heapq
input = sys.stdin.readline

MOD = 1000000007
if __name__ == '__main__':
	N, k ,P = map(int, input().split())
	graph = [[] for _ in range(N)]
	r_graph = [[] for _ in range(N)]

	in_degree = [0 for _ in range(N)]
	r_in_degree = [0 for _ in range(N)]

	for _ in range(P):
		a, b = map(int, input().split())
		graph[b].append(a)
		r_graph[a].append(b)
		in_degree[a] += 1
		r_in_degree[b] += 1
	
	q =	[]
	r_q = []
	for i in range(k):
		if in_degree[i] == 0:
			heapq.heappush(q, i)
		if r_in_degree[i] == 0:
			heapq.heappush(r_q, i)
	
	x = N - k
	max_value = [0 for _ in range(N)]
	while q:
		cur = heapq.heappop(q)
		max_value[cur] = x
		x += 1
		for next in graph[cur]:
			in_degree[next] -= 1
			if in_degree[next] == 0:
				heapq.heappush(q, next)

	x = k - 1
	min_value = [0 for _ in range(N)]
	while r_q:
		cur = heapq.heappop(r_q)
		min_value[cur] = x
		x -= 1
		for next in r_graph[cur]:
			r_in_degree[next] -= 1
			if r_in_degree[next] == 0:
				heapq.heappush(r_q, next)
	
	ans = 0
	for i in range(k):
		ans = (ans + (max_value[i] - min_value[i]) * pow(N, i, MOD)) % MOD
	
	print(ans % MOD)