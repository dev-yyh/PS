import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))

    aa = []
    bb = []
    for s in S:
        if s > 0:
            aa.append(s)
        else:
            bb.append(s)
    aa.sort(reverse=True)
    bb.sort()

    temp_a = deque()
    for i, a in enumerate(aa):
        if i % 2:
            temp_a.append(a)
        else:
            temp_a.appendleft(a)

    temp_b = deque()
    for i, b in enumerate(bb):
        if i % 2:
            temp_b.append(b)
        else:
            temp_b.appendleft(b)

    if temp_a and temp_a[0] > temp_a[-1]:
        temp_a.reverse()
    if temp_b and temp_b[0] > temp_b[-1]:
        temp_b.reverse()

    print(' '.join(map(str, temp_b + temp_a)))
