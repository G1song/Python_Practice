import requests 
from bs4 import BeautifulSoup
import json

def best_seller_list():
    book_url =  'https://store.kyobobook.co.kr/api/gw/best/best-seller/online?page=1&per=20&period=001&dsplDvsnCode=000&dsplTrgtDvsnCode=001'

    r = requests.get(book_url)
    r.status_code
    r.text
    print(r.status_code)
    #print(r.text)

    d = json.loads(r.text)
    print(d.keys())
    d['bestSeller'][0]['cmdtName']
    for idx, book in enumerate(d['bestSeller']):
        idx += 1
        print(f"📙book {idx}: {book['cmdtName']}, {book['pbcmName']}")




best_seller_list()
   


    