import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    print(max(dp))