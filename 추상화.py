# 추상화
# 부모클래스에서 메서드의 정의를 하지 않고 상속받은 자식 클래스에서 오버라이딩하여 사용하도록 지정하는 것.
# 부모 클래스에서 선언한 메소드에 대해서 반드시 상속 받은 클래스에서 기능을 구현 해야하는 특성
# 추상 클래스가 포함된 부모 클래스는 객체로 만들 수 없음. 상속을 주기 위해서 존재

from abc import *
class NetworkAdapter(metaclass=ABCMeta): #추상 클래스를 선언
    @abstractmethod     # 추상메서드
    def connect(self): pass # 구현할 내용이 없는 경우  pass 키워드를 사용. 상속받은 class에서 무조건 선언 해야함


class Wifi(NetworkAdapter) :
    def __init__(self, company):    # 생성자 만들기
        self.company = company      # company 인스턴스 변수

    def connect(self):              # 부모 클래스에게서 상속받은 connect 추상 메서드 구현
        print(f"{self.company} Wi-Fi에 연결 했습니다.")

class FiveG(NetworkAdapter) :
    def __init__(self, company):    # 생성자 만들기
        self.company = company      # company 인스턴스 변수

    def connect(self):              # 부모 클래스에게서 상속받은 connect 추상 메서드 구현
        print(f"{self.company} 5G에 연결 했습니다.")

net = input("연결할 네트워크를 선택 : [1]Wifi [2]5G")
if net == "1":
    adapter = Wifi("kt")
    adapter.connect()
elif net =="2":
    adapter = FiveG("LG")
    adapter.connect()
else:
    print("연결할 네트워크가 없습니다.")


