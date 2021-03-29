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
import random

# 1~45 까지 숫자 중에 랜덤으로 하나를 뽑는다.
def lotto_num(min = 1, max = 45):
    num = random.randrange(min, max+1)
    #print("luckey_num = ", num)
    return num

# 1000원 로또 번호 추첨
def lotto_fullnumber():
    lotto = list()
    while True:
        num = lotto_num()
        if(num in lotto): 
            pass
        else:
            lotto.append(num)

        if(len(lotto) == 6) :
            break            
    
    lotto.sort()
    
    return lotto




def lotto_program():
    count = 0
    while True:
        try:
            answer = input("사려는 로또 금액을 천원단위로 입력하시오.")
            if (answer == 'X' or answer == 'x'):
                print("프로그램을 종료합니다.")
                break
            else:
                count = int(answer)
                if(count > 0) :
                    count = int(count/1000)
                    for i in range(count):
                        print("{0}회 추첨번호 = {1}".format(i, lotto_fullnumber()))
                else:
                    print("입력된 값이 0보다 작습니다.")


        except ValueError:
            print("잘못된 값을 입력하였습니다.")


if __name__ == "__main__":
    a = 0 / 2000
    lotto_program()
else :
    print("함수가 모듈 형태로 import 되었습니다.")
