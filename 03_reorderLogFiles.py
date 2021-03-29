# 1. logs 변수에 저장된 문자열이 있는데 식별자가 숫자인지, 문자인지 식별
# 2. 문자로 구성된 로그는 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 주지 않으나 문자가 동일할 경우 식별자 순으로 정렬한다.
# 4. 숫자 로그는 입력 순서대로 한다.

# logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero" ]
# output = [ "let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

# lambda 함수를 알아야 한다.

str1 = "dig1 8 1 5 1"
key = lambda x : (x.split()[1:], x.split()[0])
print(key(str1))


def reorderLogFiles(logs):
    letters, digits = [], []
    for log in logs:
        if(log.split()[1].isdigit()) :
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
    return letters + digits


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero" ]
    output = reorderLogFiles(logs)
    print(output)