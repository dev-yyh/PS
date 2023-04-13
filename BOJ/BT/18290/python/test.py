import sys
input = sys.stdin.readline

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(depth, x, y, ret):
    global ans
    if depth == k:
        ans = max(ans, ret)
        return

    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if visited[i][j]:
                continue

            flag = False
            for d in dir:
                nx = i + d[0]
                ny = j + d[1]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                    flag = True
                    break

            if not flag:
                visited[i][j] = 1
                dfs(depth + 1, i, j, ret + board[i][j])
                visited[i][j] = 0
    return


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    ans = -1000000

    dfs(0, 0, 0, 0)

    print(ans)
