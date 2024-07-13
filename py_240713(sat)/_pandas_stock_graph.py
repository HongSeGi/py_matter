# import pandas_datareader.data as web
# import datetime as dt

# start = dt.datetime(2020, 1, 1)
# end = dt.datetime(2022, 3, 30)

# data = web.DataReader('FB', 'yahoo', start, end)
## FB = Facebook 종목 이름
## yagoo = API 사용처
## start = 정보 수집 시작일
## end = 정보수집 종료일

# print(data.head())
## High : 고가
## Low : 저가
## Open : 개장가
## Close : 마감가
## Volume : 거래량
## Adj Close : 조정 종가
#-------------------------------------------
import yfinance as yf
import datetime as dt

# 시작일과 종료일 설정
start = dt.datetime(2020, 1, 1)
end = dt.datetime(2022, 3, 30)
'''
# Meta Platforms 주식 데이터를 Yahoo Finance에서 가져오기
data = yf.download('META', start=start, end=end)
#data = yf.download('^KS11', start=start, end=end) #얘는 코스피에서 가져올경우임.

#데이터출력
# print(data.head())
'''
#-------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

def get_code(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
    code = code.strip()
    return code

code_df = pd.read_csv('./data_4901_20240713.csv', encoding='CP949')  #http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201에서 주식전종목기본정보 csv파일 다운받은거임.
code_df = code_df[['단축코드', '한글 종목약명']]
code_df = code_df.rename(columns={'단축코드':'code', '한글 종목약명': 'name'})
code_df.code = code_df.code.apply(pd.to_numeric, errors='ignore')
code_df.code = code_df.code.apply(lambda x: str(x).zfill(6))

code = get_code(code_df, '삼성전자')
print(code)
# yahoo의 주식데이터 등록은 코스피는 .KS, 코스닥은 .KQ가 붙는 특징이 존재
code = code + '.KS'
# yfinance를 사용하여 주식 데이터 가져오기
data = yf.download(code, start=start, end=end)
# High : 고가 Low : 저가 Open : 개장가 Close : 마감가 Volume : 거래량 Adj Close : 조정 종가
data['Close'].plot()
data['Open'].plot()
plt.show()