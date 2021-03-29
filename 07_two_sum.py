# 선형 자료구조
# Data 요소가 순차적으로 배열되는 자료구조를 말함
# array, stack, queue, linked list

# 자료 구조는 연속된 메모리 공간(Contiguous) 과 포인터로 연결된 link 방식으로 나뉨
# python에서는 C의 배열처럼 정적배열을 제공하지 않고 동적배열인 list를 제공함 (Java ArrayList, C++ std::vector)
# 동적으로 배열의 크기를 늘려가는 재할당 비율(growth factor)는 언어마다 다름. python : 1.125, ArrayList : 1.5, C++ 2배

# in_num = [2, 7, 11, 15]
# target = 9
# output = [0, 1]

# Brute-Force
def brute_force1(data, target: int):
    indexlist = []
    ptr1, ptr2 = 0, 1
    while(ptr1 < len(data)-1):
        print(ptr1, ptr2)
        while(ptr2 < len(data)):
            print("ptr1={0}".format(ptr1), ptr2)
            if(data[ptr1] + data[ptr2] == target):
                indexlist.append([ptr1, ptr2])
            ptr2 += 1
        ptr1 += 1
        ptr2 = ptr1+1

    print("1's return id = ", id(indexlist))
    return indexlist

def brute_force2(data, target: int):
    indexlist = []
    for i in range(len(data)-1):
        print("i = ", i)
        for j in range(i+1, len(data)):
            print(i, j)
            if(data[i] + data[j] == target):
                indexlist.append([i, j])

    print("2's return id = ", id(indexlist))
    return indexlist

# in을 이용한 탐색 (보수를 구한다음 보수가 있는지 찾는다.)
def use_in_method(data, target: int):
    indexlist = []
    for index, value in enumerate(in_num) : 
        complement = target - value
        if complement in data[index+1:]:
            indexlist.append([index, data[index+1:].index(complement)+(index+1)])

    return indexlist


# 첫 번째 수를 뺀 결과 키 조회
def twoSum1(data, target):
    indexlist = []
    nums_map = {}

    for i, num in enumerate(data):
        nums_map[num] = i
    
    # data = [2, 7, 11, 15]
    # nums_map = {2: 0, 7: 1, 11: 2, 15: 3}
    for i, num in enumerate(data):
        complement = target - num
        if(complement in nums_map and i != nums_map[complement]):
            if(sorted([i, nums_map[complement]]) not in indexlist) :
                indexlist.append([i, nums_map[complement]])

    return indexlist


# 조회구조 개선
def twoSum2(data, target):
    indexlist = []
    nums_map = {}

    # data = [2, 7, 11, 15]
    # nums_map = {2: 0, 7: 1, 11: 2, 15: 3}
    for i, num in enumerate(data):
        complement = target - num
        if(complement in nums_map and i != nums_map[complement]):
            if(sorted([i, nums_map[complement]]) not in indexlist) :
                indexlist.append([i, nums_map[complement]])
        nums_map[num] = i

    return indexlist


# two pointer 방식 : 사전 정렬 필요
def twopointer(data, target):
    indexlist = []
    i, j = 0, len(data) -1
    data.sort()
    print("data = ", data)
    while (i < j) :
        if(data[i] + data[j] > target):
            j -= 1
        elif(data[i] + data[j] < target):
            i += 1
        else:
            indexlist.append([i, j])
            break

    return indexlist


in_num = [2, 7, 11, 15]
target = 9

result = brute_force1(in_num, target)
print("brute_force1 = ", result)

result = brute_force2(in_num, target)
print("brute_force2 = ", result)

result = use_in_method(in_num, target)
print("use_in_method = ", result)

result = twoSum1(in_num, target)
print("twoSum1_method = ", result)

result = twoSum2(in_num, target)
print("twoSum2_method = ", result)

result = twopointer(in_num, target)
print("twopointer_method = ", result)

print("in_num = ", in_num)