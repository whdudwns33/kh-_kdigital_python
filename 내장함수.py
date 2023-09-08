# 내장 함수: 파이썬이 기본적으로 제공, import가 필요 없음
# 외장 함수: 파이썬이 기본적으로 제공하긴 하지만, import가 필요함

#큰 값 작은 값 찾기
print(max(1,2,3,4,5))    # 자바의 max 메서드는 두개의 값중에서 찾는 것. 파이썬은 둘이상
print(min(1,2,3,4,5))

#총합 구하기
print(sum([1,2,3,4,5]))  # list에 대한 총합 구하기
print(sum({1,2,3,4,5}))  #
print(sum((1,2,3,4,5)))  # 튜플에 대한 총합
# num = list(map(int,input("정수 입력:").split())) #입력받은 정수를 리스트로 반환
# print(f"총 합 : {sum(num)}")
# print(f"평 균 : {sum(num) / len(num)}")

#몫과 나머지 구하기
print(divmod(10, 4))    # 튜플의 동작 원리, 두개의 반환값으로 받음

#여러 개의 값을 한번에 입력 받아서 리스트로 만들기
#리스트에서 최대값과 최소값, 합계, 평균, 몫, 나머지
arr = list(map(int, input("리스트:").split()))
print(max(arr))
print(min(arr))
print(sum(arr))
print(sum(arr) / len(arr))
print(sum(arr) // len(arr))
print(sum(arr) % len(arr))
print(divmod(sum(arr), len(arr)))

# 정렬
my_list = [1,2,8,9,15,6,7,8,9,10]
# 내림차순
print(sorted(my_list, reverse= True))
# 오름차순
print(sorted(my_list))



