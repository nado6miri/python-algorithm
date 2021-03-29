import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
#    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep= ":")


for subject in scores.keys():
    print(subject)


for score in scores.values():
    print(score)


for num in range(1, 21):
    print("대기번호 : "+ str(num).zfill(3))


#answer = input("아무 값이나 입력하세요. : ")
#print(type(answer))
#print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10 자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 딴 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _을 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마 찍어주기
print("{0:,}".format(1000000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))
# 3자리 마다 콤마로 찍어주기, 부호도 붙이기, 자릿수 확보하기, 빈자리는 ^으로 채워주기
print("{0:^<+30,}".format(1000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))


# 파일 입출력 (파일을 열면 리턴되는 값이 file discriptor이다.)
# 읽기모드(r) 쓰기모드(w) 추가모드(A) 
# 파일타입:텍스트모드(t) binary 모드(b)
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("과학 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("음악 : 80")
score_file.write("\n미술 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
contents = score_file.read()
print(contents)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")

while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")

score_file.close()
# readlines 는 한줄씩 읽어서 list형태로 나타낸다. readline은 한줄읽어 문자열로 나타낸다.
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
print("\n\nlines = {0}".format(lines))

for line in lines:
    print(line, end="")

score_file.close()


import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

with open("profile1.pickle", "wb") as profile_file:
    profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
    print(profile)
    pickle.dump(profile, profile_file)
 

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

with open("profile1.pickle", "rb") as profile_file:
    profile = pickle.load(profile_file)
    print(profile)


# with
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1, 51):
    file_name = ".//result//{0}주차.txt".format(i)
    #print(file_name)
    with open(file_name, "w", encoding="utf8") as fd:
        fd.write("- {0} 주차 주간보고 -\n".format(i))
        fd.write("부서 :\n")
        fd.write("이름 :\n")
        fd.write("업무 요약 :\n")

