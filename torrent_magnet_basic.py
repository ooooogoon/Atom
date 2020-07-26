
import requests
from bs4 import BeautifulSoup

header = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
keyword = "윈도우10"
url = "https://www.google.com/search?sxsrf=ALeKk00kn3IPDSvepAA2dUuswRmK7r834w%3A1594643247493&ei=L1MMX9PUHZXZ-QaZNQ&q={}+torrent&{}+torrent".format(
    keyword, keyword)
r = requests.get(url, headers=header)
bs = BeautifulSoup(r.content, "lxml")
divs = bs.select("div.g")  #select 리스트를 리턴

magnets = []

for d in divs:
    alink = d.select("div.r > a")[0]
    title = alink.select("h3")[0].text
    href = alink.get("href")

    r = requests.get(href)
    bs = BeautifulSoup(r.content, "lxml")
    all_links = bs.select("a")

    for a in all_links:
        g_link = a.get("href")
        if g_link is None:
            continue
        if g_link.find("magnet:?") >= 0:
            magnets.append({
                "title": title,
                "href": href,
                "magnet": g_link,
            })

print(magnets)

## 현재 페이지만 크롤링...
