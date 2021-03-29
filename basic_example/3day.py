sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "피이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "061026-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print(" 뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에서 부터) : " + jumin[-7:])

month = jumin[2:4]
print("month = jumin[2:3] type ==> ", type(month))
month = int(month) * 2
print("month = int(month)*2 type ==> ", type(month))
print("month = ", month)


python = "Python is Amazing, Python is good"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

python = python.replace("Python", "java")
print(python)

index = python.find("java", 0) 
print(index)
print(python.find("java", index+1))

print("나는 %s 살입니다." % 16)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다.".format("16"))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 16, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 16))

age = 16
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
print("나는 ", age, "살이며, ", color, "색을 좋아해요.")


# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따움표
#저는 "나는코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \'나도코딩\'입니다.")
print("저는 \"나도코딩\"입니다.")

# \\ :문장 내에서 \
print("E:\\workspace\\nhj>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rpine")

# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


site = "http://naver.com"
#site = "http://shinhancard.com"

site_name = site.replace("http://", "")
print(site_name)
print(type(site_name))

site_name = site_name.split(".")
print(site_name)
print(type(site_name))

site_name = site_name[0]
print(site_name)
print(type(site_name))

# password 1
password = site_name[0:3]
print(password)

# password 2
count = len(site_name)
print(count)

# password 3 : e의 갯수
ecount = site_name

e_count = site_name.count('e')
print(e_count)

password = password + str(count) + str(e_count) + "!"
print("My password = ", password)

print("{0}의 비밀번호는 {1}입니다.".format(site, password))