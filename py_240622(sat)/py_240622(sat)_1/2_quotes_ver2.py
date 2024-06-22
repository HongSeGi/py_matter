import random as rd

file_path = "./quotes.txt"  #파일경로 > './': 현재 디렉토리, '../' : 이전디렉토리  >> 상대경로
# C:\windows\path >> 절대 경로. (프로그램 실제에서는 절대경로를 추천한다.)

quotes = []

file = open(file_path, 'r', encoding= 'utf-8') #open 원형태(파일, 옵션, 엔코딩 옵션) #cp949로 했을때 안돼서 utf-8로 바꿔준거임.
for line in file:
    quotes.append(line.strip()) #한줄 불러온거 리스트에 추가. 단, 문장 앞뒤 공백 모두 삭제.

file.close() #불러온 파일 닫기.

print("#"*100)
print("# 오늘의 명언 #")
print("#"*100)
print()
dailyQuote = rd.choice(quotes)
print(dailyQuote)