import requests
from bs4 import BeautifulSoup

# 4D Max 상영스케줄 존재여부 체크하는 크롤러
inputUrl = input("원하시는 년도(4자리), 월, 일을 공백 하나 간격으로 입력하세요:")
day = str(inputUrl[0:4]) + str(inputUrl[5:7]) + str(inputUrl[8:]) # 원하는 날짜 입력받고 문자열 파싱해서 url 꼬리에 붙이기
url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=202&theatercode=0043&date=' + day
print(url)

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
fourD = soup.select_one('span.forDX')

if(fourD):
	fourD = fourD.find_parent('div', class_ = 'col-times') # find_parent => 부모 찾는 메서드
	title = fourD.select_one('div.info-movie > a > strong').text.strip()
	print('%s년 %s월 %s일에 4D 영화가 상영중입니다.' %(url[-8:-4], url[-4:-2], url[-2:]))
	print('상영중인 영화는 다음과 같습니다')
	print(title)
else:
	print('%s년 %s월 %s일에 4D 영화는 없습니다.' %(url[-8:-4], url[-4:-2], url[-2:]))



