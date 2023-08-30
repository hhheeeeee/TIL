# Union -> 두 그룹을 하나로 합친다
# find -> 특정 노드가 어느 그룹에 속해있는지 찾는다.

def find(node):
    if node != root[node]:  # 노드의 부모가 자기 자신이 아니라면
        root[node] = find(root[node])  # 부모 노드를 찾아간다 -> 경로 압축 수행
    return root[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if rank[root_x] > rank[root_y]:  # x의 랭크가 더 크다면 y의 부모를 x의 루트 부모로 설정
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:  # 만약 랭크가 같다면 y의 랭크 증가
            rank[root_y] += 1


N, Q = map(int, input().split())
rank = [0] * (N + 1)  # 각 노드의 랭크를 저장하는 리스트
root = [i for i in range(N + 1)]
for _ in range(Q):
    K, A, B = map(int, input().split())
    if K == 0:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')
    else:
        union(A, B)  # A와 B를 같은 그룹으로 연결
