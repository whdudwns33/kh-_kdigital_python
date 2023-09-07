A = int(input("A 입력:"))
B = int(input("B 입력:"))
C = int(input("C 입력:"))
total = (A*B*C)
for i in range (0,10,1):
    total1 = str(total)
    count = total1.count(str(i))
    print(count)