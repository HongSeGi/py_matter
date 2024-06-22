print("사전 프로그램 시작... 종료는 q를 입력")
dictionary = {"Apple" : "사과", "banana" : "바나나"}

while True:
    st = input('$ ')
    command = st[0]
    if command == '<':
        st = st[1:]
        inputStr = st.split(":")
        print(inputStr)
        if len(inputStr) < 2:
            print("입력 오류가 발생했습니다.")
        else:
            dictionary[inputStr[0].strip()] = inputStr[1].strip()
    elif command == '>':
        st = st[1:]
        inputStr = st.strip()
        if inputStr in dictionary:
            print(dictionary[inputStr])
        else:
            print('{}가 사전에 없습니다.'.format(inputStr))
    elif command == 'q':
        break
    else:
        print('입력 오류가 발생했습니다.')
print('사전 프로그램을 종료합니다.')

# 결국 오류잡아내지못했고 다시해보면서 오류 잡는다. >> 코드 흐름상의 문제 또는 문법적오류가 아닌 입력방식을 정확히 의도대로 입력하지않으면,
# 프로그램이 의도대로 흘러가지않게 처리가 진행된다는 점이 그 '오류'라는 것이었다.

# 따라서 개발자의 의도대로 사용자가 입력하지않았을경우에 그것을 바로잡기위해서는 어떻게 코드를 수정해야할까를 고민해보고 더나아가
# 의도치않은입력이 발생해도 잘 돌아가게끔 직접 코드수정작업을 해보는것 해본다.