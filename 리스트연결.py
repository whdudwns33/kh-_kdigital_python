# # 리스트 연산자: 연결+ , 반복* , 길이len()
# list_a = [1,2,3,4]
# list_b = [5,6,7,8]
# print(list_a + list_b)
# print(list_a * 3)
# print(len(list_a + list_b))
#
# # 리스트 요소 추가하기 : append()리스트의 맨 마지막에 추가, insert(index, value) 해당 인덱스에 값 추가
# list_a = [1,2,3]
# list_a.append(4)
# list_a.append(5)
# list_a.insert(1, 10)
# print(list_a)
#
# #리스트 제거하기: pop() , remove(), clear(), del() 리스명[인덱스]
# # pop()스택에서 값을 끄집어 낸다. 인덱스가 없으면 마지막 인덱스를 반환하고 삭제, 인덱스가 있으면 해당 위치의 값을 삭제.
# a = [0,1,2,"가"]
# print(a)
# print(a.pop(3)) # 해당 인덱스의 값을 반환(보여줌)하면서 제거함.
# print(a)
# print(a.pop()) # 인덱스가 없으면 가장 마지막의 값 제거
# print(a)
# # remove(값): 해당하는 값을 제거, 만약 동일한 값이 여러개인 경우 낮은 인덱스값 제거
# b = [1,2,3,4,54,5,5,5,5,6,6,3,4,56,7,4,7,4,74,57,45,74]
# b.remove(5) # 해당 값을 제거만하고 반환하지는 않음.
# print(b)
# # clear() : 모든값을 삭제, 리스트 자체를 지우지 않음
# a.clear()
# b.clear()
# print(a)
# print(b)
# # 추가. 리스트에서 인덱스 값을 지우는 방법 del
# d = [0,1,2,3,4,5,6,7,8]
# del d[3]
# print(d)
# # 중복제거
# list = [1,2,3,4,5,5,6,7,8,9,1,2,3,4]
# new_list = []
# for e in list :
#     if e not in new_list:
#         new_list.append(e)
# print(new_list)

# map(반환함수, 입력자료형), filter(반환함수, 입력자료형) 동작확인하기.
# num = list(map(int, input().split())) # int도 함수 원래는 int()
# print(num)
# num1 = list(map(lambda e: int(e)*int(e) , input().split())) # int도 함수 원래는 int()
# print(num1)
# num1 = list(filter(lambda e: int(e) % 2 == 0 , input().split())) # int도 함수 원래는 int()
# print(num1)

# 리스트의 원소 스캔하기
x = ["jone", "goerge", "paul", "ringo"]
for e in x :                 #향상된 for문과 비슷한 형태. 요소값이 찍이는 것.
    print(e)

for i in range(len(x)):      #일반 for문, 범위기반 for문. (초기값,최종값, 증감값). 해당 인덱스에 해당하는 값을 찍는 것.
    print(x[i])





