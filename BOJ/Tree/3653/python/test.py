# Segment Tree
import sys
import math
input = sys.stdin.readline

def query(node, start, end, left, right):
   if left <= start and end <= right:
      return tree[node]
   
   if right < start or end < left:
      return 0
   
   mid = (start + end)//2
   return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

def update(node, start, end, target, diff):
   if target < start or end < target:
      return 

   tree[node] += diff  
   if start != end:
      mid = (start+end)//2
      update(node*2, start, mid, target, diff)
      update(node*2+1, mid+1, end, target, diff)

if __name__ == '__main__':
   T = int(input())

   for _ in range(T):
      n, m = map(int, input().split())
      height = math.ceil(math.log2(n+m))
      tree_size = 1 << (height+1)
      tree = [0] * tree_size

      idx = {}
      for i in range(m+1, n+m+1):
         update(1, 1, n+m, i, 1)
         idx[i-m] = i
      lst = list(map(int, input().split()))
      ans = []
      for i, l in enumerate(lst):
         ans.append(query(1, 1, n+m, 1, idx[l]-1))
         update(1, 1, n+m, idx[l], -1)
         idx[l] = m - i
         update(1, 1, n+m, idx[l], 1)
      print(*ans)