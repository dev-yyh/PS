import sys
input = sys.stdin.readline

def dfs(prev, cur):
   for next, cost in graph[cur]:
      if next == prev:
         continue
      dp[0][next] = (cur, cost)
      dfs(cur, next)

def query(cur, cost):
   for i in range(19, -1, -1):
      parent, p_cost = dp[i][cur]
      if p_cost <= cost:
         cost = cost - p_cost
         cur = parent
   if cur == 1:
      return 1
   else:
      return cur
if __name__ == '__main__':
   n = int(input())
   ant = [int(input()) for _ in range(n)]
   graph = [[] for _ in range(n+1)]

   for _ in range(n-1):
      a, b, c = map(int, input().split())
      graph[a].append((b, c))
      graph[b].append((a, c))
   
   dp = [[(0, 0)] * (n+1) for _ in range(20)]
   dfs(-1, 1)
   dp[0][1] = (1, 0)
   
   for i in range(1, 20):
      for j in range(1, n+1):
         parent, cost = dp[i-1][j]
         dp[i][j] = (dp[i-1][parent][0], dp[i-1][parent][1] + cost)
   
   for i in range(n):
      print(query(i+1, ant[i]))