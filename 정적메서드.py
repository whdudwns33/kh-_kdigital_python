class Car :
    isinstance_count = 0    # 클래스 변수

    # 초기화 함수. 생성자
    def __init__(self, size, model):
        self.size = size   # 인스턴스 변수 생성 및 초기화
        self.model = model
        Car.isinstance_count = Car.isinstance_count + 1 # 클래스 변수 이용
        print(f"자동차 객체 생성 수 : {Car.isinstance_count}")

    def move(self, speed):
        self.speed = speed
        print(f"자동차 {self.size} & {self.model}가 시속 {self.speed}로 달립니다.")

    @staticmethod   # 정적 메서드로 객체로 만들어 지지 않음
    def check_type(code):
        if(code >= 10): print("전기차 입니다.")
        elif(code >= 20): print("가솔린차 입니다.")
        elif(code >= 30): print("디젤차 입니다.")
        else: print("분류 코드가 없습니다.")

car1 = Car("소형", "모닝")
car2 = Car("중형", "쏘나타")

car1.move(90)
Car.check_type(11)
car2.move(70)