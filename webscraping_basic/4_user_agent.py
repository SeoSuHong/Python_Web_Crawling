import requests

url = "https://github.com/SeoSuHong"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()


with open("mygithub.html", "w", encoding="utf8") as f:
    f.write(res.text)
