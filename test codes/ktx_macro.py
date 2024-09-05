import asyncio
from playwright.async_api import async_playwright
from time import time, sleep 


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await browser.new_page()
        await page.goto('https://www.letskorail.com/korail/com/login.do')
        login_id = await page.wait_for_selector('#txtMember.txt')
        await login_id.type('1577065670')
        # await page.evaluate('''
        #                 () => {
        #                     id_input = document.querySelector('input[id="txtMember"]');
        #                     id_input.value = '1577065670';
        #                 }''')
        login_password = await page.wait_for_selector('#txtPwd.txt')
        await login_password.type('sesac0905*')
        
        # login_button = await page.wait_for_selector('li[class="a.btn_login"]')
        login_button = await page.wait_for_selector('.btn_login')
        await login_button.click()

        await date_select(page, '부산', '서울')
        sleep(5)
        await schedule_select(page)
        # await page.goto('https://www.letskorail.com/ebizprd/EbizPrdTicketPr21111_i1.do')
        


async def date_select(page, departure, destination):
    go_start = await page.wait_for_selector('#txtGoStart.txt120')
    go_end = await page.wait_for_selector('#txtGoEnd.txt120')
    await go_start.fill(departure)
    await go_end.fill(destination)
    calendar = await page.wait_for_selector('#selGoStartDay.txt120')
    await page.evaluate('''
                () => {
                        id_input = document.querySelector('input[id="selGoStartDay"]');
                        id_input.value = '2024.9.20';
                    }''')
    select_time = await page.wait_for_selector('#time.select')
    # await page.evaluate('''
    #                     () => {
    #                     time_input = document.querySelector('select[id="time"]');
    #                     time_input.value = '16 (오후04)';
    #                     }''')

    hour_selection = await page.wait_for_selector('#time.select')
    await hour_selection.select_option(value='14')

    ticketing_button = await page.wait_for_selector('.btn_res')
    sleep(5) 
    await ticketing_button.click()

 

async def schedule_select(page):
    ktx = await page.wait_for_selector('#selGoTrainRa00')
    await ktx.click()

    await page.evaluate('() => {inqSchedule();}')
    sleep(5)
    # lookup_button = await page.wait_for_selector('javascript:inqSchedule()') #이거마자?? 
    # 응그거당연히 아니고~~ inqSchedule() 얘를 콘솔창에서 쓰고 엔터하면 바로 클릭실행됨.

    booking = await page.wait_for_selector('javascript:infochk(2,0)') 
    payment = await page.wait_for_selector('#btn_next.btn_blue_ang')
    
    await lookup_button.click()
    await booking.click()
    # await payment.click()


    
#26번 date_select함수가 정의되기 전인데 저게 왜 실행되는거? 
#calendar변수는 안쓰이는뎅... evaluate 에서안쓰이는게 맞는거?
#왜 어떤건 fill 이 되고 어떤 건 안되지 기준이뭐지? 
# 42,43 줄에서 id_input 에서 id 는 내가 그냥 지정한거? 태그랑 상관없이?  
# 49번 시간안바뀌어요ㅠㅠ 
# 53번 ktx 클릭이 안돼요ㅠㅠ 
#4시 이후 가장 빠른 표로 혹은 시간 지정도 가능한지?? 예를들어 4-6시 사이에 있는 표만! 






if __name__=='__main__':
    asyncio.run(main())
