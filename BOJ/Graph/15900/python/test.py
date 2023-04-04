import sys
from collections import deque
input = sys.stdin.readline


def sol(root):
    visited = [-1] * (N + 1)
    q = deque()
    q.append(root)
    visited[root] = 0
    cnt = 0

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur] + 1

    for i in range(2, N + 1):
        if len(graph[i]) == 1:
            cnt += visited[i]

    if cnt % 2:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(sol(1))
