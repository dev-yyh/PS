import sys
input = sys.stdin.readline

def update(target, value):
   i = target
   while i <= N:
      tree[i] = min(tree[i], value)
      i += (i & -i)

def query(idx):
   i = idx
   ret = tree[i]
   while i:
      ret = min(ret, tree[i])
      i -= (i & -i)
   return ret

if __name__ == '__main__':
   N = int(input())
   tree = [float('inf')] * (N+1)
   score = [[0] * (3) for _ in range(N+1)]

   for i in range(3):
      for rank, num in enumerate(list(map(int, input().split()))):
         score[num][i] = rank+1

   score.sort()

   ans = 0
   for i in range(1, N+1):
      if query(score[i][1]) > score[i][2]:
         ans += 1
      update(score[i][1], score[i][2])
   
   print(ans)