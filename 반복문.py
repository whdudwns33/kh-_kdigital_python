# 반복문: 조건이 참인 동안 계속 수행되는 제어문
# n = int(input("정수 입력 : "))
# s =0
# while n :   # 파이썬은 정수값이 0이 아니면 참으로 간주
#     s += n
#     n -= 1  # 파이썬에서는 증감연산자가 없음.
# print(s)

# while True :
#     age = int(input("나이를 입력 :"))
#     # if 0< age and age < 200: break #자바 방식
#     if 0< age < 200 : break
#     print("나이를 벗어났습니다.")


# for 문: for 요소 in 시퀀스. 시퀀스의 각 요소를 순회하는데 사용. (자바의 향상된 for문과 동일)
# fruits = ["apple", "banana", "cherry", ["다차원 배열", "korea"]] # 어떠한 2차원 배열. "~~"라는 문자'열'을 하나의 리스트 배열로 묶음
# print(fruits[3] [1] [0]) # fruits 리스트의 3번째열인 []리스의 1번째 열인 korea의 0번째열인 k
# for e in fruits :
#     print(e[0])
#
# str1 = "서울시 강남구 역삼동"
# for e in str1:
#     print(e, end="/")


# for 변수 in range(시작값, 종료값, 증감값):
# n = int(input("정수 입력 :"))
# s = 0
# for i in range(1, n+1,) : # 1부터 (n+1 미만까지->: n까지)
#     s += i # i를 계속 더함
# print(s)
#
# # for문 : 역순
# for i in range(10, 0 -1, -1) : # 0-1까지 가야만 0출력. -1씩 감소해야 역순으로 찍어냄. 10부터 0까지 출력
#     print(i, end= "\t")

# 이중 for문
# n = int(input("정수 입력 :"))
# for i in range (0, n) :
#     for j in range (0, n) :
#         print("*", end=" ")
#     print()

# 구구단 찍기
# for i in range (2, 10) :
#     for j in range (1, 10) :
#         print(f"{i} * {j} = {i*j}")
#     print()

# # 홀짝 나누기
# n = int(input("정수 :"))
# for i in range(0 , n) :
#     for j in range (0, n) :
#         if j % 2 == 0 : print("$", end= " \t")
#         else : print("*", end= " \t")
#     print()

# 사각형 찍기
# 정수값을 입력 받아 n*n 크기의 행렬 출력
# n = int(input("정수 :"))
# for i in range(1, n*n + 1) :
#     print(f"{i:^3}", end="\t")
#     if i % n == 1 :
#         print()  # 줄바꾸기

# 별찍기. 직각삼각형
# n = int(input("정수 :"))
# for i in range (n) :
#     for j in range  (i + 1) :
#         print("*", end= " ")
#     print()

# 별찍기. 직각삼각형(역순)
# n = int(input("정수 :"))
# for i in range (n, 0, -1) :
#     for j in range(i) :
#         print("*", end= " ")
#     print()
# 답
# n = int(input("정수 :"))
# for i in range (n) :
#     for j in range(n-i):
#         print("*", end=" ")
#     print()


# 별찍기. 직각삼각형(역순에 역방향?)
# # 답
# n = int(input("정수 :"))
# for i in range (n) :
#     for s in range(i) :
#         print(" ", end= " ")
#     for j in range(n-i) :
#         print("*", end=" ")
#     print()

# 별찍기 . 역삼각형
# n = int(input("정수 :"))
# for i in range(n, 0 , -1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()



# 문자 출력. 문자와 ASCII코드
#chr : 유니코드 값을 입력 받아 그 코드에 해당하는 문자를 출력.
#ord : 문자를 유니코드로 변환
# for i in range(ord("A"),ord("Z")+1): # A = 65,
#     print(chr(i), end=" ") # chr 문자 출력
# print()
#
# for i in range(65,91):#A:65 Z:90
# 	print(chr(i), end=" ")
# print()