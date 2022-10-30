import sys
import bisect
input = sys.stdin.readline

def build(node, start, end):
   if start == end:
      tree[node].append(A[start])
      return
   
   mid = (start + end)//2
   build(node*2, start, mid)
   build(node*2+1, mid+1, end)

   tree[node] = tree[node*2] + tree[node*2+1]
   tree[node].sort()
   return

def query(node, start, end, left, right, k):
   if left <= start and end <= right:
      return len(tree[node]) - bisect.bisect_right(tree[node], k)
   if right < start or end < left:
      return 0
   
   mid = (start + end)//2
   return query(node*2, start, mid, left, right, k) + query(node*2+1, mid+1, end, left, right, k)


if __name__ == '__main__':
   N = int(input())
   tree = [[] for _ in range(4*N)]
   A = list(map(int, input().split()))
   M = int(input())

   build(1, 0, N-1)

   last_ans = 0
   for _ in range(M):
      a, b, c = map(int, input().split())
      i = a ^ last_ans
      j = b ^ last_ans
      k = c ^ last_ans

      last_ans = query(1, 0, N-1, i-1, j-1, k)
      print(last_ans)

