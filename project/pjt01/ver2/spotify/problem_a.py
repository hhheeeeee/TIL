import json
from pprint import pprint


def artist_info(artist):
    result = dict()
    result['id'] = artist.get('id')
    result['name'] = artist.get('name')
    result['genres_ids'] = artist.get('genres_ids')
    result['images'] = artist.get('images')
    result['type'] = artist.get('type')

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)
    
    pprint(artist_info(artist_dict))
