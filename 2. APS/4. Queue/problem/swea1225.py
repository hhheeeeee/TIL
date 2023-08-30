import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline
from collections import deque

for _ in range(10):
    tc = int(input())
    arr = deque(list(map(int, input().split())))
    k = 1
    while True:
        if k == 6:
            k = 1
        first = arr.popleft() - k
        if first <= 0:
            arr.append(0)
            break
        arr.append(first)
        k += 1

    print(f'#{tc}', end = " ")
    print(*arr)
