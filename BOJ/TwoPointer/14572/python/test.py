import sys
input = sys.stdin.readline

def get_E(l, r):
   n = r-l+1
   cnt1 = 0
   cnt2 = 0
   for i in range(1, K+1):
      if arr[i] > 0:
         cnt1 +=1
      if arr[i] == n:
         cnt2 +=1
   return (cnt1 - cnt2)*n

if __name__ == '__main__':
   N, K, D = map(int, input().split())
   arr = [0] * (K+1)
   S = []
   for idx in range(N):
      M, d = map(int, input().split())
      S.append((d, M, list(map(int, input().split()))))

   S.sort()
   for i in S[0][2]:
      arr[i] += 1
   l = 0
   r = 0
   ans = 0
   while r < N:
      if S[r][0] - S[l][0] <= D:
         ans = max(ans, get_E(l, r))
         r += 1
         if r >= N:
            break

         for i in S[r][2]:
            arr[i] += 1
         continue
      
      for i in S[l][2]:
         arr[i] -= 1
      l += 1

   print(ans)
         

