# pass
class BuildingUnit():
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

# super
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable):
    def __init__(self):
        super().__init__()


class FlyableUnit2(Flyable, Unit):
    def __init__(self):
        # 두개 이상의 class를 상속받을 경우 super()를 사용하면 맨 마지막에 상속된(Unit class) 생성자만 호출된다.
        # 따라서 두 class의 생성자를 호출하기 위해서는 Unit.__init__(), Flyable.__init__() 이렇게 직접 부모 클래스의 생성자를 호출해야 한다.
#        super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()
print("=========================\n")
dropship2 = FlyableUnit2()

print("============ 퀴 즈 =================\n")

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        pass

    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
        pass

appt1 = House("강남", "아파트", "매매", "10억", "2010년")
#appt1.show_detail()

appt2 = House("마포", "오피스텔", "전세", "5억", "2007년")
#appt2.show_detail()

appt3 = House("송파", "빌라", "월세", "500/50", "2000년")
#appt3.show_detail()

apt = []

apt.append(appt1)
apt.append(appt2)
apt.append(appt3)

count = len(apt)
print("총 {0}대의 매물이 있습니다.".format(count))

for i in apt:
    i.show_detail()
    pass
