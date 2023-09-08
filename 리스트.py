# 크기가 정해지지 않은 요소들에 대한 값을 저장하기 위한 자료형
# 아무 자료형이나 와도 된다.
# 중첩사용이 가능하다. [ ,[, [] ] ]
# 뮤터블 객체(읽고 쓰기가 가능하다.)
#
# number = [1,2,3,4,5]
# fruit = ["apple", "banana", "orange"]
# mixed = [1,"false",3.1,True]
# dup = [[[1,2],3,4],5,6,7,["계량경제학"]]
#
# # 변수와 리스트를 비교 해보기
# kor, eng, mat = map(int, input("성적 입력 : ").split())
# print(sum([kor, eng, mat]))
#
# # 리스트는 성적의 개수에 상관없이 입력 받을 수 있음.
# score = list(map(int, input("성적 입력 : ").split()))
# print(sum(score))
# print(sum(score) / len(score))

# 인덱싱과 슬라이싱.
str_name = ["서울","강남","수원","인천","한국"]
#인덱싱
print(str_name)
print(str_name[1]) # 1번째열 요소 강남. 서울은 0번째 인덱스 요소
print(str_name[1][1]) # 1번째 요소의 1번째 인덱스 요소
#슬라이싱
slice = str_name[1:3]   # 1번째열 요소 강남부터 3번째열 요소 인천까지
print(slice)
print(len(slice))
print(len(slice[1]))
prinmes = [2,3,5,7]
print(prinmes[0])   # 0번쨰 요소
print(prinmes[-1])  # 뒷자리 1번째 요소
print(prinmes[-2:]) # 뒷자리 부터 2번쨰 요소 출력
