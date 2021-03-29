'''
알고리즘을 바로 코드로 보기 전에 먼저 Anagram이 무엇인지부터 살펴보는 것이 순서일테다. 
Anagram(이하 “아나그램”)은 한 단어를 구성하는 글자의 개수를 그대로 유지하면서 순서만 바꾼 단어를 일컫는 말로 
한글로는 ‘어구전철’(語句轉綴)이라고도 한다. 

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = [
    ["ate", "eat", "tea"], 
    ["nat", "tan"],
    ["bat"]
]

#사전지식
문자열 합치기 join() 함수 사용법 숙지
정렬함수 sorted(), sorted(data, key = len) 숙지 : https://docs.python.org/ko/3/howto/sorting.html

#정렬방식 및 정렬 알고리즘별 시간 복잡도
 1. Quick 정렬
 2. 병합정렬 (Merged Sort)
 3. TimSort
'''

import re
import collections  

def groupAnagrams(strs):
    # list를 value로 하는 dictionary 생성함.
    anagrams = collections.defaultdict(list)
    #print(anagrams)

    for word in strs:
        # ''.join(sorted(word)) ==> 정렬을 하였을 경우 Anagram에 해당하면 그 단어를 동일한 key를 가진 list에 추가함.
        anagrams[''.join(sorted(word))].append(word)
    return anagrams

    
if __name__ == "__main__":
    data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    datajoin = "-".join(data)
    print('"-".join 사용법 = ', datajoin)
    datajoin = "".join(data)
    print('"".join 사용법 = ', datajoin)
    datajoin = ".".join(data)
    print('".".join 사용법 = ', datajoin)

    result = groupAnagrams(data)
    print(result)