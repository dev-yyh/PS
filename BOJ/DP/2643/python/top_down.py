import sys
input = sys.stdin.readline

def check(a, b):
    if a[0] >= b[0] and a[1] >= b[1]:
        return True
    if a[0] >= b[1] and a[1] >= b[0]:
        return True
    return False

def solve(idx):
    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = 1
    for i in range(N):
        if idx != i and check(P[idx], P[i]):
            dp[idx] = max(dp[idx], solve(i) + 1)
    
    return dp[idx]

if __name__ == '__main__':
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    dp = [-1 for _ in range(N)]

    for i in range(N):
        dp[i] = solve(i)
    
    print(max(dp))


