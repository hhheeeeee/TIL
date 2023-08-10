# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        
        get_name = input("이름을 입력하세요 : ")
        get_age = input("나이를 입력하세요: ")
        for i in get_age:
            if i not in ('1','2','3','4','5','6','7','8','9','0'):
                print('나이는 숫자로 입력해야합니다.')
                return
        self.user_data['name'] = get_name
        self.user_data['age'] = int(get_age)
        

    def display_user_info(self):
        if self.user_data:
            print('사용자 정보 :')
            print(f"이름 : {self.user_data['name']}")
            print(f"나이 : {self.user_data['age']}")
        else:
            print('사용자 정보가 입력되지 않았습니다.')


user = UserInfo()
user.get_user_info()
user.display_user_info()
