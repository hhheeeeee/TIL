# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(input_list):
    even_numbers = []
    i = 0
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            even_numbers.extend([input_list.pop(i)])
        else:
            i += 1
    return even_numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

