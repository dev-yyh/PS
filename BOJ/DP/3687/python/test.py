import sys
input = sys.stdin.readline

def max_value(n):
	value = 0
	if n % 2 == 0:
		for i in range(n//2):
			value += 10**i
	else:
		for i in range(n//2-1):
			value += 10**i
		value += 7 * (10**(n//2-1))
	return value

if __name__ == "__main__":
	T = int(input())
	min_value = [float('inf') for _ in range(101)]
	min_value[2] = 1
	min_value[3] = 7
	min_value[4] = 4
	min_value[5] = 2
	min_value[6] = 6
	min_value[7] = 8
	min_value[8] = 10
	for i in range(9, 101):
		for j in range(2, 8):
			if j != 6:
				min_value[i] = min(min_value[i], min_value[i-j] * 10 + min_value[j])
			else:
				min_value[i] = min(min_value[i], min_value[i-j] * 10)
	
	for _ in range(T):
		n = int(input())
		print(min_value[n], max_value(n))
