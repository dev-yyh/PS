import sys
input = sys.stdin.readline

def add(idx, var):
    i = idx
    while i <= N:
        tree[i][0] += var
        if var > 0:
            tree[i][1] += 1
        else:
            tree[i][1] -= 1
        i += (i & -i)

def query(idx):
    i = idx
    ans = [0, 0]

    while i > 0:
        ans[0] += tree[i][0]
        ans[1] += tree[i][1]
        i -= (i & -i)
    return ans

def range_sum(l, r):
    add(l, l)
    add(r+1, -l)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    tree = [[0,0] for _ in range(N+1)]

    for _ in range(Q):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            range_sum(cmd[1], cmd[2])
        else:
            q = query(cmd[1])
            ans = q[1] * (cmd[1]+1) - q[0] + A[cmd[1]-1]
            print(ans)