from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? :')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome("C:/Users/ooooo/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6/chromedriver.exe")
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)


# class="LC20lb DKV0Md" 제목
# class="iUh30 bc tjvcx" 링크 class="TbwUpd NJjxre"
# 위 제목,링크 전부 class="r" 에 속해있음.

r = soup.select('.r')  # class 니깐 . 찍고 r
# print(type(r)) 이렇게 타입을 자주 보는게 좋음.
# print(r)
for i in r:
    print(i.select_one('.LC20lb.DKV0Md').text)
    # alink = i.find_element_by_tag_name('a').get_attribute('href')
    # href=alink.get("href")
    # print(alink.text)
    alink = i.select("div.r > a")[0]
    href = alink.get("href")
    print(href)

driver.close
