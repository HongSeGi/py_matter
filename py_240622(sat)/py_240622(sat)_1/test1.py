
num_list = []

# 데이터 입력부
while 1:
    input_num = int(input("정수 한개 입력: "))

    if input_num == 0:
        break
    else:
        num_list.append(input_num)
# 데이터 출력부 > 이거는 처음에 입력된 다섯개만 가져오는거.
# if len(num_list) <= 5:
#     for i in num_list:
#         print(i)
# else:
#     for i in range(5):
#         print(num_list[i], end=' ')

# 데이터 출력부(선생님 답안 버전) > 마지막에 입력된 5개를 가져오는거로 하셨다.
if len(num_list) <= 5:
    for i in num_list:
        print(i)
else:
    for i in range(5):
        print(num_list[len(num_list)-(5-i)])