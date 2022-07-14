import sys
from collections import deque
input = sys.stdin.readline
class Graph:
    def __init__(self, n):
        self.size = n
        self.graph = [[] for _ in range(n)]
        self.capacity = [[0] * n for _ in range(n)]
        self.flow = [[0] * n for _ in range(n)]
        self.path = [-1] * n

    def add(self, a, b, c):
        self.graph[a].append(b)
        self.graph[b].append(a)
        self.capacity[a][b] = c

    def bfs(self, start, end):
        q = deque()
        q.append(start)
        self.path[start] = start
        while q:
            cur = q.popleft()
            for next in self.graph[cur]:
                if self.capacity[cur][next] - self.flow[cur][next] > 0 and self.path[next] == -1:
                    self.path[next] = cur
                    q.append(next)
                    if next == end:
                        return True
        if self.path[end] == -1:
            return False

        return True

    def max_flow(self, start, end):
        self.flow = [[0] * self.size for _ in range(self.size)]
        total = 0
        while 1:
            self.path = [-1] * self.size
            if not self.bfs(start, end):
                break

            flow_num = float('inf')
            i = end
            while i != start:
                s = self.path[i]
                e = i
                flow_num = min(flow_num, self.capacity[s][e] - self.flow[s][e])
                i = self.path[i]

            i = end
            while i != start:
                s = self.path[i]
                e = i
                self.flow[s][e] += flow_num
                self.flow[e][s] -= flow_num
                i = self.path[i]

            total += flow_num
        return total
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        ai = list(map(int, input().split()))
        adj = [input().rstrip() for _ in range(n)]
        src = 2*n
        sink = 2*n + 1
        graph = Graph(2*n+2)

        team = []
        enemy = []
        for i in range(n):
            if ai[i] == 0:
                continue
            flag = True
            for j in range(n):
                if adj[i][j] == 'Y' and ai[j] == 0:
                    flag = False
            if flag:
                team.append(i)
            else:
                enemy.append(i)
        
        for t in team:
            graph.add(src, t, ai[t] - 1)
            graph.add(t, t+n, ai[t])
        
        for e in enemy:
            graph.add(src, e, ai[e])
            graph.add(e, e+n, ai[e])
            graph.add(e, sink, float('inf'))
        
        for i in range(n):
            for j in range(n):
                if adj[i][j] == 'Y':
                    graph.add(n+i, j ,float('inf'))

        l = 0
        r = 10000
        while l <= r:
            mid = (l + r) // 2
            f = mid * len(enemy)
            for i in enemy:
                graph.capacity[i][sink] = mid

            flow_num = graph.max_flow(src, sink)
            if flow_num == f:
                l = mid + 1
            else:
                r = mid - 1

        print(r)