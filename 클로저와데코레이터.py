# 클로저 : 함수 안에 내부 함수(inner function)를 구현하고 그 내부 함수를 반환하는 함수
# 콜백 함수를 사용하기 위해서도 호출 함
# def calc():
#     a = 3
#     b = 5
#     def mul_add(x):
#         return a * x + b
#     return mul_add      # 내부 함수 리턴
#
# c = calc()
# print(c(2), c(5), c(10))# 외부 함수의 변수 값을 기억하고 있음

import time
# def operation(x,y,callback):
#     result = 0
#     for e in range(x):
#         result += e + x + y
#         time.sleep(1)
#     callback(result)
#
# def callback(result):
#     print(f"실행 결과를 되돌력 받기 위한 콜백 함수 호출 : {result}")
#
# operation(10, 20, callback)


# 데코레이터 : 이미 만들어져 있는 함수의 앞이나 뒤에 기능을 추가할 때 사용
from datetime import datetime
def datetime_deco(func):
    def decorated():
        print(datetime.now())
        func()  # 어노테이션을 사용한 함수. 함수가 이 사이에 들어가 꾸며줌을 받는다.
        print(datetime.now())
    return decorated()

#datetime_deco이라는 데코레이터함수 사이에 데코레이터 어노테이션을 사용해서 함수를 넣어 어떠한 꾸며주는 효과를 줌
@datetime_deco
def for_sum() :
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)

for_sum()

