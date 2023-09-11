# 클로저 : 함수 안에 내부 함수(inner function)를 구현하고 그 내부 함수를 반환하는 함수
# 콜백 함수를 사용하기 위해서도 호출 함
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()
print(c(2), c(5), c(10))