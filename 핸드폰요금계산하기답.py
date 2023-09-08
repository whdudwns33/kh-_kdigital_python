# 영식이 요금제 : 30초에 10원
# 민식이 요금제 : 60초에 15원
n = int(input("통화 회수:"))
call = list(map(int, input("통화시간:").split()))  # 통화 횟수에 대한 통화 시간. list()는 개수가 정해지지 않은 배열을 만들 수 있음
y_pay = m_pay = 0
for i in range(n) :
    y_pay += (call[i] // 30) * 10 + 10
    m_pay += (call[i] // 60) * 15 + 15

if y_pay > m_pay:
    print("M", m_pay)
elif y_pay < m_pay:
    print("Y", y_pay)
else:
    print("Y M", y_pay)
