
# input_nums_list = input("세자리 이하의 정수 연속으로 입력: ").strip().split(" ")

# for i in range(len(input_nums_list)):
#     input_nums_list[i] = int(input_nums_list[i])

# for i in input_nums_list:
#     if i//100 > 0:
#         input_nums_list.remove(i)
#     else:
#         pass

# print(input_nums_list)


# print("최댓값 :", max(input_nums_list))
# print("최솟값 :", min(input_nums_list))


#선생님 답안.
input_lst = list(map(int, input().split())) #>리스트를 형변환시킬때 map쓰는건가.
print(max(input_lst), min(input_lst))


#선생님 답안.(내가 좀더 확인해본거)
input_lst = map(int, input("정수 연속입력:").split())
print(input_lst)
print(type(input_lst))
input_lst = list(input_lst)
print(max(input_lst), min(input_lst))









