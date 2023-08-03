import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def recur(start):
    global cnt
    if len(rs) == N:
        copy = rs[:]
        if sum(copy) == K:
            cnt += 1
        return
    
    for i in range(start, 13):
        if i not in rs:
            rs.append(i)
            recur(i+1)
            rs.pop()

T = int(input())
for testcase in range(1,T+1):
    N, K = map(int, input().split())
    cnt = 0
    rs = []
    total = []
    recur(1)
    print(f'#{testcase} {cnt}')
