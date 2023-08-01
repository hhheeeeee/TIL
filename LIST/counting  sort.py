
def counting_sort(arr):
    # 배열의 끝 값 알아야 하니까
    max_value = max(arr)
    # 카운트 저장할 리스트
    count_arr = [0] * (max_value + 1)

    for num in arr:
        count_arr[num] += 1

    sorted_arr = []
    for i, count in enumerate(count_arr): # 인덱스와 값을 쌍으로 반환
        sorted_arr.extend([i] * count) # iterable 추가
    
    return sorted_arr

arr = [4,4,4,4,4,3,3,3,3,2,2,2,1,0]
result = counting_sort(arr)
print(result)