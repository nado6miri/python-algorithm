from random import *


subway = [10, 20, 30]
print("subway의 타입은 {0}이고 값은 {1}입니다.".format(type(subway), subway))

subway = ["유재석", "조세호", "박명수"]
print(subway)

# index는 index함수로 전달된 파라미터(데이터)가 존재하는 위치를 리턴하는 함수(0부터 시작)
print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(2, "정형돈")
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway = ["유재석", "조세호", "박명수"]
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5,3,4,2,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)

# Dictionary

cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet)
print(5 in cabinet)


cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-3"] = "조세호"
print(cabinet)

cabit = {}

cabit['key1'] = 1
cabit['key2'] = 2
cabit['key3'] = 3
cabit['key4'] = 4
print(cabit)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)

# Tuple

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# Tuple은 읽기만 가능하기 때문에 값을 지정할수 없다.
# menu[0] = "회"

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할수있거나 python 할수있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할수있지만 python은 할줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# java를 할수있는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요.
java.remove("김태호")
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
menu.append("커피")
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


reply = { 
    1 : "이게 문제냐?", 2 : "저를 뽑아주세요", 3 : "3's comment", 4: "4's comment", 5: "5's comment", 6: "6's comment", 7: "7's comment", 8: "8's comment", 9: "9's comment", 10: "10's comment",
    11 : "이게 문제냐?", 12 : "저를 뽑아주세요", 13 : "13's comment", 14: "14's comment", 15: "15's comment", 16: "16's comment", 17: "17's comment", 18: "18's comment", 19: "19's comment", 20: "20's comment"
}
print(reply)

applier = reply.keys()
print(applier)

applier = list(applier)
print(type(applier))

shuffle(applier)
print(applier)

chicken = sample(applier, 1)

applier = set(applier)
chicken = set(chicken)
applier -= chicken

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken))
print(applier)

coffee = sample(applier, 3)
print(coffee)
print("커피 당첨지 : {0}, {1}, {2}".format(coffee[0], coffee[1], coffee[2]))
print("커피 당첨지 : {0}".format(coffee))
print("-- 축하합니다 --")


