balance = 0 # 외부에서 선언했지만 매개변수로 전달하여 결과를 리턴 받음
# return이 없으면 balance의 경우 0으로 계속 선언되고 함수의 경우 return이 있어야 원하는 결과값을 반환받을 수 있음.
# 계좌 개설하기
def open_account(name) :
    print(f"{name}님의 계좌가 개설되었습니다.")
    return name #반환값으로 이름을 전달.

# 입금 함수
def deposit(balance, save) : # 잔고와 입금액을 매개변수로 전달
    print(f"{save}원 입금. 잔액: {balance + save}")
    return balance + save

# 출금
def withdraw(balance, output):
    if balance >= output:
        print(f"{output}원 출금. 잔액: {balance - output}")
        return balance - output
    else:
        print(f"잔액이 부족합니다. 잔액: {balance}")
        return balance


name = open_account("전사")
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(f"{name}님의 잔액은 {balance}입니다.") # return이 있기 때문에 뱐수 balance의 값이 바뀔 수 있음
deposit(1000,500)

print(withdraw(1000,400))