# 인덱싱과 슬라이싱
id = "980612-1xx"
gender = id[7] # 성별
year = id[:2] # 2번째열 미만, 출생연도.
month = id[2:4] # 월
day = id[4:6]
print("생년월일 :" + id[:6])
print("뒷 자리 :" + id[7:])  # 7번째부터
print("뒷 자리 :" + id[-3:]) # 마지막 뒷자리부터 -1, -2, -3

if gender == "1" :
    print("남성")
else :
    print("여성")


a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
#a[1] = "L"  # 문자열 요소는 읽을 수 있지만 변경은 되지 않음. 리터럴 상수

# 대소문자 바꾸기
aa = "Hello Python Prigram.."
print(aa.upper()) # 실제 값이 바뀌지는 않음. upper로 대문자로 빠구어서 출력만 한 것.
bb = aa.upper()   # 새로운 변수에 저장해야 바꾼 값이 유지 됨
print(bb)
print(aa.lower)

# 문자열 변경 : replace("")
input_str = "hello Java"
new_str = input_str.replace("Java","Python")
print(new_str)

# 문자열에 포함된 문자 갯수 세기. 길이 세기
input_str2 = "hello Java"
print(input_str2.count("l")) # 문자열에서 count 매개변수의 갯수를 반환해줌.
print(len(input_str2)) # 문자열의 길이를 반환, 별도의 외부함수를 사용하는 방식
print(input_str2.__len__()) # .__~~__ 형식의 내부 함수 사용, .__len__은 문자열에 포함된 범용 함수
test = [1,2,3,4,5]
print(f"길이 {test.__len__()}")

# 문자열 찾기
# find(): 찾은 문자열의 첫번째 인덱스를 반환, 못찾으면 -1을 반환
# rfind(): 역순으로 찾지만 위치상 가장 처음에 나온 값을 출력. 
# index(): 찾은 문자열의 첫 번째 인덱스를 반환하고 못찾으면 ValueError
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장")) # 0번째 인덱스 출력
print(phrase.rfind("가장"))# 맨뒤에서 부터 34번째(정방향0번째) 인덱스 출력
print(phrase.index("포기"))
print(phrase.find("나에게")) # 못찾아도 에러가 나오지 않고 -1반환
# print(phrase.index("나에게"))# 못찾으면 에러가 나옴. value 에러

new_phrase = phrase.replace("가장", "나에게") # 한번에 모든 문자열 변경. 자바?의 replaceAll과 동일한 역할
print(new_phrase)

# 문자열 연산
print("태양고 " + "나희도")
print("태양고 " + str(2) + "학년")
print("안녕하세여"*2) # 해당 문자열을 반복 수행
print("안녕하세요", "!"*5, "\n", "\t", "high school", "="*3, "끝입니다.")
print()
# 문자열 앞,뒤 공백 제거 : strip()
input_aa = """
    안녕하세요.
문자열 함수를 알아봅시다.


"""
print(input_aa.strip())


