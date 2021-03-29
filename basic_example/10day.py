# 예외처리 기본 문법 
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input(" 첫번쨰 숫자를 입력하세요 : "))
    num2 = int(input(" 두번쨰 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError:
    print("에러! 0을 입력하였습니다. 0으로 나눌수 없습니다.")
except Exception as err:
    print("알수없는 에러가 발생했습니다.")
    print(err)
finally:
    print("코드가 실행되고 예외처리가 완료되었습니다.")


print("프로그램 종료")

# 기존 Exception 발생시키기
try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input(" 첫번쨰 숫자를 입력하세요 : "))
    num2 = int(input(" 두번쨰 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


# 사용자 정의 Exception 발생시키기
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input(" 첫번쨰 숫자를 입력하세요 : "))
    num2 = int(input(" 두번쨰 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

