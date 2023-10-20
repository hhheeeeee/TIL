import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    # search API 문서: https://developer.spotify.com/documentation/web-api/reference/search
    URL = 'https://api.spotify.com/v1'

    headers = getHeaders()
    params = {
        'q': f'artist:{name}',  # 필수 파라미터
        'type': 'artist',     # 필수 파라미터
        'market': 'KR',
        'limit': 1
    }

    try:
        response = requests.get(f'{URL}/search', headers=headers, params=params)
        response = response.json()
        id = response.get('artists').get('items')[0].get('id')
        response1 = requests.get(f'{URL}/artists/{id}/related-artists', headers=headers)
        response1 = response1.json()
        result = []
        for artist in response1.get('artists'):
            result.append(artist['name'])
        return result
    
    except:
        return


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_related_artists('NewJeans'))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    pprint(get_related_artists('OldShirts'))
    # None
