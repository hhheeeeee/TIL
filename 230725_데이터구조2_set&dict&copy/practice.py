# 실습1. 영어 단어를 입력하면 단어의 뜻을 보여주는 프로그램

vocab = {'plus': ['더하기', '장점'],
         'minus': ['빼기', '적자'],
         'multiply': ['곱하기', '다양하게'],
         'division': ['나누기', '분열'],
         }
# 실습 1 - 1
search = input("영어 단어를 입력하세요 : ")
print(vocab.get(search, "없는 단어입니다"))

# 실습 1 - 2
search = input("영어 단어를 입력하세요 : ")
try:
    print(vocab[search])
except:
    print("없는단어")

# 실습 1 -3
vocab.setdefault(input("영어 단어를 입력하세요 : "))  # 없는 단어면 None

# 실습 2. 단어들 목록을 보여주는 프로그램
print(list(vocab.keys()))

# 실습 3 - 1 단어 update
new_word = input("영어 단어를 입력하세요 : ")
meanings = list(input("뜻을 입력하세요 : ").split())
vocab[new_word] = []
for meaning in meanings:
    vocab[new_word].append(meaning)

for key, value in vocab.items():
    print(f"{key} : {value}")

# 실습 3 - 2 단어 update
new_word = input("영어 단어를 입력하세요 : ")
meanings = list(input("뜻을 입력하세요 : ").split())
vocab.update({new_word: meanings})
for key, value in vocab.items():
    print(f"{key} : {value}")

# 실습 4-1 입력받은 단어 지우기
word = input("지울 단어 입력 : ")
vocab.pop(word)  # 없는 단어 입력하면 KeyError
for key, value in vocab.items():
    print(f"{key} : {value}")

# 실습 4-2 입력받은 단어 지우기
word = input("지울 단어 입력 : ")
del vocab[word]  # 없는 단어 입력하면 KeyError
for key, value in vocab.items():
    print(f"{key} : {value}")
