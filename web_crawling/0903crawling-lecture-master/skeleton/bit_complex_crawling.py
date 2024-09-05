
import requests 
from bs4 import BeautifulSoup

from time import time 
import os
import pickle 

def crawl_press_names_and_codes():
    """Make the dict that have press code as key, and press name as value. Crawl from https://media.naver.com/channel/settings. 
    """

    begin = time()
    url = 'https://media.naver.com/channel/settings'
    code2name = {}
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        for li in soup.find_all('li', {'class': 'ca_item _channel_item'}):
            press_name = li.find('div', {'class': 'ca_name'}).text
            press_code = li['data-office']
            code2name[press_code] = press_name 

            # print(press_code, press_name)
    end = time()
    print(end - begin)
    return code2name 

def crawl_journalist_info_pages(code2name):
    """Accepts press code - press name dict, and return dict having press code as key, and 2-tuple of (press name, listof 2-tuple containing journalist name and their link) as value. 

    For now, you DO NOT have to crawl all journalists; for now, it's impossible. 
    Crawl from https://media.naver.com/journalists/. 
    """
    begin = time()
    res = {}
    
    for press_code, press_name in code2name.items():
        url = f'https://media.naver.com/journalists/whole?officeId={press_code}'

        response = requests.get(url)

        journalist_list = []
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            for li in soup.find_all('li', {'class' : 'journalist_list_content_item'}):
                info = li.find('div', {'class' : 'journalist_list_content_title'})
                a = info.find('a')
                journalist_name = a.text.strip(' ������')
                journalist_link = a['href']
                journalist_list.append((journalist_name, journalist_link))

        res[press_code] = (press_name, journalist_list)
    
    end = time()

    print(end - begin)
    return res 

class Journalist:
    def __init__(self, name, press_code, 
                career_list, 
                graduated_from, 
                no_of_subscribers, 
                subscriber_age_statistics, 
                subscriber_gender_statistics, 
                article_list):
        self.name = name 
        self.press_code = press_code 
        self.career_list = career_list
        self.graduated_from = graduated_from
        self.no_of_subscribers = no_of_subscribers
        self.subscriber_age_statistics = subscriber_age_statistics
        self.subscriber_gender_statistics = subscriber_gender_statistics
        self.article_list = article_list 


def crawl_journalist_info(link):
    """Make a Journalist class instance using the information in the given link. 
    """
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        profile_head = soup.find('div', {'class' : 'media_reporter_basic_text'})

        press_code = profile_head.find('a')['href'].split('/')[-1]   
        journalist_name = profile_head.find('hw', {'class' : 'media_reporter_basic_name'}).text

        print(press_code, journalist_name)

        award_div = soup.find('div', {'class':'media_reporter_profile_award'})

        for award in award_div.find_all('div', {'class' :  'media_reporter_profile_award'}): 
            award_category = award.find('h4', {'class' : 'media_reporter_award_category'}).text
            award_list = award.find('ul', {'class' : 'media_reporter_award_list'})

            award_lst = []

            for award_item in award_list.find_all('li', {'class' :'media_reporter_award_item'}):
                award_year = award_item.find('em', {'class': 'media_reporter_award_year'}).text.strip()
                award_name = award_item.find('ul', {'class': 'media_reporter_award_name'}).text.strip()
                print('    ', award_year, award_name)
                award_lst.append((award_year, award_name))

            award_dict[award_category] = award_lst
        for k, v in award_dict.items():
            print(k)
            for e in v:print(e)

    return Journalist(name = journalist_name, career_list = award_dict, )






if __name__ == '__main__':
    code2info_pickle = 'code2info.pickle'

    # if code2info_pickle in os.listdir():
    # else: 

    crawl_journalist_info('https://media.naver.com/journalist/006/31564')


    if code2info_pickle in os.listdir():
        begin = time()
        code2info = pickle.load(open(code2info_pickle, 'rb'))    
        end = time()
        print(f'{end - begin} sec passed for unpickling')
    else:
        begin = time()
        code2name = crawl_press_names_and_codes()
        code2info = crawl_journalist_info_pages(code2name)
        pickle.dump(code2info, open(code2info_pickle, 'wb+'))
        end = time()
        print(f'{end - begin} sec passed for execution and pickling')

    # for code, (press_name, journalist_list) in code2info.items():
    #     for journalist_name, link in journalist_list:
    #         j = crawl_journalist_info(link)
    #         assert j.name = journalist_name

    