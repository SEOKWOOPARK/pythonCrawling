from selenium import webdriver
import time

# 네이버 이동
browser = webdriver.Chrome("./chromedriver")
browser.get("http://naver.com")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# id 새로 입력
browser.find_element_by_id("id").clear() # 기존 입력 내용 지워주기
browser.find_element_by_id("id").send_keys("my_id")

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
browser.quit() # 브라우저 전체 종료
# browser.close() 현재 탭만
