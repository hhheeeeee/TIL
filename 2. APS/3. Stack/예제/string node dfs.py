# 8개의 알파벳으로 구성된 문자열ㄷ과 대응되는 인접행렬을 입력받기
# 0번 알파벳으로부터 DFS로 노드들을 탐색하면서 출력해주세요
'''
RKFCVICM
0 1 1 1 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

출력예시
RKBIFCCM
'''

def dfs(n, V, adj_m):
    stack = []
    visited = [0] * (V + 1)
    visited[n] = 1          # 시작점 방문 표시
    print(arr[n], end = '')                # do[n]
    while True:
        for w in range(0, V):   # 현재 정점 n에 인접하고 미방문 w찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n) # push(v), v = w
                n = w
                print(arr[n], end = '')       # do(w)
                visited[n] = 1 # w 방문 표시
                break # for w, n에 인접인 w 찾은 경우
        else: #방문할 곳이 더이상 없다면 뒷걸음질
            # 스택에 지나온 정점이 남아있으면
            if stack:
                n = stack.pop() # pop()해서 다시 다른 w 찾을 갈림길 n준비
            else:
                # 스택이 비어 있으면 뒷걸음질쳐서 다른 갈림길 찾을 수 없음
                break   # while True 탐색 끝
    return

arr = input()
adj_m = [list(map(int, input().split())) for _ in range(8)]
dfs(0, 8, adj_m)