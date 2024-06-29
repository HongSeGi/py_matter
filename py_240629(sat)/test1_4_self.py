
# subject_score = {
#     "국어" : 0,
#     "영어" : 0,
#     "수학" : 0,
#     "총합" : 0
# }

student_dict = {}

for i in range(5):

    input_name = input("학생이름 입력: ")

    student_dict[input_name] = list(map(int, input("국어, 영어, 수학 점수 입력: ").strip().split(" ")))

# print(student_dict)

for name, score in student_dict.items():

    student_dict[name].append(sum(score))

# print(student_dict)

for name, score in student_dict.items():
    pass


# 망..ㅋㅋ