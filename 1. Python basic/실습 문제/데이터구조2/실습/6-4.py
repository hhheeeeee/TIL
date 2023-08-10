# ws_6_4.py

# 아래 함수를 수정하시오.
def get_keys_from_dict(my_dict):
    return [key for key in my_dict.keys()]

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)
