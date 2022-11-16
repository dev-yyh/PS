import sys
import math
input = sys.stdin.readline

def propagate(node, start, end):
    if lazy[node] != 0:
        tree[node] = (lazy[node]+tree[node][0], lazy[node]+tree[node][1])

        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2 + 1] += lazy[node]
        lazy[node] = 0

def update(node, start, end, left, right, k):
    propagate(node, start, end)

    if end < left or right < start:
        return tree[node]
    if left <= start and end <= right:
        lazy[node] += k
        propagate(node, start, end)
        return tree[node]

    mid = (start + end) // 2
    t1 = update(node*2, start, mid, left, right, k)
    t2 = update(node*2+1, mid+1, end, left, right, k)

    tree[node] = (min(t1[0], t2[0]), max(t1[1], t2[1]))
    return tree[node]

def query(node, start, end, left, right):
    propagate(node, start, end)
    if end < left or right < start:
        return 10001, -10001
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end)//2
    left_child = query(node*2, start, mid, left, right)
    right_child = query(node*2+1, mid+1, end, left, right)

    return min(left_child[0], right_child[0]), max(left_child[1], right_child[1])

def getValue(left, right, var):
    min_value, max_value = query(1, 0, C-1, left, right)
    ret = var
    if N < max_value + var:
        ret = N - max_value
    elif min_value + var < 0:
        ret = -min_value
    return ret

if __name__ == '__main__':
    C, N, O = map(int, input().split())
    h = math.ceil(math.log2(C))
    size = 1 << (h+1)
    tree = [(0 ,0) for _ in range(size)] # list하면 메모리 초과
    lazy = [0 for _ in range(size)]

    for _ in range(O):
        cmd = input().split()
        if cmd[0] == 'change':
            X, S = int(cmd[1]), int(cmd[2])
            val = getValue(X, X, S)
            update(1, 0, C-1, X, X, val)
            print(val)
        elif cmd[0] == 'groupchange':
            A, B, S = int(cmd[1]), int(cmd[2]), int(cmd[3])
            val = getValue(A, B, S)
            update(1, 0, C-1, A, B, val)
            print(val)
        else:
            X = int(cmd[1])
            ret, _ = query(1, 0, C-1, X, X)
            print(ret)