import sys
input = sys.stdin.readline
INF=5000 * 10000
def solve(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    for _ in range(N-1):
        for u, v, d in edge:
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
    
    for u, v, d in edge:
        if dist[u] + d < dist[v]:
            return True
    return False

if __name__ == '__main__':
    TC = int(input())
    for _ in range(TC):
        N, M, W = map(int, input().split())
        edge = []
        for _ in range(M):
            S, E, T = map(int, input().split())
            edge.append((S, E, T))
            edge.append((E, S, T))
        
        for _ in range(W):
            S, E, T = map(int, input().split())
            edge.append((S, E, -T))
        
        if solve(1):
            print('YES')
        else:
            print('NO')
