import numpy as np
import pandas as pd
import json

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

meta = pd.read_csv('/workspace/MovieSearch/mysite/static/movies_metadata2.csv', encoding='CP949')
meta = meta[['id', 'genres', 'title', 'original_language', 'vote_count', 'popularity', 'overview','tagline', 'runtime', 'vote_average']]

def parse_genres(genres_str):
    genres=json.loads(genres_str.replace('\'', '"'))

    genres_str=''
    for g in genres:
        genres_str += (g['name'])

    return genres_str

meta['genres']=meta['genres'].apply(parse_genres)

#meta = meta[meta['genres'].str.startswith('Thriller')] # 코미디로 시작하는 거 찾기, 즉 코미디가 장르임
meta = meta.sort_values(by=["vote_count","popularity"], ascending=[False, False])#투표득수 정렬->선호도 정렬

meta.to_csv("/workspace/MovieSearch/mysite/static/movies_search.csv", index=False)

meta.head()
print(meta)