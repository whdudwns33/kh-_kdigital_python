#튜플이란 변경할 수 없는 시퀀스 자료형. 나머지는 리스트와 동일. 즉, 요소값만 바꿀수 없다는 특징
#튜플은 ()사용하여 정의. 혹은 괄호 없이 ,로만 판단

#튜플만들기
person0 = "전사", "마법사"     #튜플
person1 = "전사",             #튜플
person2 = "마법사"            #튜플이 아님
person3 = "궁수", 200, "헤네시스"
print(person0)   # 튜플
print(person1)  # 튜플
print(person2)  # 단순한 문자열 타입
print(person3)

#튜플 요소로 접근하기
print(person0[0])
print(person0[1])

#튜플의 언패킹
name, level, addr = person3
print(name)
print(level)
print(addr)

#튜플의 언패킹 기능을 이용한 함수 만들기
def get_person():
    name = "해적"         # 언패킹된 변수
    level = 120
    addr = "노틸러스"
    return name, level, addr

rst = get_person() #언패킹되서 전달되는 반환값을 다시 패킹하는 것.
print(rst)

name, level, addr = get_person()
print(name)
print(level)
print(addr)

tp = 1,1,2,2,2,3,3,3,3
print(tp.count(3)) # 매개변수로 전달한 변수가 몇번 등장하는지 계산
print(tp.index(2)) # 매개변수로 전달한 변수의 시작(가장 처음) 인덱스를 반환
print(len(tp))

#튜플에서 안되는 것. 튜플은 immutable특성 때문에 값을 바꿀 수 없음. 정확히는 삭제할 수 없음
#del tp[0] # 삭제는 안됨.

