import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import json
import pandas as pd

i = 2586 #2586부터 멈춤
for i in range(45462):

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    meta = pd.read_csv('/workspace/MovieSearch/mysite/static/movies_metadata_search.csv', encoding='UTF8')
    
    subscription_key = "8723311019d84791961586339c4086b0"
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    search_term = meta['title'][i]+' movie'
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}


    params  = {"q": search_term, "license": "all", "imageType": "photo", "aspect" : "tall"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    if search_results:
        with open('/workspace/MovieSearch/mysite/static/json_all/'+search_term+'.json' , 'w', encoding='utf-8') as make_file:
            json.dump(search_results, make_file, indent="\t")
    else:
        break
        
    #thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]
    #f, axes = plt.subplots(2, 2)
    #for i in range(2):
    #    for j in range(2):
    #        image_data = requests.get(thumbnail_urls[i+2*j])
    #        image_data.raise_for_status()
    #        image = Image.open(BytesIO(image_data.content))
    #        axes[i][j].imshow(image)
    #        axes[i][j].axis("off")

    #plt.show()
    print(i)
    print(search_term)
