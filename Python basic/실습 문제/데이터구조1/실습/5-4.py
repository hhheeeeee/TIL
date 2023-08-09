# ws_5_4.py

# 아래 함수를 수정하시오.
def capitalize_words(input_string):
    result = []
    input_list = input_string.split()
    
    for word in input_list:
        new_string = ""
        first_char = word[0]
        new_string += first_char.upper()
        for i in range(1, len(word)):
            new_string += word[i]
        result.append(new_string)
    
    return ' '.join(s for s in result)

result = capitalize_words("hello, world!")
print(result)