# 산술 연산자 : 사칙연산자. (+ - * /) // : 몫을 구하기, ** : 제곱 연산자, % : 나머지 연산자
i = 10 # 파이썬은 값을 대입할 때 데이터 형이 결정됨. 파이썬은 데이터형을 선언하지 않음.
j = 3
print(f"덧샘: {i+j}") #f를 넣어야 ""안에 변수를 삽입하겠다는 의미임. 없으면 그냥 문자열을 넣는 것일 뿐.
print(f"뺄샘: {i+j}")
print(f"곱샘: {i*j}")
print(f"나누기: {i/j}")
print(f"몫계산: {i//j}")
print(f"나머지: {i%j}")
print(f"제곱: {i**j}")
text = "python"
print(text + " hello")
print(text + " hello " + str(100)) # 숫자를 문자로 변환
print(text * 3) # 문자열 3번 반복


# 증감연산자 : 지원하지 않음. 오류남
# a = 10
# print(a--)
# a = 10
# print(--a)
# a = 10
# print(a++)
# a = 10
# print(++a)

#하지만
# i = i+1 # => i += 1
# print(f"증감연산자 : {i}") # 이거는 가능함
#
# # 간단 예제 : 파이썬에서 변수는 상수로 만들 수 없다. 관례상 대문자로 표기하여 상수로 간주.
# TAX_RATE = 0.10 # 파이썬은 상수 선언이 없기 때문에 대문자로 씀. 어떠한 관례처럼.
#                 # 그나마 상수 비슷하게 할 수 있는 것은 ():튜플을 사용하는 것.
# income = int(input("당신의 수입이 얼마입니까? "))
# print(f"당신이 내야 할 세금은 {income * TAX_RATE:.2f} 입니다.") # :.(n)f 는 소숫점 n자리 까지 출력

# 관계 연산자 : 기존의 자바에서 and(&&)는 파이썬에서 and로 바뀜. or(||) => or, not(!) = > not
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y  # 참과 거짓 으로 구성되어 있고 and는 둘다 참이어야 하므로 결과는 false
print(rst1)
# 자바에서는 조건에 1같이 정수를 넣을 수가 없고 x>y, true 정도만 된다.
# 하지만 파이썬은 비교적 자유롭다.
rst2 = x > 0 or x > y  # 둘중 하나만 true면 True
print(rst2)
rst3 =  not(x > 0 or x > y) # false
print(rst3)
print(rst1, rst2, rst3, sep="\t")


# 다항(삼항) 연산자
num = int(input("정수입력 :"))
rst = (num % 2 == 0) and "짝수" or "홀수" # 참이면 "짝수" , 거짓이면 "홀수", 람다식 :  e => (e % 2 == 0)  and "짝수" or "홀수"
print(f"{num} 은 {rst} 입니다. ")

# 2진수 입력받기 : 0b, 0과 1밖에 올 수 없음
number = 0b01
# 8진수 입력받기 : 0o, 0부터 7까지만
number = 0o01234567
# 16진수 입력받기 : 0x, 0123456789abcdef
number = 0xffffff


