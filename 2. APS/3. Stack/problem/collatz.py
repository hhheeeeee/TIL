# 1. 어떤 수가 짝수라면 2로 나눈다
# 2. 어떤 수가 홀수라면 3을 곱하고 1을 더한다
# 3. 어떤 수가 1이 아니라면 1, 2를 반복한다.
# 위를 거치면 무조건 어떤 수던 1이 된다.
# 수가 주어지면 몇 번 거쳐야 1이 되는지

# import sys
# sys.setrecursionlimit(10**9)

def collatz(N):
    global cnt
    if N == 1:
        return
    if N % 2 == 0:
        cnt += 1
        collatz(N // 2)
    elif N % 2 == 1:
        cnt += 1
        collatz((N * 3) + 1)


N = int(input())

cnt = 0
collatz(N)
print(cnt)

#################################

def collatz(N, cnt):
    if N == 1:
        print(cnt)
        return
    elif N % 2 == 0:
        collatz(N // 2, cnt + 1)
    elif N % 2 == 1:
        collatz((N * 3) + 1, cnt + 1)

N = int(input())
collatz(N, 0)
