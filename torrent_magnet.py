import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import render_template_string
from flask import request

app=Flask(__name__)

def search_magnet(keyword):
  if keyword is None:
    return []

  header = {
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
  }
  # keyword = "윈도우10"
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

  return magnets

## 현재 페이지만 크롤링...

@app.route("/", methods=["GET", "POST"])
def index():
  if "keyword" in request.form:
    keyword=request.form["keyword"]
  else:
    keyword = None
  magnets = search_magnet(keyword)


  if len(magnets) > 0:
    HTML='''
    <form name="form" method="POST" action="/">
      <input type="text" name="keyword" value="">
      <input type="submit">
    </form>

    {% for m in magnets %}
    <li><a href="{{m.magnet}}" target="_blink">{{m.title}}</a></li>
    {% endfor %}
    '''
    return render_template_string(HTML, **{"magnets": magnets})
  else:
    HTML='''
    <form name="form" method="POST" action="/">
      <input type="text" name="keyword" value="">
      <input type="submit">
    </form>
    <p>검색 결과가 없습니다.</p>
    '''
    return render_template_string(HTML)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5678, debug=True)
