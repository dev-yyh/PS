import sys
from collections import deque

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N + 1)
    visited = [0] * (N + 1)

    for i in range(1, N+1):
        x, y = map(int, input().split())
        graph[i].append(x)
        graph[i].append(y)
        in_degree[x] += 1
        in_degree[y] += 1

    q = deque()
    for i in range(1, N+1):
        if in_degree[i] < 2:
            q.append(i)
            visited[i] = 1

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            in_degree[next] -= 1
            if in_degree[next] < 2 and not visited[next]:
                visited[next] = 1
                q.append(next)

    ret = []
    for i in range(1, N+1):
        if not visited[i]:
            ret.append(i)

    print(len(ret))
    print(*ret)
