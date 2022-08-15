import sys
from heapq import *
input = sys.stdin.readline
INF = 10000000

def bfs(start):
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, cur = heappop(q)

        for next, l in graph[cur]:
            if cost + l < dist[next]:
                dist[next] = cost + l
                heappush(q, (dist[next], next))

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    cnt = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))
    
    ans = 0
    for i in range(1, n+1):
        dist = [INF]*(n+1)
        bfs(i)
        total = 0
        for j in range(1, n+1):
            if dist[j] <= m:
                total += cnt[j]
        ans = max(ans, total)
    print(ans)