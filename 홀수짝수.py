# map : 전달 받은 값을 함수내부에서 가공해서 반환한다. 입력 개수와 반환 개수가 동일
# filter : 전단 받은 값을 함수내부에서 조건에 일치하는 것만 골라서 반환한다.


arr = list(map(int, input().split()))
eve = []
odd = []

# 향상된 for문이나 일반for문을 통한 홀수짝수 나누기
for e in arr:
    if e % 2 == 0:
        eve.append(e)
    else:
        odd.append(e)
print(eve)
print(odd)
#filter
eve2 = list(filter(lambda e : int(e)% 2 == 0, arr))
odd2 = list(filter(lambda e : int(e)% 2 != 0, arr))
print(eve2)
print(odd2)
