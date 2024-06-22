from wordcloud import WordCloud
import matplotlib.pyplot as plt

file = open(".\quotes.txt", 'r', encoding='utf-8')  #파일불러오고 대기상태.
text = file.read() #quotes.txt파일 안의 데이터를 가져온다.
#한글텍스트는 결과에 표시가 안돼서 > 구글번역기로 영어로 바꾼작업을 한 다음에 다시 돌렸다.

#워드클라우드 생성하는 부분.
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

#워드클라우드 출력하는 부분.
plt.figure(figsize=(10, 5)) #10, 5는 비율임.
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()