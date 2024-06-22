fruit_lst = ["Apple", "banana", "Pineapple", "Blueberry", "Mango"]

max_idx = []
max_len, cnt = 0, 0
#가장 긴 문자열의 길이 찾기
for fruit in fruit_lst:
    if max_len <= len(fruit):
        max_len = len(fruit)        # > 문자열의 길이가 가장 큰 값을 찾아서 하나의 변수로 저장.
# 가장 긴 문자열의 위치 찾기
for fruit in fruit_lst:
    if max_len == len(fruit):
        max_idx.append(cnt)         # > 그 변수로 다시 리스트를 돌려서 동일하면 새로만든 리스트에 추가.
    cnt += 1        # > 얘는 fruit_lst의 각 요소의 인덱스를 써먹으려고 같이 요소가 이동하면서 같이 증가시키는거.
# 가장 긴 문자열 삭제
max_idx.reverse()
for incnt in max_idx:
    del fruit_lst[incnt]
print(fruit_lst)


# 이거하고 wordcloud 넘어갔다.