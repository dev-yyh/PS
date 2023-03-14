import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur = q.popleft()

        if cur == G:
            return visited[cur]

        for next in [cur + U, cur - D]:
            if 0 < next <= F and visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur] + 1
    return "use the stairs"


if __name__ == '__main__':
    F, S, G, U, D = map(int, input().split())
    graph = [[] for _ in range(F + 1)]
    visited = [-1] * (F + 1)

    print(bfs(S))
