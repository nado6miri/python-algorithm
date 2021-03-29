# pip install 패키지 설치 방법
# pip install beautifulsoup4
# pip list - 어떤 package가 설치되었는지 확인하는 명령어
# pip install --upgrade beautifulsoup4 패키지 업그레이드
# pip uninstall beautifulsoup4 패키지 삭제

import inspect
from bs4 import BeautifulSoup
print(inspect.getfile(BeautifulSoup))

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>some<b>bad<i>HTML")
print(soup.prettify())

# 내장함수
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어 좋아하세요?")
# print("{0}은 아주 좋은 언어 입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체기 어떤 변수외 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "jim"
# print(dir(name))


# 내장함수 : python에서 기본적으로 제공해 주는 함수 - import 없이 바로 사용가능
# 외장함수 : python에서 import를 해서 기본적으로 제공해 주는 함수. import 모듈명 을 해서 사용함. ramdom같은 모듈..
# 사용자 정의함수 : 사용자가 직접 모듈을 만들고 import 해서 사용함.

# 외장함수
import glob
print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)

import byme
byme.sign()