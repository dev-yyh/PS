import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur, is_root):
   global idx
   idx += 1
   visited[cur] = idx
   min_order = idx
   child_cnt = 0

   for child in graph[cur]:
      if not visited[child]:
         child_cnt += 1
         sub_min_order = dfs(child, False)
         if visited[cur] <= sub_min_order and not is_root:
            selected[cur] = 1
         min_order = min(min_order, sub_min_order)
      else:
         min_order = min(min_order, visited[child])
   
   if is_root and child_cnt > 1:
      selected[cur] = 1

   return min_order

if __name__ == '__main__':
   V, E = map(int, input().split())
   graph = [[] for _ in range(V+1)]
   visited = [0 for _ in range(V+1)]
   selected = [0 for _ in range(V+1)]
   for _ in range(E):
      a, b = map(int, input().split())
      graph[a].append(b)
      graph[b].append(a)
   
   idx = 0
   for i in range(1, V+1):
      if not visited[i]:
         dfs(i, True)

   ans = []
   for i in range(1, V+1):
      if selected[i] == 1:
         ans.append(i)

   print(len(ans))
   print(*ans)