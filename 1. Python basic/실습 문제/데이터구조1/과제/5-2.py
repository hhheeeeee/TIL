# main.py

# 아래 함수를 수정하시오.
def count_character(sentence, char):
    cnt = 0
    for i in sentence:
        if i == char:
            cnt += 1
    return cnt

result = count_character("Hello, World!", "o")
print(result) # 2
