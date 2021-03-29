'''
Palindrome(팰린드롬)이란 회문이라고 부르며 "소주 만병만 주소" 처럼 앞으로 해도, 뒤로해도 동일한 문자열을 의미함.

1. 문자열을 입력받아 특수문자를 제외하고 한글/영문자/숫자만 가지고 Palindrome인지 아닌지 판단하여 True / False를 return한다.

example 1) True Case : "A man, a plan, a canal : Panama"
example 2) False Case : "race a car"

[출력 예문]
입력 string = "race a car"
중간 처리 문자열 = ['r', 'a', 'c', 'e', 'a', 'c', 'a', 'r']
결과 => 'race a car' 문자열은 Palindrome 이 아닙니다.

'''

import re

str1 = "A man, a plan, a 98 canal : Panama"
str2 = "소주 만병만 주소"
str3 = 'race a car'

# 1. list를 이용하여 구현
def is_palindrome(string : str) -> bool:
    print("입력 문자열 = ", string)
    s = []
    for char in string:
        if(char.isalnum()) :
            s.append(char.lower())

    print("중간 처리 문자열 = ", s)

    while len(s) > 1:
        if(s.pop(0) != s.pop()) : 
            return False

    return True


# 2. 문자열 Slice를 이용하여 구현
# 정규식 : https://wikidocs.net/4308
def is_palindrome1(string : str) -> bool:
    print("입력 문자열 = ", string)
    string = string.lower()
    string = re.sub('[^a-z]', '', string)
    print("정규식 후 입력 문자열 = ", string)

    return string == string[::-1]


if __name__ == "__main__":

    string = str1
    if(is_palindrome(string)):
        print("결과 => \'{0}\' 문자열은 Palindrome 입니다.".format(string))
    else:
        print("결과 => \'{0}\' 문자열은 Palindrome 이 아닙니다.".format(string))

    if(is_palindrome1(string)):
        print("결과1 => \'{0}\' 문자열은 Palindrome 입니다.".format(string))
    else:
        print("결과1 => \'{0}\' 문자열은 Palindrome 이 아닙니다.".format(string))
