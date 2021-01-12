import requests
from bs4 import BeautifulSoup

# iframe 태그의 src 속성을 긁어온다.
url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=202&theatercode=0043&date=20210114'
html = requests.get(url)
# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
# print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(2) > div > div.info-movie > a > strong'))
# select_one => 웹상의 css 선택자를 하나만 갖고 온다.

# print(soup.select('div.info-movie'))
example = soup.select('div.info-movie')
# 배열형태로 넣는다.

for i in range(len(example)):
	print(example[i].select_one('a > strong').text.strip())

