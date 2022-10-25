import sys
from collections import deque
input = sys.stdin.readline

class Graph:
    def __init__ (self, n):
        self.graph = [[] for _ in range(n+1)]
        self.capacity = [[0] * (n+1) for _ in range(n+1)]
        self.flow = [[0] * (n+1) for _ in range(n+1)]

    def add(self, a, b, c):
        self.graph[a].append(b)
        self.graph[b].append(a)
        self.capacity[a][b] = c

    def bfs(self, src, sink, path):
        q = deque()
        q.append(src)
        path[src] = src

        while q:
            cur = q.popleft()
            for next in self.graph[cur]:
                if self.capacity[cur][next] - self.flow[cur][next] > 0 and path[next] == -1:
                    path[next] = cur
                    q.append(next)
                    if next == sink:
                        return True
        return False
#        if path[sink] == -1:
#            return False
#        return True
    
    def solve(self, src, sink):
        path = [-1] * (sink + 1)
        cnt = 0
        while self.bfs(src, sink, path):
            i = sink
            while i != src:
                self.flow[path[i]][i] += 1
                self.flow[i][path[i]] -= 1
                i = path[i]
            cnt += 1
            path = [-1] * (sink + 1)
        return cnt

if __name__ == '__main__':
    N, K, D = map(int, input().split())
    kind = list(map(int, input().split()))
    Z = [list(map(int, input().split())) for _ in range(N)]
    src = N + D + 1
    sink = src + 1
    g = Graph(sink)

    for i in range(1, N+1):
        g.add(src, i, K)
    for i in range(N):
        cnt = Z[i][0]
        for j in range(1, cnt+1):
            g.add(i+1, Z[i][j]+N, 1)
    for i in range(1, D+1):
        g.add(i+N, sink, kind[i-1])

    print(g.solve(src, sink))


