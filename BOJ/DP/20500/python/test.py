# 15�� ����� 3�� ����̸鼭 5�� ����̴�.
# 3�� ����� ��� �ڸ����� ���� ������ 3���� �������� ������ �������� ������ ����
# 5�� ����� 1�� �ڸ����� 0�̰ų� 5�̴�.
# �� ���������� 1�� 5�� ���θ� �̷���� �ֱ� ������ 15�� ����� �Ǳ� ���ؼ� ù��° �ڸ����� ������ 5�� �����ؾ� �Ѵ�.
import sys
input = sys.stdin.readline

MOD = 1000000007
if __name__ == '__main__':
	N = int(input())
	dp = [[0 for _ in range(3)] for _ in range(N+3)] #dp[i][j] i�ڸ��̸鼭 3���� ���� �������� j�� ��
	dp[2][0] = 1 # 15
	dp[2][1] = 1 # 55

	for i in range(3, N+1):
		dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD # 555
		dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD # 115
		dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD # 515, 155
	
	print(dp[N][0])