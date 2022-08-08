import sys
input = sys.stdin.readline

if __name__ == '__main__':
	ops = input().rstrip()
	pri = {'(':0, '+':1, '-':1, '*':2, '/':2}
	ans = ''
	stack = []
	for op in ops:
		if 'A' <= op <= 'Z':
			ans += op
		else:
			if op in '(':
				stack.append(op)
			elif op in ')':
				while stack and stack[-1] != '(':
					ans += stack.pop()
				stack.pop()
			else:
				while stack and pri[op] <= pri[stack[-1]]:
					ans += stack.pop()
				stack.append(op)
	while stack:
		ans += stack.pop()
	
	print(ans)