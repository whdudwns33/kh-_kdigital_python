# 클래스 상속
# 오버라이딩은 부모 클래스를 상속받아 동일한 메서드를 재정의하여 사용하는 것.
# 파이썬은 오버로딩이 없음. 왜냐하면, 데이터 형이 없기 때문에 매개변수에 데이터형을 임의로 넣어도 동작, 오버로딩과 유사한 효과
# 디폴트 매개변수 문법이 있음

# def sum(num1, num2, num3 = 100):
#     return num1 + num2 + num3
#
# print(sum(100 , 200))
# print(sum(100 , 200, 300))
# print(sum("korea", "seoul", ))

class ProtoTV:
    def __init__(self, isOn, channel, volume):
        self.isOn = isOn
        self.channel = channel
        self.volume = volume

    def set_on(self, isOn):
        self.isOn = isOn

    def set_channel(self, cnl):
        if 0 < cnl < 1000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

    def set_volume(self, vol):
        self.volume = vol

    def get_on(self):
        return self.isOn

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume


class TV(ProtoTV):  #Proto Tv로 부터 상속 받음
    def set_channel(self, cnl): # 오버라이딩, 재정의. 부모가 가진 메서드를 상속받아 재정의
        if 0 < cnl < 2000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")


lg_tv = TV(False, 10, 10)
samsung_tv = TV(False, 20, 20)
samsung_tv.set_channel(1200)

proto = ProtoTV(False, 10, 10)
proto.set_channel(1000)

