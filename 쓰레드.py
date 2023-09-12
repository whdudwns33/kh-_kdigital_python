from simple_colors import *  # 화면 출력에 컬러 넣기
import threading             # 쓰레드 기능을 위해 import
import time                  # sleep()을 쓰기 위해서 import
import random


class Unit:
    def __init__(self, pp, mp, ph, mh, hp):
        self.pPower = pp
        self.mPower = mp
        self.pHit = ph
        self.mHit = mh
        self.hp = hp
        self.isAlive = True


class Character(Unit):  # Unit을 상속받아 Character 클래스 생성
    def __init__(self, pp, mp, ph, mh, hp, um, job):
        Unit.__init__(self, pp, mp, ph, mh, hp) # 부모의 생성자 상속(호출)
        self.ultimate = um  # 궁극기 특성 추가
        self.job = job      # 직업과 궁극기는 부모 클래스에서 선언되지 않음.

    def p_attack(self):
        return self.pPower * self.pHit

    def m_attack(self):
        return self.mPower * self.mHit

    def attack_ultra(self):
        return self.ultimate

    def is_alive(self):
        return self.isAlive

    def setDamage(self, damage):
        if self.hp > damage:
            self.hp -= damage
            print(f"남아 있는 {green(self.job)}의 체력은 {blue(self.hp)} 입니다.")
            self.isAlive = True
        else:
            print(f"{green(self.job)}가 죽었습니다. 게임을 종료 합니다.")
            self.isAlive = False


# 스레드에서 실행할 함수
def wizard_th():
    print(f"{wizard.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    while True:
        time.sleep(5)
        if warrior.is_alive() == False or wizard.is_alive() == False:
            break
        val = random.randrange(0, 2)
        ul = random.randrange(0, 18)
        if val == 0:
            print(f"{blue('물리공격')} >> {warrior.job}에게 {yellow(wizard.p_attack())} 데미지를 입혔습니다.")
            warrior.setDamage(wizard.p_attack())
        else:
            print(f"{yellow('마법공격')} >> {warrior.job}에게 {yellow(wizard.m_attack())} 데미지를 입혔습니다.")
            warrior.setDamage(wizard.m_attack())
        if ul == 1:
            print(f"{red('궁극기 발동')} >> {warrior.job}에게 {red(wizard.attack_ultra())} 데미지를 입혔습니다.")
            warrior.setDamage(wizard.attack_ultra())

def worrior_th():
    print(f"{warrior.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    while True:
        time.sleep(5)
        if warrior.is_alive() == False or wizard.is_alive() == False:
            break
        val = random.randrange(0, 2)
        ul = random.randrange(0, 12)
        if val == 0:
            print(f"{blue('물리공격')} >> {wizard.job}에게 {warrior.p_attack()} 데미지를 입혔습니다.")
            wizard.setDamage(warrior.p_attack())
        else:
            print(f"{yellow('마법공격')} >> {wizard.job}에게 {warrior.m_attack()} 데미지를 입혔습니다.")
            wizard.setDamage(warrior.m_attack())
        if ul == 1:
            print(f"{red('궁극기 발동')} >> {wizard.job}에게 {red(warrior.attack_ultra())} 데미지를 입혔습니다.")
            wizard.setDamage(warrior.attack_ultra())



# 메인 영역
if __name__ == "__main__":  # main thread 흐름을 타는 시작점

    name1 = input("전사는 강력한 체력의 물리공격형 캐릭터 (이름 입력) : ")
    name2 = input("마법사는 강력한 마법 공격형 캐릭터 (이름 입력) :  ")

    warrior = Character(8, 2, 0.8, 0.5, 150, 40, name1)  # 물공,마공, 물방, 마방, 물적,마적,체력,궁극기
    wizard = Character(2, 20, 0.5, 0.9, 60, 55, name2)  # 물공,마공, 물방, 마방, 물적,마적,체력,궁극기

    x1 = threading.Thread(target=wizard_th)
    x2 = threading.Thread(target=worrior_th)
    # print(f"{warrior.job}가 전투 준비를 완료 했습니다.")
    # time.sleep(1)
    x1.start()  # 서브 스레드 시작: 위자드
    x2.start()  # 서브 스레드 시작: 워리어
    # while True:
    #     time.sleep(5)
    #     if warrior.is_alive() == False or wizard.is_alive() == False:
    #         break
    #     val = random.randrange(0, 2)
    #     ul = random.randrange(0, 12)
    #     if val == 0:
    #         print(f"{blue('물리공격')} >> {wizard.job}에게 {warrior.p_attack()} 데미지를 입혔습니다.")
    #         wizard.setDamage(warrior.p_attack())
    #     else:
    #         print(f"{yellow('마법공격')} >> {wizard.job}에게 {warrior.m_attack()} 데미지를 입혔습니다.")
    #         wizard.setDamage(warrior.m_attack())
    #     if ul == 1:
    #         print(f"{red('궁극기 발동')} >> {wizard.job}에게 {red(warrior.attack_ultra())} 데미지를 입혔습니다.")
    #         wizard.setDamage(warrior.attack_ultra())
