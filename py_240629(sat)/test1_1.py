import test_func as tfunc

# def sum(num):
#     total = 0
#     for i in range(1, num+1):
#         total += i
#     return total

inputNum = int(input("정수 입력: "))
result = tfunc.sum(inputNum)
print(f"1부터 {inputNum}까지의 합 : {result}")