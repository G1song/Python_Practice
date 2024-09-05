import requests 
from bs4 import BeautifulSoup

def crawl_breaking_news_list():
    news_url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0014907888'

    response = requests.get(news_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        td = soup.find('td', {'class' : 'content'})

        for li in td.find_all('li'):
            try:
                if li['data-comment'] is not None:
                    a = li.find('a')
                    link = a['href']
                    text = a.text
                    print(link, text)
            except KeyError:
                pass 


'''
크롤링시 requests.get(link) 크롬에서 엔터쳐서 페이지로 넘어가는 것
response.
find : 조건에 맞는 거 처음나오는애 찾아주기
findall : 조건에 맞는 거 전부 찾아주기 

''' 

def crawl_ranking_news():
    ranking_url = 'https://news.naver.com/main/ranking/popularDay.naver'

#http get 요청을 보내고 응답 받기
    response = requests.get(ranking_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    #언론사별 랭킹 뉴스 섹션 찾기 
    media_sections = soup.find_all('div', class_='rankingnews_box')
    
    #언론사별 top5 랭킹 뉴스 추출
    for section in media_sections:
        #언론사 이름 추출
        media_name = section.find('strong', class_='rankingnews_name').get_text(strip=True)
        print(f"❤️ 언론사 💙: {media_name}")

        #각 언론사의 뉴스 목록
        news_items = section.find_all('div', class_='list_content')

        # top5 뉴스 추출 및 출력

        for idx, item in enumerate(news_items[:5]):
            title = item.find('a').get_text(strip=True)
            link = item.find('a')['href']
            print(f"{idx + 1}. {title}")
            print(f"  링크: {link}")

        print('=.' * 50)
#strip = true 

        






if __name__ == '__main__':
    crawl_breaking_news_list()
    crawl_ranking_news()