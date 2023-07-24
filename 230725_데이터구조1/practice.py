#####################################

# 1. 문자열 a 에서 'e'의 개수 세기
a = 'eeeiiiaaaiiieee'
print(a.count('e'))

# 2. 문자열 a 에서 'i'의 위치 찾기(2가지)
a = "aippleii"
print(a.find('i'))
print(a.index('i'))

print(a.find('z'))  # -1
# print(a.index('z'))  # error

# 3. 문자열 a의 문자 사이에 . 삽입
a = 'apple'
print(".".join(a))

# 4. 문자열 a를 공백 기준으로 분리하여 출력
a = ' a p p l e'
print(a.split())

# 5. 문자열 a에서 'makes'를 'made'로 바꿔서 출력
a = 'she makes a cake'
print(a.replace('makes', 'made'))

# 반환하지 않는 메소드
# 6. 문자열 a를 대문자와 소문자로 변환하여 출력
a = 'lower UPPER'
print(a.swapcase())

# 7. 문자열 a에서 양쪽 공백 삭제하기
a = '    clear blank    '
print(a.strip())

###########################
# 리스트
# 반환하지 않는 메소드(Void methonds) -> 주로 원본 변경
# 1. 리스트 a의 마지막에 'a'추가, a출력
a = [1, 2, 3]
a.append('a')
print(a)

# 2. 리스트 a를 내림차순으로 정렬, a출력
a = [2, 6, 4, 7, 4, 7]
a.sort()
print(a)

a = [2, 6, 4, 7, 4, 7]
print(sorted(a))  # [2, 4, 4, 6, 7, 7]
print(a)  # [2, 6, 4, 7, 4, 7]

# 3. 리스트 a를 오름차순으로 정렬, a출력
a = [2, 6, 4, 7, 4, 7]
a.sort(reverse=True)
print(a)
# 4. 리스트 a를 역순으로 뒤집기, a출력
a = [1, 2, 3, 4, 5, 6, 7]
a.reverse()
print(a)  # [7, 6, 5, 4, 3, 2, 1]

# 5. 리스트 a에서 문자 'a'삭제하기, a출력
a = ['a', 'p', 'p', 'l', 'e']
a.remove('a')
print(a)  # ['p', 'p', 'l', 'e']

# 반환값이 있는 메소드(Return Methods) -> 주로 원본 변경 X
# 6. 리스트 a의 마지막 요소 꺼내서 삭제하고 변경된 리스트 출력
a = [1, 2, 3, 4, 5]
print(a.pop())  # 5
print(a)  # [1, 2, 3, 4]

#  7. 리스트 a에서 문자 'n'의 개수를 출력
a = ['b', 'a', 'n', 'n', 'a']
print(a.count('n'))  # 2
