p = 'abcdabcef'
t = 'abcdabcdabcdabcef'


def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1)

    # preprocessing
    j = 0 # 일치한 개수 ==  비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j  # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    print(lps)

    #search
    i = 0 # 비교할 텍스트 위치
    j = 0 # 비교할 패턴 위치
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M:
            print(i - M, end = ' ')
            j = lps[j]

        print()
        return

kmp(t, p)