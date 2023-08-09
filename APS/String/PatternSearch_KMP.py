p = 'AAAAA'
t = 'ABAAABAABACAABABAABACAABC'

def kmp(p, t):
    N = len(t)
    M = len(p)
    lps = [0] * M

    # preprocessing
    j = 0  # 일치한 개수 == 비교할 패턴 위치
    for i in range(1, M):
        # 수정된 부분: 패턴의 i와 j가 일치하지 않으면 j를 줄임
        while j > 0 and p[i] != p[j]:
            j = lps[j-1]
        if p[i] == p[j]:
            j += 1
            lps[i] = j  # 수정된 부분: lps[i]에 일치 길이를 할당
    print(lps)

    # search
    i = 0  # 비교할 텍스트 위치
    j = 0  # 비교할 패턴 위치
    while i < N:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:  # 패턴을 찾은 경우
            print(i - M, end=' ')
            j = lps[j-1]
    return


kmp(p, t)
