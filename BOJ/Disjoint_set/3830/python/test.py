import sys 
input = sys.stdin.readline

def find(x):
	if parent[x] < 0:
		return x
	p = find(parent[x])
	weight[x] += weight[parent[x]]
	parent[x] = p
	return parent[x]

def union(x, y, w):
	root_x = find(x)
	root_y = find(y)
	if root_x == root_y:
		return
	
	if parent[root_x] > parent[root_y]:
		root_x, root_y = root_y, root_x
		x, y = y, x
		w = -w

	weight[root_y] = weight[x] - weight[y] + w
	parent[root_x] += parent[root_y]
	parent[root_y] = root_x

if __name__ == '__main__':
	while 1:
		N, M = map(int, input().split())
		if N == 0 and M == 0:
			break
		parent = [-1 for _ in range(N+1)]
		weight = [0 for _ in range(N+1)]
		for _ in range(M):
			cmd = list(input().split())
			if cmd[0] == '!':
				a, b, w = map(int, cmd[1:])
				union(a, b, w)
			else:
				a, b = map(int, cmd[1:])
				if find(a) == find(b):
					print(weight[b] - weight[a])
				else:
					print('UNKNOWN')