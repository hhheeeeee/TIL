import json
from pprint import pprint


def artist_info(artist, genres_list):
    result = dict()
    result['id'] = artist.get('id')
    result['name'] = artist.get('name')
    result['images'] = artist.get('images')
    result['type'] = artist.get('type')
    result['genres_names'] = []
    for genres in genres_list:
        if  genres['id'] in artist.get('genres_ids'):
            result['genres_names'].append(genres['name'])
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
