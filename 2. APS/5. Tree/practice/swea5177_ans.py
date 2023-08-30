import heapq
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = []
    number = map(int, input().split())
    for num in number:
        heapq.heappush(tree, num) # 힙에 num을 추가 -> 자동으로 정렬
    sumv = 0
    N = len(tree) // 2 # 부모의 노드 인덱스 계산
    while N:
        sumv += tree[N-1]
        N //= 2 # 부모 노드로 올라가기 위해  N // 2
    print(f'#{tc} {sumv}')