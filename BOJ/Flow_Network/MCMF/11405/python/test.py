import sys
from collections import deque
input = sys.stdin.readline
INF = 1000000
class Graph:
    def __init__ (self, n):
        self.graph = [[] for _ in range(n+1)]
        self.capacity = [[0] * (n+1) for _ in range(n+1)]
        self.flow = [[0] * (n+1) for _ in range(n+1)]
        self.dist = [[0] * (n+1) for _ in range(n+1)]

    def add (self, a, b, cap, cost):
        self.graph[a].append(b)
        self.graph[b].append(a)
        self.capacity[a][b] = cap
        self.dist[a][b] = cost
        self.dist[b][a] -= cost
    
    def bfs(self, src, sink, path):
        dist = [INF] * (sink + 1)
        inQueue = [0] * (sink + 1)
        q = deque()
        q.append(src)
        inQueue[src] = 1
        dist[src] = 0

        while q:
            cur = q.popleft()
            inQueue[cur] = 0
            for next in self.graph[cur]:
                if self.capacity[cur][next] > self.flow[cur][next] and dist[next] > dist[cur] + self.dist[cur][next]:
                    dist[next] = dist[cur] + self.dist[cur][next]
                    path[next] = cur
                    if not inQueue[next]:
                        inQueue[next] = 1
                        q.append(next)
        if path[sink] == -1:
            return False
        return True

    def solve(self, src, sink):
        path = [-1] * (sink + 1)
        ret = 0
        while self.bfs(src, sink, path):
            flow_num = INF
            i = sink
            while i != src:
                flow_num = min(flow_num, self.capacity[path[i]][i] - self.flow[path[i]][i])
                i = path[i]

            i = sink
            while i != src:
                self.flow[path[i]][i] += flow_num
                self.flow[i][path[i]] -= flow_num
                ret += self.dist[path[i]][i] * flow_num
                i = path[i]
            path = [-1] * (sink + 1)
        return ret

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [list(map(int, input().split())) for _ in range(M)]

    src = N + M
    sink = N + M + 1
    graph = Graph(sink)
    for i in range(N):
        graph.add(i+M, sink, A[i], 0)

    for i in range(M):
        graph.add(src, i, B[i], 0)
    
    for i in range(M):
        for j in range(N):
            graph.add(i, j+M, INF, C[i][j])
    
    print(graph.solve(src, sink))