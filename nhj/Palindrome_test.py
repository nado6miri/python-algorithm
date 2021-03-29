import Palindrome

str1 = "A man, a plan, a 98 canal : Panama $@$%%#@$@#"
str2 = "소주 만병만 주소"
str3 = 'race a car'

# test 1 : Palindrome 문자열 체크 - str1 = "A man, a plan, a 98 canal : Panama $@$%%#@$@#"
return_value = Palindrome.check_palindrome(str1)
if(return_value == True) :
    print("[Test1][OK]")
else :
    print("[Test1][Error]")

# test 2 : Palindrome 문자열 체크 - str2 = "소주 만병만 주소"
return_value = Palindrome.check_palindrome(str2)
if(return_value == True) :
    print("[Test1][OK]")
else :
    print("[Test1][Error]")

# test 3 : Palindrome 문자열 체크 - str3 = 'race a car'
return_value = Palindrome.check_palindrome(str3)
if(return_value == False) :
    print("[Test1][OK]")
else :
    print("[Test1][Error]")

