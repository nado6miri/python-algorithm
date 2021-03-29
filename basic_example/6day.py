def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은{0} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balnce, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


#start...
open_account()

balance = 0 
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
#print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))



# 함수의 기본값(default)
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 언어: {2}" \
        .format(name , age, main_lang))

profile("유재석", 20, "파이선")
profile("김태호", 25, "자바")

def profile_default(name, age=17, main_lang="파이선"):
    print("이름 : {0}\t나이 : {1}\t주 언어: {2}" \
        .format(name , age, main_lang))

profile_default("유재석")
profile_default("김태호")

profile_default("정형돈", 20, "c")

# 키워드를 통한 함수호출
profile_default(age=25, main_lang= "C", name = "데프콘")

# 가변인자
def profile1(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end= " ")
    for lang in language:
        print(lang, end= " ")
    print()

profile1("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile1("김태호", 25, "Kotlin", "Swift")


# 가변인자 사용 안하고 하는 방법
def profile2(name, age, language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end= " ")
    for lang in language:
        print(lang, end= " ")
    print()

profile2("유재석", 20, ["Python", "Java", "C", "C++", "C#", "JavaScript"])
profile2("김태호", 25, ("Kotlin", "Swift"))


# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint1(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint1(gun, 2)
print("전체 총 : {0}".format(gun))

def std_weight (height, gender):
    result = 0
    height /= 100
    if gender == "남자":
        result = height * height * 22
    elif gender == "여자":
        result = height * height * 21
    else:
        print('성별을 올바르게 입력해주세요.("남자", "여자")')
        return -1
    
    result = round(result, 2)
    print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height*100, gender, result))
    return result
    
h = 175
g = "남자"
standard = std_weight(h, g)
#print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(h, g, standard))

standard = std_weight(178, "여자")
#print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(178, "여자", standard))

std_weight(176, "여성")
