import sys
input = sys.stdin.readline

def dfs(cur, idx):
    if idx == n:
        return 0
    
    if dp[cur][idx] != -1:
        return dp[cur][idx]
    
    dp[cur][idx] = dfs(name[idx]+1, idx+1) + (m-cur+1) * (m-cur+1)

    if cur+name[idx] <= m:
        dp[cur][idx] = min(dp[cur][idx], dfs(cur+name[idx]+1, idx+1))
    return dp[cur][idx]

if __name__ == '__main__':
    n ,m = map(int, input().split())
    name = [int(input()) for _ in range(n)]
    dp = [[-1 for _ in range(n+1)] for _ in range(m+2)]

    print(dfs(0, 0))

