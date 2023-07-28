import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def recommendation(track, artist, genre):
    # search API 문서: https://developer.spotify.com/documentation/web-api/reference/search
    URL = 'https://api.spotify.com/v1'

    headers = getHeaders()
    params = {
        'q': f'track:{track}',  # 필수 파라미터
        'type': 'track',     # 필수 파라미터
        'market': 'KR',
        'limit': 10
    }

    params1 = {
        'q': f'artist:{artist}',  # 필수 파라미터
        'type': 'artist',     # 필수 파라미터
        'market': 'KR',
        'limit': 10
    }

    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json().get('tracks').get('items')

    response1 = requests.get(f'{URL}/search', headers=headers, params=params1)
    response1 = response1.json().get('artists').get('items')

    track_id = 0
    artist_id = 0

    try:
        for item in response:
            track_id = item['id']
        for item in response1:
            artist_id = item['id']
    except:
        return

    params2 = {
        'seed_artists': artist_id,  # 필수 파라미터
        'seed_genres': genre,     # 필수 파라미터
        'seed_tracks': track_id,     # 필수 파라미터
        'market': 'KR',
        'limit': 10
    }
    response2 = requests.get(
        f'{URL}/recommendations', headers=headers, params=params2)
    response2 = response2.json().get('tracks')
    result = []
    for item in response2:
        result.append(item['name'])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('HypeBoy', 'BTS', 'acoustic'))
    # ['Best Of Me', 'A Drop in the Ocean', 'We Are', 'Dear Mr. President', 'Hurt']
