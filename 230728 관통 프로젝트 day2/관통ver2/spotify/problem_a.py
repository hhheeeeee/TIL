import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_tracks():
    # search API 문서: https://developer.spotify.com/documentation/web-api/reference/search
    URL = 'https://api.spotify.com/v1'

    headers = getHeaders()
    params = {
        'q': 'genre:k-pop',  # 필수 파라미터
        'type': 'track',                  # 필수 파라미터
        'market': 'KR',
        'limit': 20
    }

    # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    # 파이썬에서 쓸 수 있도록 하기 위해 json() 메서드를 사용해 json 타입의 데이터를 파이썬의 자료형으로 변환한다.
    response = response.json()
    # response 구조는 위의 공식 문서에서 확인할 수 있다.
    items = response.get('tracks').get('items')
    result = []
    for item in items:
        result.append(item['name'])
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    장르가 k-pop인 음악트랙 20개 가져오기
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_tracks())
    """
    ['Cupid - Twin Ver.',
    'Take Two',
    'Like Crazy',
    'MONEY',
    'OMG',
    'Like Crazy',
    'Ditto',
    'Bite Me',
    'FLOWER',
    'UNFORGIVEN (feat. Nile Rodgers)',
    'Super',
    'Hype Boy',
    'The Planet',
    'Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack]',
    'Like Crazy (English Version)',
    'Cupid',
    'Run BTS',
    'Eve, Psyche & The Bluebeard’s wife',
    'Tally',
    'Spicy']
    """
