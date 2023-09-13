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
# import math as m
# # print(math.sin(1))
# print(m.sin(1))
#
# # sys 모듈은 시스템과 관련된 정보를 가지고 있는 모듈입니다.
# import sys
# print("명령 줄 인수 :", sys.argv)
# print("실행 경로 :", sys.path)
# sys.stdout.write("Hello! \n")
# sys.stdout.write("Error \n")
# sys.exit(18) # 강제 종료. 숫자는 원하는 숫자를 넣으면 됨.

#os 모듈: operating system. 운영체제와 상호 작용하기 위한 기능을 제공(파일 시스템 접근, 환경변수 제어, 프로세스 관리 등)
import os
cwd = os.getcwd() # 현재 작업 디렉토리
print("현재 작업 디렉토리:", cwd)
# 디렉토리 생성
is_dir = os.path.isdir("test")
if not is_dir:  # 디렉토리 생성.
    os.mkdir("test")
is_file = os.path.isfile("score.txt")

os.system("dir")    # 터미널 커맨드 실행


