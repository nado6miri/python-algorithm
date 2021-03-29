'''
Palindrome(팰린드롬)이란 회문이라고 부르며 "소주 만병만 주소" 처럼 앞으로 해도, 뒤로해도 동일한 문자열을 의미함.

1. 문자열을 입력받아 숫자/특수문자를 제외하고 한글/영문자만 가지고 Palindrome인지 아닌지 판단하여 True / False를 return한다.

example 1) True Case : "A man, a plan, a canal : Panama"
example 2) False Case : "race a car"

[출력 예문]
입력 string = "race a car"
중간 처리 문자열 = ['r', 'a', 'c', 'e', 'a', 'c', 'a', 'r']
결과 => 'race a car' 문자열은 Palindrome 이 아닙니다.

사전지식 : 정규식 re
Regular Expression

string 객체 함수  join 사용법 '구분자'.join(list).lower()

'''
import re


str1 = "A man, a plan, a 98 canal : Panama $@$%%#@$@#"
str2 = "소주 만병만 주소"
str3 = 'race a car'

def check_palindrome(s):
    pat = re.compile('[a-zA-Z]')
    result = pat.findall(s)
    #print(result)

    result = "".join(result).lower()
    #print(result)

    left = 0
    right = len(result) - 1

    #print(right)

    while left < right:
        if result[left] == result[right]:
            left += 1
            right -= 1
        else:
            break

    if left >= right:
#        print("이 문자열은 palindrome입니다")
        return True
    else:
 #       print("문자열은 Palindrome 이 아닙니다.")       
        return False


if __name__ == "__main__":
    checklist = [ str1, str2, str3 ]
    for s in checklist:
        if check_palindrome(s):
            print("{0} 문자열은 palindrome입니다".format(s))
        else:
            print("{0} 문자열은 Palindrome 이 아닙니다.".format(s))       

else:
    print("모듈로 import되었습니다.")