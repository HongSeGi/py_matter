# def add(a=3, b=7):
#     return a+b

# print(add())
# print(add(a=17))
#------------------------------------

# def add(*args):
#     print(type(args))
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(add(10, 20, 30, 40, 50))
# print(add(5))
#--------------------------------------

def max_min(choice, *args):
    if choice == "max":
        return(max(args))
    elif choice == 'min':
        return(min(args))

print(max_min("max", 15, 47, 23, 46, 17, 3, 6))
print(max_min("min", 15, 47, 23, 46, 17, 3, 6))