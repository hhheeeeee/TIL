# 형변환
# 할당된 값 변경해서는 안됨
book = '1'
total = 10
guide = '현재 보유 중인 총 \033[4m'  + '책의' + '\033[0m 수는 다음과 같습니다.'
print(guide)
print(int(book) * total)

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
print(changes)
print(total - int(rental))
