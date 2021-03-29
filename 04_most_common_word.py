# 금지된 단어를 제외하고 가장 흔한 단어를 출력하라.
# 대소문자를 구분하지 않으며, 구두점(마침표, 쉼표)는 무시한다.

# 입력값 paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# 금지어 banned = ["hit"]
# 출력값 = "ball"

# 정규식 : https://wikidocs.net/4308
# re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)

'''
Comprehension이란 
iterable한 오브젝트를 생성하기 위한 방법중 하나로 파이썬에서 사용할 수 있는 유용한 기능중 하나이다.
파이썬에는 다음과 같은 크게 네 가지 종류의 Comprehension이 있다.
https://mingrammer.com/introduce-comprehension-of-python/

List Comprehension (LC)
Set Comprehension (SC)
Dict Comprehension (DC)
Generator Expression (GE)

collections 모듈
https://wikidocs.net/84392
'''

import re
import collections  


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(paragraph)
temp = re.sub(r'[^\w]', ' ', paragraph)
print (temp)


# data cleansing.. 전처리 과정을 거침.
words = [ word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if(word not in banned) ]

print("words = ", words)

for word in words:
    print(word)


#counts = collections.defaultdict(int)
counts = collections.Counter(words)
print(counts)

mostcommon = counts.most_common(1)
print(mostcommon[0][0])

