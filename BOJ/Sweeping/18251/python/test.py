import sys
import math
input = sys.stdin.readline

def dfs(idx, y):
    if idx > N:
        return
    dfs(2*idx, y+1)
    node.append((y, W[idx-1]))
    dfs(2*idx+1, y+1)

if __name__ == '__main__':
    N = int(input())
    W = list(map(int, input().split()))
    node = []
    dfs(1, 0)
    h = math.ceil(math.log2(N))
    
    ans = node[0][1]
    for i in range(h):
        for j in range(i, h):
            s = 0
            for n in node:
                if n[0] < i or n[0] > j:
                    continue
                if s + n[1] < 0:
                    ans = max(ans, n[1])
                    s = 0
                else:
                    s += n[1]
                    ans = max(ans, s)
    print(ans)
    
            