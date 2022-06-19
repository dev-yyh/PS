import sys
input = sys.stdin.readline

def solve(n, k):
    if n == k or k == 0:
        return 1
    
    if dp[n][k] != -1:
        return dp[n][k]
    
    dp[n][k] = (solve(n-1, k-1) + solve(n-1, k)) % M
    return dp[n][k]


if __name__ == "__main__":
    N, K, M = map(int, input().split())
    dp = [[-1 for _ in range(K+1)] for _ in range(N+1)]

    print(solve(N%M, K%M))