# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
# a = map(int, input().split()) #map은 형변환 등을 위한 함수. map은 하나의 주소값으로 저장. 실제값을 도출하기 위해서는 list() 등을 이용해야 실제로 값이 도출될 수 있음. int에 함수를 넣을 수 있음
a, b, c = map(int, input().split())
total_val = str(a * b * c)
for i in range(10):
    print(total_val.count(str(i)))



