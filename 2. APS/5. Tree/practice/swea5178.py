def make_tree(root):

    if root < N:
        make_tree(root * 2)
        make_tree(root * 2 + 1)
        h[root] += h[root * 2] + h[root * 2 + 1]



for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    h = [0] * (1000)
    for _ in range(M):
        key, value = map(int, input().split())
        h[key] = value
    make_tree(1)

    print(f'#{tc} {h[L]}')