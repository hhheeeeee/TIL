from collections import deque

def DSLR(now):
    d = int(now) * 2
    if d > 9999:
        d %= 10000
    d = str(d).zfill(4)

    if int(now) == 0:
        s = str(9999)
    else:
        s = str(int(now) - 1)
        s = s.zfill(4)

    l = now[1:] + now[0]
    r = now[-1] + now[:-1]

    return {'D': d, 'S': s, "L": l, "R": r}


def solve(S, G):
    q = deque([(S, "")])
    visited[int(S)] = True
    # result = []
    while q:
        now, passed = q.popleft()
        if now == G:
            return passed
        arr = DSLR(now)
        for key, value in arr.items():
            if not visited[int(value)] and key != S:
                visited[int(value)] = True
                q.append((value, passed + key))

for _ in range(int(input())):
    S, G = input().split()
    visited = [False] * 10000
    S = S.zfill(4)
    G = G.zfill(4)
    res = solve(S, G)
    print(res)