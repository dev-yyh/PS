# 인접한 비트의 개수
## 문제
0과 1로 이루어진 수열 S가 있다. S의 첫 수는 s1이고, 마지막 수는 sn이다. S의 인접한 비트의 개수는 다음과 같이 구할 수 있다.

s1*s2 + s2*s3 + s3*s4 + ... + sn-1 * sn

위의 식을 이용하면 수열 S에서 인접한 1의 개수를 구할 수 있다. 예를들어, 011101101의 인접한 비트의 개수는 3이 되고, 111101101은 4, 010101010은 0이 된다.

수열 S의 크기 n과 k가 주어졌을 때, 인접한 비트의 개수가 k인 수열 S의 개수를 구하는 프로그램을 작성하시오.

예를 들어, n이 5이고, k가 2이면, 수열 S가 될 수 있는 수열은 다음과 같이 6가지가 있다.

11100, 01110, 00111, 10111, 11101, 11011
## 입력
첫째 줄에 테스트 케이스의 수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 수 2개가 공백으로 구분되어 이루어져 있다. 첫 번째 수는 n이고, 두 번째 수는 k이다. n과 k는 100을 넘지 않는 자연수이다.
## 출력
각 테스트 케이스에 대해 인접한 비트의 개수가 k인 수열 S의 개수를 한 줄에 하나씩 출력한다. 이 값은 2,147,483,647보다 작거나 같다.
## 예제 입력 1
```
10
5 2
20 8
30 17
40 24
50 37
60 52
70 59
80 73
90 84
100 90
```
## 예제 출력1
```
6
63426
1861225
168212501
44874764
160916
22937308
99167
15476
23076518
```