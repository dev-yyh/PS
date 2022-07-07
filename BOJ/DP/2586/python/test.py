import sys
from collections import defaultdict
input = sys.stdin.readline

if __name__ == '__main__':
    P, F = map(int, input().split())
    L = [(i, 0) for i in list(map(int, input().split()))]
    L += [(i, 1) for i in list(map(int, input().split()))]
    L.sort()

    V = defaultdict(list)
    i = 0
    for l in L:
        if l[1] == 0:
            V[i].append(l[0])
            i += 1
        else:
            i -= 1
            V[i].append(l[0])
    
    ans = 0
    for key in V:
        ret = 0
        count = len(V[key])
        for i in range(1, count, 2):
            ret += abs(V[key][i] - V[key][i-1])
        
        if count % 2 == 0:
            ans += ret
            continue
        
        min_value = ret
        for i in range(count-1, 1, -2):
            ret += (abs(V[key][i] - V[key][i-1]) - abs(V[key][i-1] - V[key][i-2]))
            min_value = min(min_value, ret)
        ans += min_value

    print(ans)
