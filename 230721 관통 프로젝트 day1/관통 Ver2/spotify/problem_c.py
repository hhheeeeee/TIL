import json
from pprint import pprint

def new_artist(artist, genres):
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

def artist_info(artists, genres):
    result = []
    for artist in artists:
        result.append(new_artist(artist, genres))
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
