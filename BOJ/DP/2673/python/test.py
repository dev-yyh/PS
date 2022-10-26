import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    dp = [[0] * (101) for _ in range(101)]
    cost = [[0] * (101) for _ in range(101)]
    
    for _ in range(N):
        a, b = map(int, input().split())
        cost[a][b] = 1
        cost[b][a] = 1
    
    for end in range(1, 101):
        for start in range(end, 0, -1):
            for k in range(start, end):
                dp[start][end] = max(dp[start][end], dp[start][k] + dp[k][end] + cost[start][end])
    
    print(dp[1][100])
