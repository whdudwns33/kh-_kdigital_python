print("hello, world")   # 파이썬은 큰따옴표와 작은 따옴표를 구분하지 않음, 반면 자바는 구분함
print('hello, world')
print(100)
print(33.33)
print(100 + 23)

# 변수를 선언하고 값을 대입.
num = 100    # 데이터형은 값이 대입되는 순간 결정. 자바는 데이터형을 직접 지정해준 후 결정 Ex. int형은 스택메모리에 4바이트로 할당
num1 = "100" # 문자열.
print(num)
print(num1)
# print(num + num1) # 데이터 타입이 다르기 때문에 오류
num = "100"  # 다시 값을 지정할 수 있음
print(num + num1) # 데이터 타입이 같음

#특수문자는 _만 가능, 자바는 $, _ 가 가능.
#num = $100 # 안됨

# 변수활용
name = "마법사"
email = "@@"
age = 26
addr = "엘레니아" # 작은 따옴표도 사용 가능


## 범위 주석
"""
    여기는 범위 주석 구간입니다.
"""

# f""" ~~ """ 범위 입력 포메터
print (f"""
이름  : {name}
이메일 : {email}
나이  : {age}
주소  : {addr}
""")


# 파이썬은 boolean 값이 대문자로 시작한다.
# 나이 입력 받아서 20이상이면 retuen True.
# 파이썬은 들여쓰기 줄, 칸을 맞춰야 함.
isAdualt = True
if isAdualt :
    print ("나는 성인입니다.")
else :
    print("나는 성인이 아닙니다.")


### 잘 추가 되었나?
