for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    h = [0] * 1000000
    last = 0
    for i in range(N):
        last += 1
        h[last] = arr[i]
        c = last
        p = last // 2
        while p > 0 and h[p] > h[c]:
            h[p], h[c] = h[c], h[p]
            c = p
            p = c // 2
    res = 0
    while N > 0:
        res += h[N // 2]
        N //= 2
    print(f'#{tc} {res}')