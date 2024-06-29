def abs_sum(lst):
    sum = 0
    for i in lst:
        i = i if i > 0 else -1*i
        sum += i
    return sum

num_lst = list(map(int, input().split()))
print(abs_sum(num_lst))