def add(a, b):
    return a+b

# num_1, num_2 = map(int, input().split())
# print(add(num_1, num_2))
#-----------------------------------------

def say():
    str_v = "안녕하세요. 챗봇입니다."
    return str_v

# print(say())
#-----------------------------------------

def result(prt):
    print("계산 결과는 {0}입니다.".format(prt))

num_1, num_2 = map(int, input().split())
result(add(num_1, num_2))