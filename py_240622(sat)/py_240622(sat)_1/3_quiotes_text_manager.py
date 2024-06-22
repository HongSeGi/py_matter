
file_path = "./quotes.txt"
file = open(file_path, 'a', encoding='utf-8')

new_quote = input('새로운 명언을 입력하세요:')
file.write('\n'+new_quote) #\n을 앞에 붙이지않으면 이전에 끝났던 행에 이어서 같은행에 추가가 되기때문에 앞에 \n 붙여준거다.
file.close()