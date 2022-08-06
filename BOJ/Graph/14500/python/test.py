import sys
input = sys.stdin.readline

def dfs(x, y, depth, s):
    global result
    if max_value*(4-depth) + s <= result:
        return

    if depth >= 4:
        if result < s:
            result = s
        return

    for i, j in d:
        nx = x+i; ny = y+j
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth == 2:
                visited[nx][ny] = 1
                dfs(x, y, depth+1, s+arr[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, depth+1, s+arr[nx][ny])
            visited[nx][ny] = 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    max_value = max(map(max, arr))
    result = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            dfs(i, j, 1, arr[i][j])
            visited[i][j] = 0
    
    print(result)