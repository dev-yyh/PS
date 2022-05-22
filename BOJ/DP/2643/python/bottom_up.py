import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    P = sorted([sorted(list(map(int, input().split()))) for _ in range(N)])
    dp = [1 for _ in range(N)]

    for i in range(1, N):
        for j in range(i):
            if P[i][1] >= P[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    
    print(max(dp))

