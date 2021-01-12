import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() 

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a", attrs={"class" : "title"})
# find_all => a의 class="title"인 값들 모두 찾기

for c in cartoons:
	print(c.get_text())


