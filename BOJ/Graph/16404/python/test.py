import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def init(cur, par):
	global cnt
	cnt += 1
	start[cur] = cnt
	for next in graph[cur]:
		if next != par:
			init(next, cur)
	end[cur] = cnt

def add(i, var):
	while i <= N:
		tree[i] += var
		i += (i & -i)

def update(idx, var):
	add(start[idx], var)
	add(end[idx]+1, -var)

def query(i):
	i = start[i]
	ret = 0
	while i > 0:
		ret += tree[i]
		i -= (i & -i)
	return ret

if __name__ == '__main__':
	N, M = map(int, input().split())
	cnt = 0
	tree = [0] * (N+1)
	start = [0] * (N+1)
	end = [0] * (N+1)
	
	parent = list(map(int, input().split()))
	graph = [[] for _ in range(N+1)]
	for i in range(1, N):
		graph[parent[i]].append(i+1)

	init(1, -1)

	for _ in range(M):
		cmd = list(map(int, input().split()))
		if cmd[0] == 1:
			update(cmd[1], cmd[2])
		else:
			print(query(cmd[1]))
		