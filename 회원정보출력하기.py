name = input("이름 :")
while True:
    age = int(input("나이 :"))
    if 0< age < 200 :
        age = age
        break
    else:
        print("다시 입력")

while 1:
    gen = input("남자: M,m 여자: F,f \n")
    if gen == "m" or "M":
        print("남자")
        break
    elif gen == "F" or "f":
        print("여자")
        break
    else:
        print("다시 입력")

while True:
    job = int(input("직업: [1]학생 [2]회사원 [3]주부 [4]무직 \n"))
    if job == 1:
        print("학생")
        break
    elif job == 2:
        print("회사원")
        break
    elif job == 3:
        print("주부")
        break
    elif job == 4:
        print("무직")
        break
    else:
        print("다시 입력")

print(f"정보:"
      f"이름:{name}\n"
      f"나이:{age}\n"
      f"성별:{gen}\n"
      f"직업:{job}\n")