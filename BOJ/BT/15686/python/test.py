import sys
input = sys.stdin.readline
INF = 10000000
def dfs(dep, n):
	global ans
	ret = 0
	if dep == M:
		for r1, c1 in house:
			min_value = INF
			for i in range(len(chicken)):
				if visited[i]:
					r2, c2 = chicken[i]
					min_value = min(min_value, abs(r1-r2)+abs(c1-c2))
			ret += min_value
		ans = min(ans, ret)
		return
	
	for i in range(n, len(chicken)):
		if not visited[i]:
			visited[i] = 1
			dfs(dep+1, i+1)
			visited[i] = 0
	return

if __name__ == '__main__':
	N, M = map(int, input().split())
	city =[list(map(int, input().split())) for _ in range(N)]
	house = []
	chicken = []
	for i in range(N):
		for j in range(N):
			if city[i][j] == 1:
				house.append((i, j))
			elif city[i][j] == 2:
				chicken.append((i, j))
	visited = [0 for _ in range(len(chicken))]
	ans = INF
	dfs(0,0)
	print(ans)