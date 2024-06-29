#버전1

# def my_sort(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
    
#     return lst

# num_lst = list(map(int, input().split()))
# print(my_sort(num_lst))

#--------------------------------------------

#버전2__옵션추가한거
def my_sort(lst, op = 0):
    n = len(lst)
    match op:
        case 0:
            for i in range(n):
                for j in range(0, n-i-1):
                    if lst[j] > lst[j+1]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
            return lst
        case 1:
            for i in range(n):
                for j in range(0, n-i-1):
                    if lst[j] < lst[j+1]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
            return lst
        case _:
            return "Error"

num_lst = list(map(int, input().split()))
print(my_sort(num_lst, op = 1))