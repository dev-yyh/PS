import sys
input = sys.stdin.readline

def update(node, start, end, target, value):
   if target < start or end < target:
      return tree[node]
   
   if start == end:
      tree[node] = value
      return tree[node]
   
   mid = (start + end)//2
   left = update(node*2, start, mid, target, value)
   right = update(node*2+1, mid+1, end, target, value)
   tree[node] = min(left, right)
   return tree[node]

def query(node, start, end, left, right):
   if right < start or end < left:
      return float('inf')
   
   if left <= start and end <= right:
      return tree[node]
   
   mid = (start + end)//2
   return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))

if __name__ == '__main__':
   N = int(input())
   tree = [float('inf')] * (4*N)
   score = [[0] * (3) for _ in range(N+1)]

   for i in range(3):
      for rank, num in enumerate(list(map(int, input().split()))):
         score[num][i] = rank+1

   score.sort()

   ans = 0
   for i in range(1, N+1):
      if query(1, 1, N, 1, score[i][1]) > score[i][2]:
         ans += 1
      update(1, 1, N, score[i][1], score[i][2])
   
   print(ans)