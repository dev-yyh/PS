import sys
input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	a = 1
	b = 1
	for i in range(2, n+1):
		b, a = (a+b)%10, b

	print(b)
	