import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() # url 불러온 결과 체크

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) # 태그까지 출력
# print(soup.title.get_text()) # 태그 안의 문자들만 출력
# print(soup.a)
# print(soup.a.attrs) # 이벤트를 포함한 속성값들
# print(soup.a["href"])

a = soup.find("a", attrs = {"class" : "Nbtn_upload"})
# find => 해당하는 첫 번째 element 가져옴
b = soup.find("li", attrs = {"class" : "rank01"})
# print(b.a.get_text())

c = b.next_sibling.next_sibling
d = c.next_sibling.next_sibling
e = d.previous_sibling.previous_sibling
# print(d.a.get_text())
# print(e.a.get_text())
# print(b.parent) 부모 element

finding = b.find_next_sibling("li") # b 다음 나오는 li 출력
# print(finding.a.get_text())

allFinding = b.find_next_siblings("li") # 형제 element 싹다 찾기
# print(allFinding)

webtoon = soup.find("a", text="소녀의 세계-2부 37화")
print(webtoon)

