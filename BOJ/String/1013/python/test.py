# 정규식 사용
import sys
import re
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    P = re.compile('(100+1+|01)+')
    for _ in range(T):
        S = input().rstrip()
        if P.fullmatch(S):
            print('YES')
        else:
            print('NO')