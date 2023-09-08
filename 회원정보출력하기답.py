# 회원정보 출력하기 ( 1단계는 현재상태대로 -> 2단계 함수로 바꾸기)
name = input("이름 :")
while True :
    age = (input("나이 :"))
    if age.isdigit() : # 입력 받은 문자열이 숫자로 구성되어 있는지 확인
        age = int(age)
        if 0 < age < 200 : break
    else : print("나이를 잘못입력하셨습니다. ")

while True:
    gender = input("성별 :")
    if gender == "M" or "m" or "F" or "f" : break
    print("성별이 잘못 입력되었습니다.")

while True :
    jobs = input("직업 :")
    if jobs.isdigit() :
        jobs = int(jobs)
        if 0 < jobs < 5 : break
    print("직업을 잘 못 입력하셨습니다.")

if gender == "M" or "m" :
    gen_str = "남성"
else :
    gen_str = "여성"

jobs_str = ("", "학생", "회사원", "주부", "무직")    # 고정된 정보를 출력하기 위함. 따라서 값이 변하지 않는 튜플을 사용. ()을 안써도 물론 튜플임.

print("="*3, "회원정보", "="*3)
print(f"""이름 : {name}
나이 : {age}
성별 : {gen_str}
직업 : {jobs_str[jobs]}
""")

# 함수형
name = input("이름 :")
def input_age() :
    age = (input("나이 :"))
    if age.isdigit() : # 입력 받은 문자열이 숫자로 구성되어 있는지 확인
        age = int(age)
        if 0 < age < 200 : return age
    print("나이를 잘못입력하셨습니다. ")

def input_gender() :
    while True :
        gender = input("성별 :")
        if gender == "M" or "m": return "남성"
        elif gender == "F" or "f" : return "여성"

def input_jobs() :
    while True:
        jobs = input("직업 :")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5: return jobs
        print("직업을 잘못 입력하셨습니다.")

def print_info() :
    print("=" * 3, "회원정보", "=" * 3)
    print(f"""이름 : {name}
    나이 : {age}
    성별 : {gen_str}
    직업 : {jobs_str[jobs]}
    """)

age = input_age()
gender = input_gender()






