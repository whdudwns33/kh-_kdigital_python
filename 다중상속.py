# 다중 상속은 둘 이상의 부모 클래스로 부터 상속을 받는 것.
# 자바에서는 다중 상속 문제가 있었음.
# 다이아몬드 상속 문제.
# 사람이라는 최상위 부모 클래스에서 학생과 노동자라는 자식클래스에 '먹는다' 라는 메서드를 상속하고
# 학생과 노동자는 각각의 특성인 '공부하다'와 '일하다'를 갖는다. 물론 '먹는다'라는 특징 또한 갖음
# 그리고 나서 개발자 라는 클래스에 학생과 노동자가 상속을 하는데,
# 자바는 사람이라는 클래스에서 상속받은 학생과 노동자에서 동일한 특성을 개발자에 중첩되게 상속하는 문제가 생기지만
# 파이썬은 이중상속 문제가 생기지 않는다.

class Person :
    def __init__(self, eat):
        self.eat = eat
        print("인간 입니다.")
    def set_eat(self):
        print(f"{self.eat} 밥을 먹습니다.")

class Student(Person):  # Person 클래스를 상속 받은 Student
    def __init__(self, eat, study):
        Person.__init__(self, eat)  # 상속 받은 특성
        self.study = study
        print("학생 입니다.")
    def set_study(self, study):
        self.study = study
        print("공부 합니다.")

class Worker(Person):
    def __init__(self, eat, work):
        Person.__init__(self, eat)  # 상속 받은 특징
        self.work = work
        print("직장인 입니다.")
    def set_work(self, work):
        self.work = work
        print("일 합니다.")

class Developer(Student, Worker):
    def __init__ (self, eat, study, work):
        Student.__init__(self, eat, study)
        Worker.__init__(self, eat, work)
        print("개발자 입니다.")

dev = Developer(1, 1, 1)
dev.eat = 200
dev.set_eat()