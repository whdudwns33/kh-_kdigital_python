# 대문자는 소문자, 소문자는 대문자.
rst = ""
for e in input() : # input에 입력받는 문자열 만큼 자동 순회
    if e.islower():
        rst += e.upper()
    else :
        rst += e.lower()
print(rst)