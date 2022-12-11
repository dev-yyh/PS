# 재귀 풀이
import sys
input = sys.stdin.readline

def is_pattern(start, end):
    if start >= end:
        return True
    flag = False

    if start < end-1 and P[start] == '0':
        if P[start+1] == '1':
            flag |= is_pattern(start+2, end)
    else:
        idx = start + 1
        cnt_zero = 0
        cnt_one = 0
        while idx < end and P[idx] == '0':
            idx += 1
            cnt_zero += 1

        if cnt_zero < 2:
            return flag

        while idx < end and P[idx] == '1':
            idx +=1
            cnt_one +=1

        if cnt_one == 1:
            flag |= is_pattern(idx, end)
        if cnt_one >= 2:
            if idx == end-1:
                return flag
            if idx + 1 < end and P[idx+1] == '0':
                flag |= is_pattern(idx-1, end)
            else:
                flag |= is_pattern(idx, end)

    return flag

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        P = input().rstrip()
        if is_pattern(0, len(P)):
            print('YES')
        else:
            print('NO')