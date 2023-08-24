def find_child(root):
    global cnt

    if len(graph[root]) == 2:
        cnt += 2
        find_child(graph[root][0])
        find_child(graph[root][1])

    if len(graph[root]) == 1:
        cnt += 1
        find_child(graph[root][0])



for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    line = list(map(int, input().split()))
    graph = [[] for _ in range(E + 2)]
    for i in range(E):
        graph[line[i*2]].append(line[i*2 + 1])
    cnt = 0
    find_child(N)
    print(f'#{tc} {cnt + 1}')