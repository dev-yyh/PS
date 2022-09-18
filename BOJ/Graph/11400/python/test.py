import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur, parent):
	global idx
	idx += 1
	visited[cur] = idx
	min_value = idx
	
	for next in graph[cur]:
		if next == parent:
			continue
		if not visited[next]:
			sub_min_value = dfs(next, cur)
			if sub_min_value > visited[cur]:
				ans.append((min(cur, next), max(cur, next)))
			min_value = min(min_value, sub_min_value)
		else:
			min_value = min(min_value, visited[next])
	
	return min_value

if __name__ == '__main__':
	V, E = map(int, input().split())
	graph = [[] for _ in range(V+1)]
	visited = [0 for _ in range(V+1)]
	ans = []
	for _ in range(E):
		A, B = map(int, input().split())
		graph[A].append(B)
		graph[B].append(A)
	
	idx = 0

	for i in range(1, V+1):
		if not visited[i]:
			dfs(i, None)
	
	print(len(ans))
	ans.sort()
	for a in ans:
		print(*a)