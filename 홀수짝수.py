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

eve2 = list(filter(lambda e : int(e)% 2 == 0, arr))
odd2 = list(filter(lambda e : int(e)% 2 != 0, arr))
print(eve2)
print(odd2)
