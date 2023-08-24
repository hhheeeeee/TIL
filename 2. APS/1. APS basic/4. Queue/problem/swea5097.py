import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력
    for _ in range(M):
        front = arr.pop(0)
        arr.append(front)
    print(f'#{tc} {arr[0]}')
