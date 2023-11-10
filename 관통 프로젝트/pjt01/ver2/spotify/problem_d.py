import json


def max_revenue(artists):
    maxpopularity = 0
    for artist in artists:
        artist_detail = json.load(
            open(f'data/artists/{artist["id"]}.json', encoding='utf-8'))
        if artist_detail['popularity'] > maxpopularity:
            maxpopularity = artist_detail['popularity']
            maxpopularartist = artist_detail['name']
    return maxpopularartist

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(max_revenue(artists_list))
