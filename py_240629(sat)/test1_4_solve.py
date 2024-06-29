def create_dic(cnt):
    name = f"학생{cnt}" #학생이름생성
    kor = int(input(f"{name}의 국어 점수: "))
    eng = int(input(f"{name}의 영어 점수: "))
    mat = int(input(f"{name}의 수학 점수: "))
    return {'name': name, '국어': kor, '영어': eng, '수학': mat}

def add_student_to_list(student_dic, students_scores):
    students_scores.append(student_dic)

def calculate_total(students_scores, keys):
    total = 0
    for student in students_scores:
        for key in keys:
            total += student[key]
    return total

def print_totals(students_scores):
    # 과목별 총점 계산 및 출력
    subjects = ['국어', '영어', '수학']
    for subject in subjects:
        total = calculate_total(students_scores, [subject])
        print(f"{subject} 총점: {total}")
    
    # 학생별 총점 계산 및 출력
    for student in students_scores:
        student_total = calculate_total([student], ['국어', '영어', '수학'])
        print(f"{student['name']}의 총점: {student_total}")

students_scores = []
for i in range(1, 6):
    student_dic = create_dic(i)
    add_student_to_list(student_dic, students_scores)

print_totals(students_scores)



