r = input("문자 입력:")
for i in input():
    if i.islower():
        r += i.upper()
    else:
        r+= i.lower()
print(r)