from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

wb = Workbook()

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#####################
# 여기에 코드 적기!
uls = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
ws1 = wb.active
ws1.title = "뉴스기사"
ws1.append(["제목", "url", "언론사", "썸네일"])
for ul in uls:
    title = ul.select_one('div.news_wrap.api_ani_send > div > a').text
    url = ul.select_one('div.news_wrap.api_ani_send > div > a')['href']
    comp = ul.select_one('a.info.press').text.split(' ')[0].replace('언론사', '')
    thumnail = ul.select_one('div.news_wrap.api_ani_send > a > img')['src']
    ws1.append([title, url, comp, thumnail])
wb.save(filename='news.xlsx')






#####################

driver.quit()