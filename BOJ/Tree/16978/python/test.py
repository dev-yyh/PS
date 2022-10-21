import sys
input = sys.stdin.readline

def add(i, var):
	while i <= N:
		tree[i] += var
		i += (i & -i)

def sum(i):
	ret = 0
	while i > 0:
		ret += tree[i]
		i -= (i & -i)
	return ret

def update(i, var):
	diff = var - A[i]
	A[i] = var
	add(i, diff)

def query(l, r):
	return sum(r) - sum(l-1)
if __name__ == '__main__':
    N = int(input())
    A = [0] + list(map(int, input().split()))
    M = int(input())
    tree = [0] * (N + 1)
    for i in range(1, N+1):
	    add(i, A[i])

    u = []
    q = []
    idx = 0
    for _ in range(M):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1: 
            u.append((cmd[1], cmd[2]))
        else:
            q.append((cmd[1], cmd[2], cmd[3], idx))
            idx += 1

    q.sort()
    j = 0
    ans = [0] * idx
    for c1, c2, c3, i in q:
        while j < c1:
            update(u[j][0], u[j][1])
            j += 1
        ans[i] = query(c2, c3)

    for x in ans: 
        print(x)