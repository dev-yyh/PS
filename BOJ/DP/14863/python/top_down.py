import sys
input = sys.stdin.readline

def dfs(n, k):
    if k > K:
        return -float('inf')
    if n == N:
        return 0

    if dp[n][k] != -1:
        return dp[n][k]
    
    dp[n][k] = max(dfs(n+1, k+arr[n][0]) + arr[n][1], dfs(n+1, k+arr[n][2]) + arr[n][3])
    
    return dp[n][k]

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1 for _ in range(K+1)] for _ in range(N+1)]

    print(dfs(0, 0))