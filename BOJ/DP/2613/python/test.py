import sys
input = sys.stdin.readline

def check(value):
    tmp = []
    need_group = M
    group_cnt = 0
    i = 0
    while i < N:
        s = 0
        cnt = 0
        while i < N:
            s += array[i]
            cnt += 1

            if s > value:
                s -= array[i]
                cnt -= 1
                break
            
            if need_group - group_cnt == N - i:
                i += 1
                break
            i += 1

        tmp.append(cnt)
        group_cnt += 1

    return M >= group_cnt, tmp

if __name__ == '__main__':
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    left = max(array)
    right = sum(array)

    while left <= right:
        mid = (left + right)//2
        ret, tmp = check(mid)
        if ret:
            ans = mid
            ans_list = tmp
            right = mid - 1
        else:
            left = mid + 1
    
    print(ans)
    print(*ans_list)