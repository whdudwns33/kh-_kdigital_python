# 함수란 특별한 목적을 수행하기 위한 독립적인 설계 프로그램.


# 이름, 주소, 전화번호를 매개변수로 전달받아 출력하는 함수
# def name_card(name, addr, phone):
#     print(f"\n"
#           f"주소 : {addr} \n"
#           f"번호 : {phone} \n"
#           f"이름 : {name} \n"
#           f"대륙 : VI")   # 회사 부분은 공통점
#
# # 함수는 선언 이후 호출 해야만 동작을 한다.
# # 한번 만들어진 함수를 여러번 호출하여 반복 수행이 가능함. 또한 반복 수행하면서 코드를 줄일 수 있음.
# name_card("전사","페리온","001")
# name_card("궁수","헤네시스","002")
# name_card("마법사","엘레니아","003")
# name_card("도적","커닝시티","004")
#
#
# 순차검색
# def search_list(a,x):
#     for i in range(len(a)):
#         if x == a[i]:
#             return i
#     return -1
#
# v = [17,18,19,92,33,58,7]
# print(search_list(v, 33))
# print(search_list(v, 18))
# print(search_list(v, 7))
# print(search_list(v, 100))
#
# # 기본값 인자: 함수 선언 시 매개변수에 대해서 기본값을 정의 할 수 있습니다.
# # 매개변수에 기본값이 정의 되어 있는 경우 함수호출 시 인자값을 넣지 않으면 기본값을 호출 함.
# def pofile(name, year = 2, age = 18, school = "태양고"):# name은 default값이 없으니까 무조건 입력해야함. 나머지는 defauit값이 있음
#     print(f"이름 : {name}, 학교 : {school}, 학년{year}, 나이 : {age}")
#
# pofile("나희도")
# pofile("고유림")
# pofile("백이진", "졸업", 22, "태양고 출신")

# 가변 매개변수 : 변수의 개수가 정해지지 않은 경우에 사용.
# *를 붙여 사용. 함수의 매개 변수를 몇개 입력하든 함수내에서 튜플로 인식. 패킹해서 입력됨

# def profile(name , age, *lang):
#     print(f"이름 : {name} 나이 : {age}", end= " ")
#     for e in lang :
#         print(e, end= ' ')
#     print()
#
# profile("나희도", 18, "고등학교", "자바", "파이썬", "C", "React")
# profile("유진초이", 28, "미군", "자바", "파이썬", "C++", "R")
# profile("정만월", 38, "델루나", "자바")


#지역 변수, 전역 변수
# sword = 10
# def game(player, sword):
#     sword -= player # 매개변수로 선언된 sword사용
#     print(f"남은 검 :{sword}")
#     return sword
#
# def game1(player):
#     global sword    # 전역에서 선언된 sword를 사용
#     sword -= player
#     print(f"남은 검 :{sword}")
#
#
# player = int(input("경기에 참여하는 노예가 몇명인가. :"))
# sword = game(player, sword)
# sword = game1(player)
# print(f"경기에 사용하고 남은 검 : {sword}")






