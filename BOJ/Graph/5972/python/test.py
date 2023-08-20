import sys
import heapq
input = sys.stdin.readline


def bfs():
    q = []
    heapq.heappush(q, (0, 1))
    cost[1] = 0

    while q:
        d, cur = heapq.heappop(q)

        if cost[cur] < d:
            continue

        for next, c in graph[cur]:
            if cost[next] > d + c:
                cost[next] = d + c
                heapq.heappush(q, (cost[next], next))
    return cost[N]


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    cost = [float('inf')] * (N + 1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    print(bfs())
