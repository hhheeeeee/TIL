import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline


def tile(n):
    global memo
    if n >= 3 and memo[n] == 0:
        memo[n] = (tile(n - 1) + (tile(n - 2) * 2))
    return memo[n]


def func(n):
    if n % 10 == 0:
        # 재귀함수의 종료조건
        if n == 10:
            return 1
        if n == 20:
            return 3
        else:
            return func(n - 10) + (2 * func(n - 20))


T = int(input())
for tc in range(1, T + 1):
    n = int(input()) // 10
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 3
    print(f'#{tc} {tile(n)}')
