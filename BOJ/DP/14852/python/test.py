import sys
input = sys.stdin.readline

MOD = 1000000007
if __name__ == '__main__':
    N = int(input())
    dp = [0 for _ in range(N+1)]
    dp[0:3] = [1, 2, 7]

    sum = 0
    for i in range(3, N+1):
        sum += dp[i-3]
        dp[i] = (2*dp[i-1] + 3*dp[i-2] + 2*sum) % MOD
    
    print(dp[N])