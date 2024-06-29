import test_func as tfunc

# def square_subt(x, y):
#     return x**2 - y**2

num1, num2 = map(int, input("두개의 정수 입력 : ").strip().split(" "))
result = tfunc.square_subt(num1, num2)
print(f"결과 : {num1}^2 - {num2}^2 = {result}")
