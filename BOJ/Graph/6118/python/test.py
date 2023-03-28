import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [-1] * (N + 1)

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    q = deque()
    q.append(1)
    visited[1] = 0

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur] + 1

    max_v = max(visited)
    print(visited.index(max_v), max_v, visited.count(max_v))
