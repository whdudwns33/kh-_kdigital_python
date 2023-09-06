# 파이썬 입력
# 사용자의 입력을 받아 그 값을 프로그램해서 사용하고자 할 떄 input() 함수를 사용한다.
#기존의 자바에서 사용
#print("입력을 하세요 : ", end= " ")
#name = input()
#print(f"이름 : {name}")


# input() 함수를 통해서 압력받은 데이터는 문자열로 반환, 원하는 데이터형으로 반환이 필요
# name = input("이름을 입력을 하세요 : ")
# #print(f"이름 : {name}")
#
# age = int(input("나이를 입력하세요 : ")) # 나이를 정수형으로 받기 위힘
# print(type(age))                      # 데이터형 확인
# #print(f"당신의 나이는 {age} 입니다.")
#
# addr = input("주소를 입력하세요 :")
# jobs = input("직업을 입력하세요 :")
# score = float(input("성적을 입력하세요 :"))
#
# print(f"""당신의 정보 : {name}
#       {age}, {addr}
#       {score}, {jobs}
#       입니다. """)

# split() 함수는 기본적으로 공백을 기준으로 한다.
# str1, str2 = input("이름과 주소 입력 :").split() # 자바에서는 입력을 동시에 받을수가 없었음.
# print(str1, str2) # 공백기준으로 변수를 구분하는데, 만약 주소입력에 공백이 존재한다면 오류가 생김. ex 이름 (경기도 수원시): 오류 발생


#kor, eng, mat = map(int, input("국어 영어 수학 : ").split())
# val = list(map(int, input("성적입력 : ").split())) # input으로 문자열을 입력 받고 split으로 공백기준으로 구분하고 int형으로 반환하여 list에 대입
# print(val)

# hour, min, sec = input("시:분:초 :").split(":") # split은 기본값이 space이지만 ":"이런 식으로 값을 줄 수 있음
# print(f"{hour}시 {min}분 {sec}초")


#시간을 24시간제이며 :기준으로 입력받은 후   오전과 오후로 출력하도록 변경
hour, min, sec = map(int, input("시:분:초 :").split(":"))
if (hour > 12) :
    hour -= 12
    print(f"오후{hour:02}시{min:02}분{sec:02}")
else:
    print(f"오전{hour:02}시{min:02}분{sec:02}")