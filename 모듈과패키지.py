# import math # math 모듈을 불러들이기 위해서 import함
#
# print(math.sin(1))
# print(math.cos(1))
# import math
# # 모듈내에 함수들 중 특정 함수만 사용하기 위한 경우
# from math import sin,cos
# print(sin(1))
# print(cos(1))
# print(math.floor(1))
# import math
# 모듈을 가져 올 때 충돌이나 긴 이름을 간결하게 사용하기 위해 별칭 부여. 별칭을 부여하면 원래 이름은 사용할 수 없음
import math as m
# print(math.sin(1))
print(m.sin(1))

# sys 모듈은 시스템과 관련된 정보를 가지고 있는 모듈입니다.
import sys
print("명령 줄 인수 :", sys.argv)
print("실행 경로 :", sys.path)
sys.stdout.write("Hello! \n")
sys.stdout.write("Error \n")






