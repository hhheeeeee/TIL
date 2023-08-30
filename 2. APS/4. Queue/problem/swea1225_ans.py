import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline
from collections import deque

def pw(lst):
    while True:
        for i in range(1, 6):
            num = lst.pop()
            lst.append(num - 1)

            if lst[-1] <= 0:
                lst[-1] = 0
                return lst


for _ in range(10):
    tc = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{tc} {pw(numbers)}')

