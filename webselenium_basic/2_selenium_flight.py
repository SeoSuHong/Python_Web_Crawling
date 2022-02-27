from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(r"C:\Users\Seo Su Hong\Desktop\IT\Python\Web\webselenium_basic\chromedriver.exe")
browser.maximize_window() # 창 최대화

url = "https://m-flight.naver.com/"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_class_name("tabContent_option__2y4c6").click()
# clsaa_name이 "tabContent_option__2y4c6 select_Date__1aF7Y" 이지만 select_Date__1aF7Y 를 입력하면 안됨
# select_Date__1aF7Y 는 class명이 아니라 class 내의 하나의 옵션이라 그런거 아닐까..?

try:
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[6]/button/b")))
except Exception:
    browser.quit()

# 일정 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td[6]/button/b").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button/b").click()

# //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[5]/button/b    --> 2월 17일
# //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button/b    --> 2월 25일
# //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button/b    --> 2월 26일
# //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[6]/button/b    --> 3월 25일

# 여행지 선택
browser.find_elements_by_class_name("select_code__d6PLz")[1].click()
browser.find_elements_by_class_name("autocomplete_Collapse__tP3pM")[0].click()
browser.find_elements_by_class_name("autocomplete_location__TDL6g")[1].click()

browser.find_element_by_class_name("searchBox_txt__3RoCw").click()


try:
    elem = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div")))
    # 성공했을 때 동작 수행
    print(elem.text) # 첫 번째 결과 출력
finally:
    browser.quit()

# 15초 동안 브라우저는 XPATH에 "경로"가 있는지 기다리다가 있다면 동작 수행, 없다면 오류 출력
