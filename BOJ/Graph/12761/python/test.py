import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    A, B, N, M = map(int, input().split())

    visited = [-1] * (100001)

    q = deque()
    q.append(N)
    visited[N] = 0
    while q:
        cur = q.popleft()

        for i in [1, -1, A, -A, B, -B]:
            nx = cur + i
            if 0 <= nx < 100001 and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[cur] + 1

        for i in [A, B]:
            nx = cur * i
            if 0 <= nx < 100001 and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[cur] + 1

    print(visited[M])
