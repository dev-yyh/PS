import sys
from collections import deque
input = sys.stdin.readline

def solve(n):
    q = deque()

    q.append(n)
    count[n] = 1
    while q:
        curr = q.popleft()

        for next, cnt in graph[curr]:
            count[next]+= count[curr] * cnt
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)
    
    for i in range(1, n+1):
        if not graph[i]:
            print(i, count[i])

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    in_degree = [0 for _ in range(N+1)]
    count = [0 for _ in range(N+1)]
    
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        graph[X].append((Y, Z))
        in_degree[Y] += 1
    
    solve(N)
