import sys
input = sys.stdin.readline

def solve(cur):
	if visited[cur]:
		return 0
	visited[cur] = 1

	for next in graph[cur]:
		if matched[next] == -1 or solve(matched[next]):
			matched[next] = cur
			return 1
	return 0

if __name__ == '__main__':
	N, M, K = map(int, input().split())

	graph =[[] for _ in range(N)]
	for i in range(N):
		works = list(map(int, input().split()))
		for j in works[1:]:
			graph[i].append(j)
	
	ans = 0
	matched = [-1] * (M+1)
	for i in range(N):
		visited = [0] * N
		ans += solve(i)

	cnt = 0
	for i in range(N):
		visited = [0] * N
		cnt += solve(i)
		if cnt == K:
			break

	print(ans+cnt)