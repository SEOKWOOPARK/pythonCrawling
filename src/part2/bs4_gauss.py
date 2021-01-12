import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status() 

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs = {"class" : "title"})
title = cartoons[3].a.get_text()
link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link) 

for c in cartoons:
	title = c.a.get_text()
	link = "https://comic.naver.com" + c.a["href"]
	# print(title, link)

webtoons = soup.find_all("div", attrs = {"class" : "rating_type"})
totalRates = 0

for w in webtoons: # 평점 다 불러온다
	rate = w.find("strong").get_text()
	print(rate)
	totalRates += float(rate)

print("총점: ", totalRates)
print("평균: ", totalRates / len(webtoons))




