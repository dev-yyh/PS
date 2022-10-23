import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def init(cur):
   global cnt
   cnt += 1
   start[cur] = cnt

   for next in tree[cur]:
      if depth[next] == 0:
         depth[next] = depth[cur] + 1
         init(next)
   
   end[cur] = cnt

def update(i):
   i = start[i]
   while i <= N:
      bit[i] += 1
      i += (i & -i)

def query(i):
   return sum(end[i]) - sum(start[i]-1)

def sum(i):
   ret = 0
   while i > 0:
      ret += bit[i]
      i -= (i & -i)
   return ret

if  __name__ == '__main__':
   N, C = map(int, input().split())
   tree = [[] for _ in range(N+1)]
   bit = [0] * (N+1)
   cnt = 0
   start = [0] * (N+1)
   end = [0] * (N+1)
   depth = [0] * (N+1)
   for _ in range(N-1):
      x, y = map(int, input().split())
      tree[x].append(y)
      tree[y].append(x)
   
   depth[C] = 1
   init(C)

   Q = int(input())
   for _ in range(Q):
      cmd, idx = map(int, input().split())
      if cmd == 1:
         update(idx)
      else:
         print(query(idx) * depth[idx])
