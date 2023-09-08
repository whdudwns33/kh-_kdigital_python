# 외장 함수: 파이썬이 기본적으로 제공하긴 하지만, import가 필요함
# random
import random
# randint(x, y): x이상 y 이하의 임의의 정수값 반환
# randrange(x, y): x이상 y미만의 임의의 정수값 반환

for i in range(10) :
    rand = random.randint(0, 4)
    print(rand)

for i in range(10) :
    rand = random.randrange(0, 4)
    print(rand)

# 현재 시간 불러오기
from datetime import datetime
#import를 하는데, datetime이라는 모듈에서 datetime의 함수를 불러오는 것이다.
#datetime은 운좋게 이름이 같은거지 다른 것임(파일명과 함수)을 주의할 것.
print(datetime.today())          # 현재 날짜 가져오기
print(datetime.today().year)     # 현재 년도 가져오기
print(datetime.today().month)    # 현재 월  가져오기
print(datetime.today().date())   # 현재 일자 가져오기
print(datetime.today().day)      # 현재 일  가져오기
print(datetime.today().hour)     # 현재 시간 가져오기
print(datetime.today().minute)   # 현재 분  가져오기


# 수학 계산을 위한 math
import math
print(math.sin(100))            # 사인
print(math.cos(100))            # 코싸인
print(math.tan(100))            # 탄젠트
print(math.log(100))            # 로그
print(math.log10(100))          # 로그10
print(math.ceil(100.5))         # 무조건 올림
print(math.floor(100.5))        # 무조건 내림





