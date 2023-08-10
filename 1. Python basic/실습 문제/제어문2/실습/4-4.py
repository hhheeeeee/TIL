# python -m pip install requests

import requests
from pprint import pprint as print

dummy_data = []
for i in range(1,11):
    # 무작위 유저 정보 요청 경로
    API_URL = "https://jsonplaceholder.typicode.com/users/" + str(i)
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    user = dict()
    if -80<float(parsed_data['address']['geo']['lat'])<80 and -80<float(parsed_data['address']['geo']['lng'])<80:
        user['company'] = parsed_data['company']['name']
        user['lat'] = parsed_data['address']['geo']['lat']
        user['lng'] = parsed_data['address']['geo']['lng']
        user['name'] = parsed_data['name']
        dummy_data.append(user)

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']
censored_user_list = dict()

def create_user(dummy_data):
    global censored_user_list
    for user in dummy_data:
        if censorship(user):
            company_name = user['company']
            user_name = user['name']
            censored_user_list[company_name] = []
            censored_user_list[company_name].append(user_name)
            print('이상 없습니다.')
    
    return censored_user_list
        
def censorship(user):
    if user['company'] in black_list:
        company_name = user['company']
        user_name = user['name']
        print(f'{company_name} 소속의 {user_name}은/는 등록할 수 없습니다.')
        return False
    return True


print(create_user(dummy_data))