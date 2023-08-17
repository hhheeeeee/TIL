import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def match(start, end):
    if arr[start] == arr[end] + 1 or arr[start] - arr[end] == -2:
        return start
    elif arr[start] + 1 == arr[end] or arr[end] - arr[start] == -2:
        return end
    elif arr[start] == arr[end]:
        return start


def divide(start, end):
    if start == end:
        return start
    else:
        a = divide(start, (start + end) // 2)
        b = divide((start + end) // 2 + 1, end)
    return match(a, b)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {divide(0, N - 1) + 1}')
