import sys
input = sys.stdin.readline

def check(color):
    value = 0
    dp = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            value = 0
            if (i+j) % 2 == 0:
                if board[i-1][j-1] != color:
                    value = 1
            else:
                if board[i-1][j-1] == color:
                    value = 1
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + value
    ret = float('inf')
    for i in range(1, N+2-K):
        for j in range(1, M+2-K):
            ret = min(ret, dp[i+K-1][j+K-1] - dp[i+K-1][j-1] - dp[i-1][j+K-1] + dp[i-1][j-1])
    return ret

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    print(min(check('W'), check('B')))