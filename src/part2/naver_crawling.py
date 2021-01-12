import requests

res1 = requests.get("http://naver.com")
res2 = requests.get("http://google.com")
res1.raise_for_status() # html을 불러오지 못하면 바로 에러 출력
# print(res.status_code) # 200 => 정상적 요청, 403 => 접근 권한 없음

print(len(res1.text))
print(len(res2.text))

with open("mygoogle.html", "w", encoding = "utf8") as f:
	f.write(res2.text) # 쓰기모드로 mygoogle.html 파일 생성

