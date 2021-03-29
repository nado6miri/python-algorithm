import random


# 0. 사려는 로또 금액을 천원단위로 입력받는다.
# 0-1. 값이 오류일 경우 예외처리를 하고 다시 값을 입력을 요구한다. (예외 발생시 "값을 잘못 입력 하였습니다." 라고 출력함)
# 1. 로또 금액만큼 로또 번호를 생성하여 출력한다. (1천원일 경우 6개의 숫자를 return 한다. 1만원일 경우 6개의 숫자 10개를 return한다.) 
# 1-1. lotto번호 1 ~ 45까지 숫자를 임의로 6개를 선정한다.
# 1-2. 이미 선정된 번호가 나올경우 다시 새로운 번호를 선정한다.
# 1-3. 선정된 6개의 숫자를 오름차순으로 정렬한다.
# 2. x 또는 X를 입력하면 프로그램을 종료하고 그렇지 않을경우 0 ~ 1을 반복한다.

'''
사려고 하는 로또 금액을 천원단위로 입력하세요 (종료하려면 x 를 누르세요):5000
최종 로또 번호 생성은 아래와 같습니다.
0회 추첨번호 = [2, 4, 25, 29, 38, 45]
1회 추첨번호 = [3, 4, 7, 17, 34, 38]
2회 추첨번호 = [1, 16, 26, 35, 37, 45]
3회 추첨번호 = [4, 14, 25, 27, 30, 39]
4회 추첨번호 = [3, 5, 6, 11, 35, 44]
'''

def choose_lucky_num(min = 1, max = 45):
    num = random.randrange(min, max+1)
    #print("Seleted num = ", num)
    return num   
 

def get_lotto_fullnumber():
    #1. 로또 번호 6개를 추첨합니다.
    lotto = list()
    while True:
        num = choose_lucky_num()
        if(num in lotto) : 
            pass
            #print("이미 선정된 번호 입니다. 재 추첨하겠습니다.")
        else:
            #print("새로 선정된 번호는 {0} 입니다.".format(num))
            lotto.append(num)

        if(len(lotto) == 6) :
            break            

    # 오름차순 정렬
    lotto.sort()
    
    return lotto


def Lotto_factory():
    count = 0
    while True:
        try:
            input_str = input("사려고 하는 로또 금액을 천원단위로 입력하세요 (종료하려면 x 를 누르세요):")

            if(input_str == 'x' or input_str == 'X') :
                print("로또 생성 프로그램을 종료 합니다.")
                break
            else:
                money = int(input_str)
                count = int(money / 1000)
                print("최종 로또 번호 생성은 아래와 같습니다.")
                for i in range(count):
                    print("{0}회 추첨번호 = {1}".format(i, get_lotto_fullnumber()))

        except ValueError:
            print("잘못된 값을 입력하였습니다.")

        finally:
            pass

if __name__ == "__main__":
    Lotto_factory()