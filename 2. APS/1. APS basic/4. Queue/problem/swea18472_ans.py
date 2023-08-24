N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    visited = [0] * 10000
    queue = [(A, '')]
    while queue:
        t, m = queue.pop(0)
        if t == B:
            break
        button = [
            ((t * 2) % 10000, 'D'),
            ((t + 9999) % 10000, 'S'),
            ((t % 1000) * 10 + (t // 1000), 'L'),
            ((t % 10) * 1000 + (t // 10), 'R')
        ]
        for (i, c) in button:
            if not visited[i]:
                queue.append((i, m+c))
                visited[i] = visited[t] + 1
    print(m)