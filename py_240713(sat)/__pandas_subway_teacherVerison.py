# https://github.com/w1004me/ezen_py/blob/main/pandas_test_0713.py
# 여기에서 가져옴.

import pandas as pd
import datetime as dt
import numpy as np

subway_df = pd.read_csv('./Seoul_Subway_Boarding_data/seoul_subway_daily_boarding_2015_2019.csv')
# print(subway_df)
# print(subway_df.head())
# print(subway_df.info())
# print(subway_df.describe())
# print(subway_df[subway_df.RIDE_PASGR_NUM < 10])

subway_df = subway_df.drop('WORK_DT', axis=1) #얘도 추가시킨거(해도되고 안해도되는거 > 쓸모없는거 안보게끔하려고(column이 엄청나게 많을때 특히나 유용하게쓰인다.))
# print(subway_df[['RIDE_PASGR_NUM','ALIGHT_PASGR_NUM']].mean())
subway_df['total'] = subway_df['RIDE_PASGR_NUM'] + subway_df['ALIGHT_PASGR_NUM']  #자료받고 추후 넣게된거.
theday = pd.to_datetime(subway_df.USE_DT, format='%Y%m%d')
subway_df['year'] = theday.dt.year
subway_df['month'] = theday.dt.month
subway_df['day'] = theday.dt.day
wday = {0:'월',1:'화',2:'수',3:'목',4:'금',5:'토',6:'일'}
subway_df['wday'] = theday.dt.dayofweek.map(wday)
# 각 연도별 데이터 프레임 생성
df_2015 = subway_df[subway_df['year'] == 2015]
df_2016 = subway_df[subway_df['year'] == 2016]
df_2017 = subway_df[subway_df['year'] == 2017]
df_2018 = subway_df[subway_df['year'] == 2018]
df_2019 = subway_df[subway_df['year'] == 2019]

# 각 데이터 프레임을 딕셔너리에 저장
dfs = {
    2015: df_2015,
    2016: df_2016,
    2017: df_2017,
    2018: df_2018,
    2019: df_2019
}

# 각 연도별 평균 출력
# for year, df in dfs.items():
    # print(year)
    # print(df[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']].mean())

#sub_inout = subway_df[['LINE_NUM','SUB_STA_NM','RIDE_PASGR_NUM','ALIGHT_PASGR_NUM']]
sub_inout = subway_df[['RIDE_PASGR_NUM','ALIGHT_PASGR_NUM']]
# print(sub_inout - sub_inout.min()) # 각 컬럼의 기준점을 0으로 변경시키는 작업 > 데이터 전처리 방법 중 하나
# print(sub_inout.corr())
# print(subway_df.LINE_NUM.unique())
# print(subway_df.SUB_STA_NM.unique())
# print(subway_df[subway_df.SUB_STA_NM=='서울역'])

line_name = np.sort(subway_df.LINE_NUM.unique())
# 'code'와 'name'이라는 열을 가진 DataFrame 'line_code'를 생성
# enumerate() 함수는 인자로 넘어온 목록을 기준으로 인덱스와 원소를 차례대로 접근하게 해주는 반복자를 반환해주는 함수
line_code = pd.DataFrame(list(enumerate(line_name)), columns=['code', 'name'])
# print(line_code)

## 'LINE_NUM'과 'SUB_STA_NM'의 유일한 조합을 추출하고 각 'LINE_NUM' 값의 개수를 계산합니다.
## drop_duplicates()는 중복된 행을 제거, LINE_NUM.value_counts()는 각 'LINE_NUM'값을 count
#subway_info = subway_df[['LINE_NUM', 'SUB_STA_NM']].drop_duplicates().LINE_NUM.value_counts()
## 'name'열을 기준으로 'subway_info'의 값을 'line_code' DataFrame에 매핑하여 'count'열을 추가
#line_code['역수'] = line_code.name.map(subway_info)
#print(line_code)

line_name_2015 = np.sort(df_2015.LINE_NUM.unique())
line_code = pd.DataFrame(list(enumerate(line_name_2015)), columns=['code', 'name'])
df_2015 = df_2015[['LINE_NUM', 'SUB_STA_NM']].drop_duplicates().LINE_NUM.value_counts()
line_code['역수'] = line_code.name.map(df_2015)
# print(line_code)

line_name_2019 = np.sort(df_2019.LINE_NUM.unique())
line_code = pd.DataFrame(list(enumerate(line_name_2019)), columns=['code', 'name'])
df_2019 = df_2019[['LINE_NUM', 'SUB_STA_NM']].drop_duplicates().LINE_NUM.value_counts()
line_code['역수'] = line_code.name.map(df_2019)
# print(line_code)

df_2019_1 = subway_df[(subway_df['year'] == 2019) & (subway_df['month'] == 1)]      # >조건에 맞는 정보만 가져오려고할때. 비트연산자인&를 쓴것이 특이점이다.
# print(df_2019_1)
df_2019_1.sort_values(by='total', ascending=False, inplace=True)
# print(df_2019_1.head(10))
df_2019_1_sum = df_2019_1.groupby('SUB_STA_NM').sum().sort_values(by='total', ascending=False, inplace=False)
# print(df_2019_1_sum['total'].head(10))

top10_station = df_2019_1.groupby('SUB_STA_NM').sum().sort_values(by='total', ascending=False)[['total']].head(10).index
# print(top10_station)

sort_station_top10 = df_2019_1.groupby('SUB_STA_NM')[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM', 'month', 'total']].mean().sort_values(by='total',ascending=False).head(10)
# print(sort_station_top10)

#피벗테이블생성
top10_station = sort_station_top10.pivot_table(index='month', columns='SUB_STA_NM', values= 'total')
# print(top10_station)

