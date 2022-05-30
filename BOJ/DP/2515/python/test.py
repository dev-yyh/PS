from bisect import bisect_right
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
pictures = []
heights = []

for _ in range(n):
    h, c = map(int, input().split())
    pictures.append([h, c])
    heights.append(h)

heights.sort()
pictures.sort(key=lambda x:x[0])
dp = [0]

for i in range(n):
    h, c = pictures[i]
    j = bisect_right(heights, h-s)
    dp.append(max(dp[i], c+dp[j]))

print(dp[n])