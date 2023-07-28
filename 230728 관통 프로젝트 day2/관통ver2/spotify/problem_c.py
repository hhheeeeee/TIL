import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def ranking():
    # search API 문서: https://developer.spotify.com/documentation/web-api/reference/search
    URL = 'https://api.spotify.com/v1'

    headers = getHeaders()
    params = {
        'q': 'genre:k-pop',  # 필수 파라미터
        'type': 'track',                  # 필수 파라미터
        'market': 'KR',
        'limit': 20
    }

    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    items = response.get('tracks').get('items')
    
    release_date = sorted(items, key=lambda track: track['album']['release_date'], reverse=True)
    result = []
    for date in release_date[:5]:
        result.append(date['album']['release_date'])
    return result



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    ['2023-06-09', '2023-05-22', '2023-05-12', '2023-05-08', '2023-05-01']
    """
