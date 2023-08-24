import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# M개의 곱이 최소값이 되기 위해 선택해야 하는 패의 종류
def dvc(start, r, N):
    global res
    global res_lst

    if len(temp) == M:
        if r < res:
            res = r
            res_lst = temp[:]
        return

    for card in range(start, N):
        temp.append(arr[card])
        dvc(card+1, r * arr[card], N)
        temp.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
temp = []
res = 1000000
dvc(0, 1, N)
print(*sorted(res_lst))
