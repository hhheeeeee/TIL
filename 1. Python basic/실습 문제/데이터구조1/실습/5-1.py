# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(string):
    result = ""
    for i in range(len(string)-1 , -1, -1):
        result += string[i]
    return result

result = reverse_string("Hello, World!")
print(result)