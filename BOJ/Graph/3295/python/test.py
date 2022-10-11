import sys
input = sys.stdin.readline

def dfs(cur):
	visited[cur] = 1

	for next in graph[cur]:
		if matched[next] < 0 or (not visited[matched[next]] and dfs(matched[next])):
			matched[next] = cur
			return 1
	return 0

if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		n, m = map(int, input().split())
		graph = [[] for _ in range(n)]
		for _ in range(m):
			u, v = map(int, input().split())
			graph[u].append(v)
		
		matched = [-1] * n
		ans = 0
		for i in range(n):
			visited = [0] * n
			ans += dfs(i)
		print(ans)