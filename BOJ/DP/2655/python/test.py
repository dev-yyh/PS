import sys
input = sys.stdin.readline

def solve():
    dp = [0 for _ in range(N+1)]
    max_height = 0
    idx = 0
    for i in range(1, N+1):
        for j in range(i):
            if block[i][2] > block[j][2]:
                dp[i] = max(dp[i], dp[j]+ block[i][1])
        
        if max_height < dp[i]:
            max_height = dp[i]
            idx = i
    ret = []

    while idx != 0:
        if dp[idx] == max_height:
            ret.append(block[idx][3])
            max_height -= block[idx][1]
        idx -= 1
    
    cnt = len(ret)
    print(cnt)
    for i in range(cnt-1,-1,-1):
        print(ret[i])

if __name__ == '__main__':
    N = int(input())
    block = [[0]*3] + [list(map(int, input().split())) for _ in range(N)]
    index = 0
    for b in block:
        b.append(index)
        index += 1
    block.sort()

    solve()

