import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    board = [[0] * (n+1) for _ in range(n+1)]

    for _ in range (m):
        a, b, c = map(int, input().split())
        dp[a][b] = c
        dp[b][a] = c
        board[a][b] = b
        board[b][a] = a
    
    for i in range(1, n+1):
        dp[i][i] = 0
        board[i][i] = '-'
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    board[i][j] = board[i][k]
    
    for i in range(1, n+1):
        print(' '.join(map(str,board[i][1:])))

