# 15의 배수는 3의 배수이면서 5의 배수이다.
# 3의 배수는 모든 자리수를 더한 값에서 3으로 나눴을때 나누어 떨어지는 성질이 있음
# 5의 배수는 1의 자릿수가 0이거나 5이다.
# 이 문제에서는 1과 5의 수로만 이루어져 있기 때문에 15의 배수가 되기 위해선 첫번째 자리수는 무조건 5로 시작해야 한다.
import sys
input = sys.stdin.readline

MOD = 1000000007
if __name__ == '__main__':
	N = int(input())
	dp = [[0 for _ in range(3)] for _ in range(N+3)] #dp[i][j] i자리이면서 3으로 나눈 나머지가 j인 수
	dp[2][0] = 1 # 15
	dp[2][1] = 1 # 55

	for i in range(3, N+1):
		dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD # 555
		dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD # 115
		dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD # 515, 155
	
	print(dp[N][0])