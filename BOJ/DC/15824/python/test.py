import sys
input = sys.stdin.readline

MOD = 1000000007

if __name__ == '__main__':
   N = int(input())
   A = list(map(int, input().split()))
   A.sort()

   dp = [1]
   for i in range(N):
      dp.append((dp[-1]*2)%MOD)

   ans = 0
   for i in range(N):
      ans += (dp[i] - dp[N-i-1]) * A[i]
      ans %= MOD
   
   print(ans)
