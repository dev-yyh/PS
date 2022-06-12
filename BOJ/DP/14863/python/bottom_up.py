import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = [[0,0,0,0]] + [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1 for _ in range(K+1)] for _ in range(N+1)]

    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(K+1):
            if dp[i-1][j] == -1:
                continue
            
            if j+arr[i][0] <= K:
                dp[i][j+arr[i][0]] = max(dp[i][j+arr[i][0]], dp[i-1][j] + arr[i][1])
            if j+arr[i][2] <= K:
                dp[i][j+arr[i][2]] = max(dp[i][j+arr[i][2]], dp[i-1][j] + arr[i][3])
    
    print(max(dp[N]))