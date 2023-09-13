import requests     # 서버로 부터 정보를 요청하여 가져오기. get방식으로 가져오기
from bs4 import BeautifulSoup   # html parser. 규칙을 가지고 자르는 도구
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# html = requests.get(url).text
# print(html)
# soup = BeautifulSoup(html, "html.parser")    # 파싱, 어떠한 규칙으로 자름
# print(soup)

#날씨 정보 가져오기.
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# http get요청
res = requests.get(url).text
# html parssing
soup = BeautifulSoup(res, "html.parser")
# print(soup)

for loc in soup.select("location"):
    print("도시:", loc.select_one("city").string)
    print("날씨:", loc.select_one("wf").string)
    print("최저기온:", loc.select_one("tmn").string)
    print("최고기온:", loc.select_one("tmx").string)
    print("-"*20)
