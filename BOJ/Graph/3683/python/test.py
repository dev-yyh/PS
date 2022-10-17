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
	T = int(input())
	for _ in range(T):
		c, d, v = map(int, input().split())
		P = [input().split() for _ in range(v)]
		graph = [[] for _ in range(v)]

		for i in range(v):
			for j in range(i+1, v):
				if P[i][0] ==P[j][1] or P[i][1] == P[j][0]:
					if P[i][0][0] == 'C':
						graph[i].append(j)
					else:
						graph[j].append(i)
		ret = 0
		matched = [-1] * (v)
		for i in range(v):
			visited = [0] * (v)
			ret += solve(i)
		print(v - ret)