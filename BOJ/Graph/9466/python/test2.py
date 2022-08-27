# use topological sorting
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        graph = [[] for _ in range(n+1)]
        nums = [0]+list(map(int, input().split()))
        in_degree = [0] *(n+1)

        for i in range(1, n+1):
            graph[i].append(nums[i])
            in_degree[nums[i]] += 1
        
        cnt = 0
        q = deque()
        for i in range(1, n+1):
            if in_degree[i] == 0:
                cnt += 1
                q.append(i)
        
        while q:
            cur = q.popleft()

            for next in graph[cur]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    cnt += 1
                    q.append(next)
        
        print(cnt)