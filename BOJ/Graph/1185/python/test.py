import sys
import heapq
input = sys.stdin.readline

def solve(start):
   visited = [0] * (N+1)
   q = []
   heapq.heappush(q, (C[start], start))

   ret = 0
   while q:
      c_cost, cur = heapq.heappop(q)
      if visited[cur]:
         continue

      visited[cur] = 1
      ret += c_cost

      for next, n_cost in graph[cur]:
         if not visited[next]:
            heapq.heappush(q, (n_cost, next))
   return ret

if __name__ == '__main__':
   N, P = map(int, input().split())
   C = [0] + list(int(input()) for _ in range(N))
   graph = [[] for _ in range(N+1)]
   for _ in range(P):
      s, e, l = map(int, input().split())
      cost = C[s] + C[e] + 2*l
      graph[s].append((e, cost))
      graph[e].append((s, cost))
   
   start = 1
   min_value = C[1]
   for i in range(2, N+1):
      if min_value > C[i]:
         min_value = C[i]
         start = i
   ans = solve(start)
   print(ans)