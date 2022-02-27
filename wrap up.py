# Web Scraping

###########################################################

# HTML (뼈대)

# <html>
#     <head>
#         <title>홈페이지</title>
#     </head>
#     <body>
#         <h1>어서오세요</h1>
#     </body>
# </html>

# CSS (예쁘게)
# JavaScript (살아있게)

###########################################################

# XPath (Element 의 경로)

# 특징(id, class, text)의 경로를 알려줌

# <button id="search_btn"
#         type="submit"
#         title="검색"
#         class="btn_submit">

# XPath _-> //*[@id="search_btn"]
# XPath 전체 경로 --> /html/body/div[2]/div[1]/div[1]/div/div[3]/form/fieldset/button

# Element 간의 관계

# <부모>
#     <자식/>
#     <자식/>
#     <자식/>
# </부모>

###########################################################

# 정규식 (규칙을 가진 문자열을 표현하는 식) (3_re.py 참조)
# ex) 주민등록번호, 이메일 주소, 차량 번호

# . (ca.s) : 하나의 문자 ex) case, cage, cake ...
# ^ (^de) : 문자열의 시작 ex) desk, destination ...
# $ (se$) : 문자열의 끝 ex) base, case ...

# match() : 처음부터 일치하는지
# search() : 일치하는 게 있는지
# findall() : 일치하는 것 모두 [리스트]로

###########################################################

# User-Agent (4_user_agent.py 참조)
# 어떤 페이지를 보여줄까?
# 사람이 맞는가?

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}

###########################################################

#          Requests                    Selenium

#   웹 페이지(html) 읽어오기         웹 페이지 자동화
#           빠르다                        느리다
#       동적 웹 페이지 X              동적 웹 페이지 O
#                  \                      /
#                   \                    /
#                       BeautifulSoup
#                원하는 데이터 추출 (웹 스크래핑)

# Requests (2_requests.py 참조)
# 주어진 url을 통해 받아온 html에 원하는 정보가 있을 때
# res.raise_for_status() : 주소 접속에 문제가 있을 시 오류 발생

# Selenium (1_selenium.py 참조)
# 로그인, 어떤 결과에 대한 필터일 등 어떤 동작을 해야 하는 경우
# !!! 크롬 버전에 맞는 chromedriver.exe가 반드시 있어야 함 !!!

# find_element(s)_by_id
# find_element(s)_by_class_name
# find_element(s)_by_link_text
# find_element(s)_by_xpath

# click()
# send_keys(), clear()

###########################################################

# Selenium 로딩 기다리기 (2_selenium_flight.py 참조)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# try:
#     elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@ID='CONTENT']")))
#     성공했을 때 동작 수행
#     pass
# finally:
#     browser.quit()

###########################################################

# Selenium 스크롤 내리기 (4_selenium_movies_scroll.py 참조)

# import time
# interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
# prev_height = browser.execute_script("return document_body.scrollHeight")

# 반복 수행
# while True:
#     # 스크롤을 가장 아래로 내림
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#     # 페이지 로딩 대기
#     time.sleep(interval)

#     # 현재 문서 높이를 가져와서 저장
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if curr_height == prev_height:
#         break

#     prev_height = curr_height

###########################################################

# BeautifulSoup (5_bs4.py 참조)

# find                       조건에 맞는 첫 번째 element
# find_all                   조건에 맞는 모든 element 리스트로
# find_next_sibling(s)       다음 형제 찾기
# find_previous_sibling(s)   이전 형제 찾기

# soup["href"]    속성
#soup.get_text()  텍스트

###########################################################

# 이미지 다운로드 (10_daum_movies.py 참조)

# with open("파일명", "wb") as f:
#     f.write(res.content)

# CSV (11_csv_stock.py 참조)

# import csv

# f = open(filename, "w", encoding="utf-8-sig", newline="")

###########################################################

# Headless Chrome (6_headless_chrome_useragent.py 참조)

# 브라우저를 띄우지 않고 동작
# 때로는 User-Agent 정의 필요

# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("windows-siza=1920x1080")

###########################################################

# !!! 막 쓰면 안됩니다. !!!

# 무분별한 웹 크롤링 / 웹 스크래칭은 대상 서버에 부하
# -> 계정 / IP 차단

# 데이터 사용 주의
# -> 이미지, 텍스트 등 데이터 무단 활용 시 저작권 등 침해 요소, 법적 제재

# robots.txt
# -> 법적 효력 X, 대상 사이트의 권고
