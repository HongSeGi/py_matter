import test_func as tfunc

# def pyramid(num):
#     print("print")
#     for i in range(0, num, 1):
#         for j in range(num-1-i, 0, -1):
#             print(" ", end="")
#         for j in range(0, 2*i+1, 1):
#             print("*", end="")
#         print()

inputNum = int(input("input = "))

tfunc.pyramid(inputNum)
# tfunc.diamond(inputNum) #피라미드끝나고나서 해본거.

