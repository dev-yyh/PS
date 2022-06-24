import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    P =list(map(int, input().split()))
    M = int(input())
    
    dp = [0 for _ in range(M+1)]

    for i in range(N-1, -1, -1):
        p = P[i]
        for j in range(p, M+1):
            dp[j] = max(dp[j-p]*10+i, dp[j])
    
    print(dp[M])