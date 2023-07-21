import json


def dec_artists(artists):
    result = []
    for artist in artists:
        artist_detail = json.load(
            open(f'data/artists/{artist["id"]}.json', encoding='utf-8'))
        if int(artist_detail["followers"]["total"]) > 10000000:
            each = dict()
            each['name'] = artist['name']
            each['uri-id'] = artist['uri'].split(':')[2]
            result.append(each)
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
