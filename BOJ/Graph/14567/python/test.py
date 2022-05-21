import sys
from collections import deque
input = sys.stdin.readline

def solve():
    ret = [1 for _ in range(N+1)]
    
    q = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            q.append(i)
    
    while q:
        cur = q.popleft()

        for next in graph[cur]:
            ret[next] = ret[cur] + 1
            
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)
    
    print(*ret[1:])

if __name__ == '__main__':
    N, M = map(int, input().split())
    in_degree = [0 for _ in range(N+1)]
    graph =[[] for _ in range(N+1)]

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        in_degree[B] += 1
    
    solve()