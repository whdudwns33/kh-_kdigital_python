# 로또 만들기

import random
print("로또")
ls = [] # 빈리스트 만들기
while True :
    rand = random.randrange(1, 46) # 46미만
    if rand not in ls : # 생성된  list에 rand값이 없으면 
        ls.append(rand) # append로 rand 추가
    if len(ls) == 6 : break
print(ls)
