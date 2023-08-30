import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline
from collections import deque

a = int(input())
for tc in range(1, a + 1):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    fire = deque([[arr[i], i] for i in range(N)]) # 처음에 화덕에 피자를 넣는다
    i, turn = 0, 0
    # 화덕에 가장 마지막까지 남아있는 피자 번호
    while True:
        # 한 바퀴 돌 때마다 치즈가 반으로 줄어든다
        fire.rotate(-1)
        turn += 1
        if turn == N:
            turn = 0
            for c in fire:
                c[0] //= 2

        if fire:
            if fire[0][0] == 0: # 만약에 치즈가 다 녹았으면 꺼낸다
                takeout, takeout_idx = fire.popleft()
                if N + i < M:
                    fire.appendleft([arr[N + i], N + i])
                    i += 1
                else:
                    fire.appendleft([-1, -1])
        chk = 0
        for c in fire:
            if c[0] == -1:
                chk += 1
        if chk == N:
            break
    print(f'#{tc} {takeout_idx + 1}')
