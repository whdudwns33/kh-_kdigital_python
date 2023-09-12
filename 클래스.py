# 생성자는 클래스가 객체로 만들어 질 때, 자동으로 호출되며 객체의 초기값을 지정할 수 있음
# 생성자 키워드가 있음: __init__
# self는 자신의 객체를 가리키는 변수. ex. tv1 = Tv(~~~) 객체를 생성하면 self는 객체를 의미하고 거기에 생성자의 인스턴스 변수를 불러옴. 추가로 self는 아무거나 써도 됨.
# 파이썬은 오버로딩이 없고 캡슐화가 완벽하지 않음
# 인스턴스 필드는 따로 없고 생성자 안에 직접 입력해야함


class Tv :
    #생성자 생성
    def __init__(self,name, is_on, channal, volume):    # 객체, 이름~~~
        self.name = name
        self.is_on = is_on
        self.channel = channal
        self.volume = volume

    #setter
    def set_on(self, is_on):
        self.is_on = is_on
    def set_channel(self, channel):
        self.channel = channel
    def set_volume(self, volume):
        self.volume = volume

    #getter
    def get_on(self, is_on):
        self.is_on = is_on
    def get__channel(self, channel):
        self.channel = channel
    def get_volume(self, volume):
        self.volume = volume

    def  view_tv(self):
        power = "off", "on"
        print(f"이름: {self.name}")
        print(f"전원: {self.is_on}")
        print(f"채널: {self.channel}")
        print(f"볼륨: {self.volume}")

lg_tv = Tv("Lg", False, 10 ,10)
samsung_tv = Tv("Ss", False , 10, 10)
lg_tv.view_tv()
samsung_tv.view_tv()


