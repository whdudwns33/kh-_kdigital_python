# 람다란 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현한 것입니다.
# 파이썬에서 람다 함수를 통해 이름이 없는 함수를 만들 수 있습니다.
# 람다 함수의 장점은 코드의 간결함, 메모리 절약이라고 생각할 수 있습니다.


# def add(a, b):
#     return a + b
# print(add(1,2))
# print((lambda a, b : a + b)(1,2))


# 함수의 매개변수를 함수로 전달
# def call_times(func) :  # 매개변수에 함수를 선언할 수 있음
#     for i in range (10) :   # 10번 반복
#         func()              # 매개변수의 함수를 10번 반복
#
# def print_hello() :
#     print(f"hello ")
#
# call_times(print_hello)   # 함수에 매개변수를 함수로 선언


# filter() map()
# filter(함수, 리스트): 리스트의 요소를 함수에 넣고 리턴값이 True인 것으로 새로운 리스트를 구성
# map(함수, 리스트): 리스트의 요소를 함수에 넣고 새로운 리스트로 구성

#power 함수
# def power(n) :
#     return n * n

# 람다로 선언한 power
# power_lambda = lambda n: n * n

# in_ = [1,2,3,4,5]
# out_1 = list(map(power, in_))
# out_2 = list(map(power_lambda, in_))
# out_3 = list(map(lambda n: n * n, in_))   # 함수자리에 람다식으로 익명의 함수를 넣는 방법

# print(out_1)
# print(out_2)
# print(out_3)


# 리스트에 람다를 넣는 방법
my_list = [lambda a,b: a*b, lambda a,b: a+b]    # 0번째열은 곱셈, 1번쨰열은  덧셈
print(my_list[0](5,2))
print(my_list[1](5,2))






