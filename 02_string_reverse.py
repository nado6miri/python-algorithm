# 문자열 뒤집기 문제
# List에 존재하는 문자열을 뒤집는다.
# str1 = [ 'h', 'e', 'l', 'l', 'o' ]
# str2 = [ "H", "a", "n", "n", "a", "h"]

# Shallow copy & Deep Copy
import copy

# str을 reverse하는 함수
def string_reverse(s):
    string = copy.deepcopy(s)
    print("id(s) = {0}, id(string) = {1}".format(id(s), id(string)))

    left, right = 0, len(string) - 1
    while (left < right) :
        string[left], string[right] = string[right], string[left]
        left+=1
        right-=1
    
    return string


# str을 reverse하는 함수1
def string_reverse1(s):
    string = copy.deepcopy(s)
    print("id(s) = {0}, id(string) = {1}".format(id(s), id(string)))

    left, right = 0, len(string) - 1
    while (left < right) :
        tmp = string[left]
        string[left] = string[right]
        string[right] = tmp
        left+=1
        right-=1
    
    return string

# str을 reverse하는 함수2
def string_reverse2(s):
    return s[::-1]



if __name__ == "__main__":

    # 1. str.reverse() 함수를 사용하는 방법
    print("\n str.reverse() 함수를 활용한 문자열 뒤집기")
    str1 = [ 'h', 'e', 'l', 'l', 'o' ]
    str2 = [ "H", "a", "n", "n", "a", "h"]
    str1.reverse()
    str2.reverse()
    print("str1 문자열 뒤집기 결과는 {0} 입니다.".format(str1))
    print("str2 문자열 뒤집기 결과는 {0} 입니다.".format(str2))

    # 2. str을 reverse하는 함수를 직접 만들자...
    print("\n string_reverse() 함수를 활용한 문자열 뒤집기")
    str3 = [ 'h', 'e', 'l', 'l', 'o', 'z' ]
    str4 = [ "H", "a", "n", "n", "a", "h", 'x']
    print("id(str3) = {0}, value = {1} 문자열 뒤집기 결과는 {2} 입니다.".format(id(str3), str3, string_reverse(str3)))
    print("id(str4) = {0}, value = {1} 문자열 뒤집기 결과는 {2} 입니다.".format(id(str4), str4, string_reverse(str4)))

    # 3. str을 reverse하는 함수를 직접 만들자...
    print("\n string_reverse1() 함수를 활용한 문자열 뒤집기")
    str5 = [ 'h', 'e', 'l', 'l', 'o', 'z' ]
    str6 = [ "H", "a", "n", "n", "a", "h", 'x']
    print("id(str5) = {0}, value = {1} 문자열 뒤집기 결과는 {2} 입니다.".format(id(str5), str5, string_reverse1(str5)))
    print("id(str6) = {0}, value = {1} 문자열 뒤집기 결과는 {2} 입니다.".format(id(str6), str6, string_reverse1(str6)))


    # 4. str을 reverse하는 함수를 직접 만들자...
    print("\n string_reverse2() 함수를 활용한 문자열 뒤집기")
    print("id(str5) = {0}, value = {1} 문자열 뒤집기 결과는 {2} 입니다.".format(id(str5), str5, string_reverse2(str5)))
    print("id(str6) = {0}, value = {1} 문자열 뒤집기 결과는 {2} 입니다.".format(id(str6), str6, string_reverse2(str6)))
