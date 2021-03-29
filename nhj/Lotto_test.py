import Lotto as lotto

#test step 1 : lotto_num() 함수를 검증한다.
for i in range(1000):
    num = lotto.lotto_num()
    if num < 0 or num > 45 :
        print("함수에 문제가 있습니다. error 입니다. num=", num)

print("함수 검증 Test step 1가 종료되었습니다.")        

#test step 2 : lotto_fullnumber() 함수를 검증한다.
for i in range(1000):
    result = lotto.lotto_fullnumber()
    if (len(result) == 6):
        pass
        #print("선정된 값은 6개로 정상입니다. = {0}".format(result))
    else :
        pass
        #print("선정된 값은 {0}개로 비정상입니다. = {1}".format(len(result), result))
        print("[Error] 비정상입니다. = {1}".format(result))

print("함수 검증 Test step 2가 종료되었습니다.")        
