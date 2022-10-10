import sys
input = sys.stdin.readline

MOD = 100003

def hashing(size):
   ret = 0
   for i in range(size):
      ret = (ret*2 + ord(S[i]))%MOD
   return ret

def cmp(idx1, idx2, s):
   for i in range(s):
      if S[idx1+i] != S[idx2+i]:
         return False
   return True

def check(s):
   hash_set = [[] for _ in range(MOD+1)]
   text = hashing(s)
   hash_set[text].append(0)
   for i in range(1, L-s+1):
      text = (2*text - ord(S[i-1])*pow[s] + ord(S[i+s-1]) + MOD)%MOD

      if len(hash_set[text]) > 0:
         for idx in hash_set[text]:
            if cmp(i, idx, s):
               return True
      hash_set[text].append(i)

   return False

if __name__ == '__main__':
   L = int(input())
   S = input().rstrip()
   pow = [1] * L
   for i in range(1, L):
      pow[i] = (pow[i-1] * 2) % MOD
   l = 0
   r = L-1
   ans = 0
   while l <= r:
      mid = (l + r)//2
      if check(mid):
         ans = mid
         l = mid + 1
      else:
         r = mid - 1
   
   print(ans)
