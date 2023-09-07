#세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
A = int(input("A 입력:"))
B = int(input("B 입력:"))
C = int(input("C 입력:"))
total = (A*B*C)
for i in range (0,10,1):
    total1 = str(total)
    count = total1.count(str(i))
    print(count)