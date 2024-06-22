fruits = {"사과" : 0, "배" : 0, "수박" : 0, "귤" : 0, "딸기" : 0, "포도" : 0}

for fruit_name, price in fruits.items():
    fruits[fruit_name] = int(input(f"{fruit_name} 가격 입력 : "))
print("-------------과일목록-------------")
for fruit_name, price in fruits.items():
    print(f"{fruit_name} : {price}원")
print("-------------과일가격정보------------")

while 1:
    input_fruit = input("Q. 과일명을 입력하세요 : ")
    if input_fruit == 'N' or input_fruit == "n":
        print("프로그램을 종료합니다.")
        break
    
    elif input_fruit not in fruits.keys():
        print("과일 목록에 없습니다. 과일명을 올바르게 입력해주세요")
        continue
    

    for fruit_name, price in fruits.items():
        if input_fruit == fruit_name:
            print(f"> {fruit_name}의 가격은 {price}원 입니다.")

    print("계속 하시려면 과일명을, 종료하시려면 n을 입력해주세요")

sorted_fruits = dict(sorted(fruits.items(), key=lambda x: x[0]))

for fruit_name, price in sorted_fruits.items():
    print(f"{fruit_name} : {price}원")

