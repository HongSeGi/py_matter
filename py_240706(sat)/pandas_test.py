import pandas as pd
import datetime as dt

subway_df = pd.read_csv('./Seoul_Subway_Boarding_data/seoul_subway_daily_boarding_2015_2019.csv')

# print(subway_df)
# print(subway_df.head())
# print(subway_df.info())
# print(subway_df.describe())
# print(subway_df[subway_df.RIDE_PASGR_NUM < 10])
# print(subway_df[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']].mean())

theday = pd.to_datetime(subway_df.USE_DT, format= '%Y%m%d')
subway_df['year'] = theday.dt.year
subway_df['month'] = theday.dt.month
subway_df['day'] = theday.dt.day
wday = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}
subway_df['wday'] = theday.dt.dayofweek.map(wday)
# print(subway_df)
# df_2015 = subway_df[subway_df['year']==2015]
# df_2016 = subway_df[subway_df['year']==2016]
# df_2017 = subway_df[subway_df['year']==2017]
# df_2018 = subway_df[subway_df['year']==2018]
# df_2019 = subway_df[subway_df['year']==2019]
# print(df_2015[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']].mean())
# print(df_2016[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']].mean())
# print(df_2017[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']].mean())
# print(df_2018[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']].mean())
# print(df_2019[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']].mean())

# print(subway_df[subway_df['RIDE_PASGR_NUM']>subway_df['ALIGHT_PASGR_NUM']])
# print(subway_df[subway_df['RIDE_PASGR_NUM']<=subway_df['ALIGHT_PASGR_NUM']])

# sub_inout = subway_df[['LINE_NUM', 'SUB_STA_NM', 'RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']]
# print(sub_inout.head())
# print(sub_inout.tail())

sub_inout = subway_df[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']]
print(sub_inout-sub_inout.min()) # 각 컬럼의 기준점을 0으로 변경시키는 작업을 한다. > 데이터 전처리방법중에 하나이다.