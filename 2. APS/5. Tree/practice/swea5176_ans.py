# 완전 이진트리 규칙, 부모 노드의 인덱스 : n
# 왼쪽 자식 노드의 인덱스 : 2n, 오른쪽 자식 노드의 인덱스 : 2n + 1
def make_BST(n):
    global node
    if n <= N: # n이 전체 노드 수 N보다 작거나 같을 때만
        make_BST(n*2)
        tree[n] = node
        node += 1
        make_BST(n*2 + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for i in range(N+1)]
    node = 1
    make_BST(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')