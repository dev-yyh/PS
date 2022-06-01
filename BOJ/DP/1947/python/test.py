import sys
input = sys.stdin.readline

MOD = 1000000000
if __name__ == "__main__":
    N = int(input())
    dp = [0 for _ in range(N+3)]
    dp[1] = 0
    dp[2] = 1

    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2])*(i-1) % MOD
    
    print(dp[N])