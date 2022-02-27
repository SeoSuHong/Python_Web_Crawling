from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windows-siza=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

browser = webdriver.Chrome(r"C:\Users\Seo Su Hong\Desktop\IT\Python\Web\webselenium_basic\chromedriver.exe", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/98.0.4758.102 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# headless로 user-agent를 찍어내면 headless chrome으로 뜸
# headless를 막는 페이지에서는 접속이 불가능
# options.add_argument에 user-agent를 입력하면 해결
