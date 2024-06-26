cs_fruit = {}
state = 0

while True:
    match state:
        case 0: #메뉴 출력
            print("1: 과일등록\n2: 전체메뉴\n3: 과일 찾기\n4: 종료\n")
            state = int(input())
        case 1: #과일 등록
            input_fruit = input("과일의 이름을 입력하세요: ")
            input_price = int(input("과일의 가격을 입력하세요: "))
            cs_fruit[input_fruit] = input_price
            state = 0
        case 2: #과일 전체 출력, 문제 3번
            cs_fruit = dict(sorted(cs_fruit.items(), key = lambda x: x[1]))
            for fruit, price in cs_fruit.items():
                print(fruit, ":", price)
            state = 0
        case 3: #입력 과일 출력, 문제 2번
            input_fruit = input("가격이 궁금한 과일의 이름을 입력하세요: ")
            if input_fruit in cs_fruit:
                print(f"{input_fruit}의 가격은 {cs_fruit[input_fruit]}입니다.")
            else:
                print("없는 과일 입니다.")
            state = 0
        case 4: #종료
            break
        case _: #잘못된 입력
            print("잘못된 입력 값입니다.")
            state = 0


#과일등록할때 과일명을 잘못입력하거나 과일명이 아닌 단어를 입력해도 과일메뉴에 등록시켜버리는 문제가 있다.
#이를 해결하기위해선 > 잘못입력한 키와 그에 해당하는 value값을 삭제시키는 메뉴를 만들거나,
#       또는, 세상 모든 과일에 대한 리스트를 만들어놓고, 만약 입력한 과일명이 해당리스트에 없다면 오류를 발생시켜 다시 입력하게끔 회귀시켜서 하면 되겠다.

#따라서 과일명을 잘못 입력한것에 대한 문제는 크게 어렵지않게 해결할수있다.

#선생님이 제시한 솔루션에서의 포인트는 내가 하나의 기계를 만들었다고 가정하고, 사용자가 모든 기능중에서 선택해서 해당 기능만 서비스를 제공하도록 만들어야하는것이다.
#그래서 서로다른 기능들을 case단위로 나눠서 애초에 사용자가 진입할때 어떤 case를 쓸것인지 선택하게끔하고 해당 관련 기능을 실행시키는 방향으로 서비스프로그램이 진행되게 한다.

#나는 일단 과일명을 입력할때 오류가 나지않게끔하는데에 초점을 맞추고, 목록에 없으면 추가시키는 기능까지는 고려하지않은탓에,
#정해놓은 과일키값에 대응되게끔만 입력하게끔되어있어서 다소 답답한 느낌이 있긴하다.
#새로운 데이터가 들어왔을때에 대한 대응. 새로운 키값데이터가 들어왔을때의 대응. 해당 키가 제대로된 키값에 해당하는지 판별하는 대응. 이런것들을 고려해서
#집약해서 만들면 나쁘지않은 서비스프로그램을 나도 충분히 만들수 있다는 확신이 든다.




##이거하고 CV2넘어감.