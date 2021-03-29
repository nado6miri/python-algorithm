import keyboard
'''
a = 3
b = 5
c = a + b
print("a = ", a, " b = ", b, " c = ", c)
'''

# 더하기 함수
def sum(a, b):
    '''
    이 sum 함수는 더하기 함수입니다.
    '''
    c = a + b
    return c

# 빼기 함수
def sub(a, b):
    c = a - b
    return c

# 곱하기 함수
def mul(a, b):
    c = a * b
    return c

# 나누기 함수
def div(a, b):
    c = a / b
    return c

def hello() :
    print("hello....")

def scores():
    score_korea = input("국어 점수를 입력하세요 => ")
    score_korea = int(score_korea)
    score_math = input("수학 점수를 입력하세요 => ")
    score_math = int(score_math)
    score_english = input("영어 점수를 입력하세요 => ")
    score_english = int(score_english)
    average = (score_korea + score_math + score_english) / 3
    print("당신의 평균은 = ", average, " 입니다.")
    pass

def scores2():
    score_korea = input("국어 점수를 입력하세요 => ")
    score_korea = int(score_korea)
    score_math = input("수학 점수를 입력하세요 => ")
    score_math = int(score_math)
    score_english = input("영어 점수를 입력하세요 => ")
    score_english = int(score_english)
    score_art = input("미술 점수를 입력하세요 => ")
    score_art = int(score_art)
    score_music = input("음악 점수를 입력하세요 => ")
    score_music = int(score_music)
    average = (score_korea + score_math + score_english + score_art + score_music) / 5
    print("당신의 평균은 = ", average, " 입니다.")
    pass

def scores3():
    count = 5
    score_list = [] # 0: 국어, 1: 수학, 2: 영어, 3: 미술, 4: 음악

    for i in range(count):
        print(i, "번째 과목에 대한")
        score = input("점수를 입력하세요 => ")
        score = int(score)
        score_list.append(score)
        
    print("입력한 값은 = ", score_list)
    # 1. list에 있는 원소를 모두 더한다.
    hap = 0
    for i in range(len(score_list)):
        hap = hap + score_list[i]

    # 2. 더한값을 원소 개수로 나눈다.
    average = hap / len(score_list)
    print("당신의 평균은 = ", average, " 입니다.")
    pass


def looptest():
    e = {'name': '나성빈', 'age': 46, 'address': '경기 오산시 청호동', 'phone': '010-9937-5504'}

    for key in e:
        print("Key = ", key, " value = ", e[key])
#        print(key, e[key])

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for val in a:
        print("list val = ", val)

    b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for val in b:
        print("tuple val = ", val)        
        if val == 5:
            print("tuple value is 5 입니다.")
        else:
            pass

def inputtest():
    for cnt in range(10):
        inval = input("keyboard를 누르세요:")
        print("입력된 Key = ", inval, " 입니다.")

    print("키 입력 10개를 모두 받았습니다. - (종료)")
    pass

def inputtest2():
    bullet = 10
    while (True):
        key = keyboard.read_key()
        if(key == 'esc'):
            break
        elif(key == 'down'):
            print("뒤로!!")
        elif(key == 'up'):
            print("앞으로!!")
        elif(key == 'left'):
            print("좌회전!!")
        elif(key == 'right'):
            print("우회전!!")
        elif(key == 'a'):
            if(bullet > 0):
                bullet = bullet - 1
                print("사격-탕!!, 남은총알 = ", bullet)
            else:
                print("총알이 없습니다.")
        elif(key == 'space'):
            print("Jump!!")
        else:
            pass

    print("ESC 키가 입력되어 프로그램을 종료합니다.")
    pass

# 1. 프로그램의 시작을 알린다.
if __name__ == "__main__":
    print("main function 입니다.")
    '''
    print("sum(5, 9) = ", sum(5, 9))
    print("sum(나, 형준) = ", sum("나", "형준"))
    print("sub(5, 9) = ", sub(5, 9))
    print("mul(5, 9) = ", mul(5, 9))
    print("div(5, 9) = ", div(5, 9))

    result = mul(9, 9)
    print("9 * 9 = ", result)

    hello()

#    scores()
    scores3()
    '''
    looptest()
    inputtest2()