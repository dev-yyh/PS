import sys
input = sys.stdin.readline

MOD = 1000000007

def pow(a, b):
   ret = [[0 for _ in range(N)] for _ in range(N)]
   for i in range(N):
      ret[i][i] = 1
   
   while b:
      if b % 2:
         ret = mul(ret, a)
      a = mul(a, a)
      b >>= 1

   return ret

def mul(A, B):
   ret = [[0 for _ in range(N)] for _ in range(N)]
   for i in range(N):
      for j in range(N):
         for k in range(N):
            ret[i][j] += (A[i][k]*B[k][j]) % MOD
         ret[i][j] %= MOD
   return ret

if __name__ == '__main__':
   T, N, D = map(int, input().split())
   graph = []
   for _ in range(T):
      M = int(input())
      arr = [[ 0 for _ in  range(N)] for _ in  range(N)]
      for _ in range(M):
         a, b, c = map(int, input().split())
         arr[a-1][b-1] = c
      graph.append(arr)
   
   ans = [[0 for _ in range(N)] for _ in range(N)]
   for i in range(N):
      ans[i][i] = 1

   for i in range(T):
      ans = mul(ans, graph[i])
   ans = pow(ans, D//T)
   for i in range(D%T):
      ans = mul(ans, graph[i])

   for a in ans:
      print(*a)
