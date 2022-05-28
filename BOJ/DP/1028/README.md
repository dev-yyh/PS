# 다이아몬드 광산(P5)
## 문제
다이아몬드 광산은 0과 1로 이루어진 R행*C열 크기의 배열이다.

다이아몬드는 1로 이루어진 정사각형의 경계선을 45도 회전시킨 모양이다. 크기가 1, 2, 3인 다이아몬드 모양은 다음과 같이 생겼다.
```
size 1:    size 2:    size 3:
                         1
              1         1 1
   1         1 1       1   1
              1         1 1
                         1

```
다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력하는 프로그램을 작성하시오.

## 입력
첫째 줄에 R과 C가 주어진다. R과 C는 750보다 작거나 같은 자연수이다. 둘째 줄부터 R개의 줄에는 다이아몬드 광산의 모양이 주어진다.

## 출력
첫째 줄에 다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력한다. 만약 다이아몬드가 없을 때는 0을 출력한다.

## 예제 입력 1
```
5 5
01100
01011
11111
01111
11111
```

## 예제 출력 1
```
3
```

## 예제 입력 2
```
5 5
01100
00011
11111
01111
11111
```

## 예제 출력 2
```
2
```

## 예제 입력 3
```
4 4
0000
0000
0000
0000
```

## 예제 출력 3
```
0
```

## 예제 입력 4
```
3 6
111000
101111
111111
```

## 예제 출력 4
```
2
```