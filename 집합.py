# 집합은 주로 중복제거를 위해 사용
# 순서가 보장되지 않음.
# 중복 불가.
# mutable, 수정가능 함.

# 중복제거
s1 = set([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5])
s2 = set([4,5,6,7])
s3 = set([1,2,3,4,5])
print(s1)
print(s2)
print(s3)

# 합집합. 집합에서 어느 한쪽만 존재하면 포함된다. 중복은 제거
print(s1.union(s2))
print(s1 | s2)

# 교집합. 집합에서 모두 존재하는 요소만 선택
print(s1.intersection(s2))
print(s1 & s2)

# 차집합. 집합은 연산이 되고 교집합만 첫번째 집합에서 뺴고 남은 요소만 출력.
print(s1.difference(s2))
print(s1 - s2)




