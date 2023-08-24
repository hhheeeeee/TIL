import heapq
n = int(input())
k = list(map(int, input().split()))
ugly = []
heap = [1]

heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)

while len(ugly) < max(k):
    n = heapq.heappop(heap)
    if n not in ugly:
        ugly.append(n)
        heapq.heappush(heap, n * 2)
        heapq.heappush(heap, n * 3)
        heapq.heappush(heap, n * 5)
for i in k:
    print(ugly[i-1], end=' ')