# 회원가입을 위한 아이디와 패스워드 입력 받기
user = input("아이디 : ")
if len(user) >= 8: # 입력받은 아이디의 길이가 10과 같거나 커야함
    pw = input("비밀번호 : ")
    # if pw.__len__() < 8 or pw.__len__() > 16: #문자열의 내부함수를 통한 pw의 길이
    if len(pw) < 8 or len(pw) > 16:             #외부함수를 통한 pw 길이
        print("비밀번호는 8~16자리입니다. ")
    elif pw.find(user) >= 0: #
        print("비밀번호는 아이디가 포함되지 않습니다. ")
    else:
        print(f"아이디 : {user}")
        print(f"패스워드 : {pw}")
else :
    print("아이디는 8자 이상입니다.")