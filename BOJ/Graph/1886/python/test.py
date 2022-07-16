import sys
from collections import deque
input = sys.stdin.readline

class Graph:
    def __init__(self, n):
        self.size = n
        self.graph = [[] for _ in range(n)]
        self.match = [[-1] * n for _ in range(n)]
        self.visit = [0] * n

    def make(self):
        self.S = []
        self.D = []
        for i in range(N):
            for j in range(M):
                if board[i][j] == '.':
                    self.S.append((i,j))
                elif board[i][j] == 'D':
                    self.D.append((i,j))
        dic = [(0,1), (0,-1), (1,0), (-1,0)]
        for i, j in self.S:
            self.visit = [0] * self.size
            q=deque()
            q.append((i, j, 0))
            while q:
                cx, cy, cnt = q.popleft()
                if board[cx][cy] == 'D':
                    self.graph[id(i,j)].append((id(cx, cy), cnt))
                    continue

                for x, y in dic:
                    nx = cx + x
                    ny = cy + y
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if self.visit[id(nx, ny)] == 0 and board[nx][ny] != 'X':
                        self.visit[id(nx, ny)] = 1
                        q.append((nx, ny, cnt+1))

    def dfs(self, cur, limit):
        if self.visit[cur]:
            return False
        self.visit[cur] = 1

        for next, cost in self.graph[cur]:
            if cost > limit:
                continue
            for i in range(cost, limit+1):
                if self.match[next][i] == -1 or self.dfs(self.match[next][i], limit):
                    self.match[next][i] = cur
                    return True
        return False

    def solve(self, limit):
        cnt = 0
        self.match = [[-1] * self.size for _ in range(self.size)]
        for i, j in self.S:
            self.visit = [0] * self.size
            if self.dfs(id(i, j), limit):
                cnt += 1
        return cnt >= len(self.S)

def id(x, y):
    return x*M+y

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = list(input().rstrip() for _ in range(N))

    sink = N*M+1
    graph = Graph(sink)

    graph.make()

    l = 0
    r = sink
    while l <= r:
        mid = (l+r)//2
        if graph.solve(mid):
            r = mid - 1
        else:
            l = mid + 1
    
    if r == sink:
        print('impossible')
    else:
        print(l)
