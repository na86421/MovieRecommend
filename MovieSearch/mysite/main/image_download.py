import urllib.request
import json
import pandas as pd

##코미디 다운로드에서 안되는 중 머임?
##아 특정사이트에서 다운로드 차단 발생;;

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

meta = pd.read_csv('/workspace/MovieSearch/mysite/static/sciencefiction.csv', encoding='CP949')

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

i = 0
for i in range(21):
    search_term = meta['title'][i]+' movie'
    with open('/workspace/MovieSearch/mysite/static/sciencefiction/'+search_term+'.json') as json_file:
        json_data = json.load(json_file)

        json_string = json_data["value"][0]["contentUrl"]
        print(json_string)

        urllib.request.urlretrieve(json_string, '/workspace/MovieSearch/mysite/static/sciencefiction/image/'+search_term+'.jpg')
