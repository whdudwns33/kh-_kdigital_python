# 파이썬의 다양한 출력 방법
name = "용임릉"
age = 26
gender = "남성"
jobs = "에반"
addr = "헤네시스"

# c언서 스타일 출력: 서식지정자를 사용하는 방식
print("="*5, "c 스타일 ", "="*5)
print("이름 :%s"%(name))
print("나이 :%d"% age)
print("성별 :%s"%(gender))
print("직업 :%s"%(jobs))
print("주소 :%s"%(addr))

# 파이썬 스타일 1 : 3.6 이전 방법
print("="*5, "3.6이전 파이썬 스타일 ", "="*5)

print("이름 : {}".format(name)) # format에 지정한 변수를 {}에 입력
print("이름과 주소 : {} {}".format(name, addr))
print("용임릉 : {} {} {} {}".format(age, gender, jobs, addr))

# 파이썬 스타일 2 : 3.6 이후 방식. f와 {} 사용해서 출력하는 방식
print("="*5, "3.6이후 파이썬 스타일 ", "="*5)
print(f"이름 : {name}")   # f"  {변수}"
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"직업 : {jobs}")
print(f"주소 : {addr}")

# 자바 스타일
print("="*5, "자바 스타일 ", "="*5)
print("이름 :" + name)
print("나이 :" + str(age)) # 데이터형이 다르기 때문에 age를 형변환 해야함
print("주소 :" + addr)

print()
# 출력시 정렬하기
# < 좌측 정렬
# > 우측 정렬 : 생략 가능함
# ^ 중앙 정렬
print("|{:>5}|".format("변수")) #우측 정렬, 오른 쪽으로 5칸.
print("|{:<5}|".format(10)) #좌측 정렬
print("|{:^6}|".format(10)) #중앙 정렬. 오른쪽 3칸 왼쪽 3칸

print(f"|{10:>5}|")         #우측 정렬
print(f"|{10:<5}|")         #왼쪽 정렬
print(f"|{10:^6}|")         #중앙 정렬

PI = 3.14159265
print(f"{PI:.2f}")  #.(n)f n= 자연수, 소숫점 n번째까지 출력

