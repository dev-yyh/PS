import sys
input = sys.stdin.readline

MOD = 1000000007

def pow(x, y):
   ret = 1
   while y:
      if y%2:
         ret = (ret * x) % MOD
      x = (x * x) % MOD
      y //= 2
   return ret

def make_prime(n):
   is_not_prime[0] = 1
   is_not_prime[1] = 1
   for i in range(2, n+1):
      if is_not_prime[i]:
         continue
      for j in range(i*2, n+1, i):
         is_not_prime[j] = 1

if __name__ == '__main__':
   N, M = map(int, input().split())
   
   min_value = min(N, M)
   is_not_prime = [0] * (min_value+1)
   make_prime(min_value)

   ans = 1
   for i in range(min_value+1):
      if is_not_prime[i]:
         continue
      cnt = 0
      j = i
      while j <= min_value:
         cnt += (N//j) * (M//j)
         j *= i
      ans *= pow(i, cnt)
      ans %= MOD
   
   print(ans)
