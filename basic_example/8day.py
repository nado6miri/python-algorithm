name = "마린"
hp = 40
damage =5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 위의 코드를 class를 사용하여 object(객체)지향 프로그램으로 변경
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("뺴앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#parent class 부모 class
class CommonUnit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

#child class 자식 class
class AttackUnit(CommonUnit):
    def __init__(self, name, hp, damage, speed):
        CommonUnit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebeat1 = AttackUnit("파이어뱃", 50, 16, 100)
firebeat1.attack("5시")

firebeat1.damaged(25)
firebeat1.damaged(25)

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    # 부모의 attack 함수를 사용하지 않고 FlyableAttackUnit의 attack 함수를 다시 정의한다. - overloading 함수의 오버로딩이라 한다.
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 핵공격 합니다. [공격력*10배 {2}]"\
            .format(self.name, location, self.damage))

    # 부모의 move 함수를 사용하지 않고 FlyableAttackUnit의 move 함수를 다시 정의한다. - overloading 함수의 오버로딩이라 한다.
    def move(self, location):
        print("[공중 유닛 이동]")
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(self.name, location, self.flying_speed))

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")        
valkyrie.attack(3)        

vulture = AttackUnit("벌쳐", 80, 20, 10)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 3, 25)

# 벌쳐 : 지상유닛 생성 및 이동
vulture.move("11시")

# 배틀크루져 : 공중유닛 생성 및 이동(날아감)
battlecruiser.move("9시")