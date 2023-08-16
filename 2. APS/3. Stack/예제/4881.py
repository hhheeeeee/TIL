import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def subsum(r, s, N, p):
    global res
    if r == N and s < res:
        res = s
        return

    if s > res:
        return

    else:
        for c in range(N):
            if c not in p:
                p[r] = c
                subsum(r + 1, s + arr[r][c], N, p)
                p[r] = -1


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [-1] * (N*1)
    res = 1000000
    subsum(0, 0, N, p)
    print(f'#{tc} {res}')


