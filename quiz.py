from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

url = "https://www.google.co.kr/?&bih=754&biw=1519&hl=ko" # 구글
browser = webdriver.Chrome(r"C:\Users\Seo Su Hong\Desktop\IT\Python\Web\webselenium_basic\chromedriver.exe")
browser.get(url) # 구글 접속

# 구글 이미지 클릭
browser.find_elements_by_class_name("gb_d")[1].click()

# '우왁굳' 검색 후 엔터
browser.find_element_by_name("q").send_keys("우왁굳")
browser.find_element_by_name("q").send_keys(Keys.ENTER)

# 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")


# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기 (2초)
    time.sleep(1)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        try:
            browser.find_element_by_class_name("mye4qd").click()
        except:
            break
    prev_height = curr_height

images = browser.find_elements_by_class_name("isv-r")
count = 1

for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = browser.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count+=1
    except:
        pass

while True:
    pass
