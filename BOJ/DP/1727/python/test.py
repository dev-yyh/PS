import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    M = [0] + list(map(int, input().split()))
    W = [0] + list(map(int, input().split()))
    M.sort()
    W.sort()

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j-1] + abs(M[i] - W[j])
            if i > j:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            elif i < j:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
    
    print(dp[n][m])