def DFS(idx, now_sum):
    global min_sum
    if now_sum >= min_sum:
        return
    if idx == N:
        if min_sum > now_sum:
            min_sum = now_sum
            return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            DFS(idx + 1, now_sum + arr[idx][i])
            used[i] = 0


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = 21e8
    DFS(0, 0)
    print(min_sum)
