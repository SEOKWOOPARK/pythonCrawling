import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})
print(items[0].find("div", attrs = {"class" : "name"}).get_text())

for item in items:
	ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
	if ad_badge:
		print("광고 상품 제외")
		print('-----------------------------------')
		continue

	name = item.find("div", attrs = {"class" : "name"}).get_text() # 제품명
	
	if "Apple" in name:
		print("애플 제품 제외")
		print('-----------------------------------')
		continue

	price = item.find("strong", attrs = {"class" : "price-value"}).get_text() #제품 가격

	#리뷰 50개, 평점 4.5 이상
	rate = item.find("em", attrs = {"class" : "rating"}) # 제품 평점
	if rate:
		rate = rate.get_text()
	else:
		print("평점 없는 상품")
		print('-----------------------------------')
		continue
		
	rate_count = item.find("span", attrs = {"class" : "rating-total-count"}) # 평점 갯수
	if rate_count:
		rate_count = rate_count.get_text()
		rate_count = rate_count[1:-1] # 문자열에서 숫자만 슬라이싱
		print("리뷰 수", rate_count)
	else:
		print("평점 수 없는 상품")
		print('-----------------------------------')
		continue

	if float(rate) >= 4.5 and int(rate_count) >= 100:
		print(name, price, rate, rate_count)
		print('-----------------------------------')