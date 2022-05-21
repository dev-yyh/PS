import sys
input = sys.stdin.readline

def lower_bound(key):
    left = 0
    right = len(ret) - 1
    while left < right:
        mid = (left + right)//2
        if key > ret[mid]:
            left = mid + 1
        else:
            right = mid
    return right

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    ret = [nums[0]]

    for i in range(1, N):
        if ret[-1] < nums[i]:
            ret.append(nums[i])
        else:
            idx = lower_bound(nums[i])
            ret[idx] = nums[i]
    
    print(len(ret))