# 값을 할당하는 방법
a = b = c = 1
print(a, b, c)
# 이게 되네;;
a,b,c = 1, False, "이름" # 여러개의 변수를 한번에 대입
print(a,b,c)
# 타입 확인
# age = input("나이를 입력하시오 : ")
# print(age)
# print(type(age))    # input은 기본적으로 문자열형임
# age = int(input("age를 입력하시오 : "))
# print(age)
# print(type(age))

# 숫자형 타입
# 0~~은 8진수, 0x~~ 16진수
value = 0o77 # 63
print(value)
value = 0xff # 255
print(value)

# boolean Type. bool() 참과 거짓의 값을 가짐.
print(bool(1)) # True
print(bool(0)) # False
print(bool(-100)) # True
print(bool("")) # False
print(bool(None)) # False. 값이 아직 정해지지 않음
val = None

# 문자열 타입:
name = "hello Python"
print(name)
print(name[0]) # 인덱싱. 배열의 첫번쨰
print(name[2:5]) # 2번 인덱스에서 5번 인덱스 미만까지
print(name[2:]) # 2번 인덱스부터 끝까지
print(name * 3) # str 3번 반복
print(name + " Test")

# 형변환 : 파이썬은 값이 할당되는 순간 형이 결정됨, 이후 데이터 형을 변경하고자 할 때, 형변환을 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(1 + 3.141592)
print(3 + 1.4 + float("3.333"))
print(3 + 1.4 + float("글자")) # 이건 안됨. "글자"는 숫자가 아님


