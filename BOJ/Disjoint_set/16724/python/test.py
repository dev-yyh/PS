import sys
input = sys.stdin.readline

def get_node(x, y):
    return x*M + y

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return 

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    parent = [-1 for _ in range (N*M)]
    dir ={'D':(1, 0), 'U':(-1, 0), 'L':(0, -1), 'R':(0, 1)}
    visited = set()
    cnt = 0
    for i in range(N):
        for j in range(M):
            x, y = dir[board[i][j]]
            union(get_node(i, j), get_node(i+x, j+y))
    
    cnt = 0
    for i in range(N*M):
        if parent[i] < 0:
            cnt += 1

    print(cnt)