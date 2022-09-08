import sys
import copy
input = sys.stdin.readline

def push(cx, cy):
	for x, y in dir:
		nx = cx + x
		ny = cy + y
		if 0 <= nx < 10 and 0 <= ny < 10:
			temp[nx][ny] ^= 1
	temp[cx][cy] ^= 1

if __name__ == '__main__':
	board = [[0] * 10 for _ in range(10)]
	for i in range(10):
		str = input().rstrip()
		for j, c in enumerate(str):
			if c == 'O':
				board[i][j] = 1

	dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	ans = 101
	for step in range(1 << 10):
		temp = copy.deepcopy(board)
		cnt = 0

		for i in range(10):
			if step & (1<<i):
				cnt += 1
				push(0, i)

		for i in range(1, 10):
			for j in range(10):
				if not temp[i-1][j]:
					continue
				push(i, j)
				cnt += 1
	
		if sum(temp[9]) == 0:
			ans = min(cnt, ans)

print(ans if ans != 101 else -1)