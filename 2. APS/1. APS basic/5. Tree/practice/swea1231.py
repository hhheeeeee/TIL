import sys
sys.stdin = open('1.txt')

def inorder(me):

    lchild = me * 2
    rchild = lchild + 1

    if me > N:
        return

    inorder(lchild)
    print(arr[me], end = '')
    inorder(rchild)


for tc in range(1, 11):
    print(f'#{tc} ', end = "")
    N = int(input())
    arr = [0]
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(N):
        line = list(input().split())
        arr.append(line[1])
    inorder(1)
    print()
