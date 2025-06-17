import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = '../resData/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel("../resData/시도별_전출입_인구수.xlsx", engine='openpyxl', header=0)
df = df.fillna(method='ffill')
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({"전입지별": "전입지"}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

'''
map 함수를 통해 1970~2017까지의 문자열로 구성된 리스트를 생성한다.
map의 첫번쨰 인수는 str함수이므로 범위만큼 반복하면서 호출하게된다.
'''
col_years = list(map(str, range(1970, 2018)))

# 서울에서 각 3개의 도로 이동한 데이터 추출. 기간은 1970~2017로 설정
df3 = df_seoul.loc[['충청남도','경상북도','강원도'],col_years]

# 스타일 설정 및 Axe 객체 1개 생성
plt.style.use('ggplot')
fig = plt.figure(figsize=(20,5))
axe = fig.add_subplot(1,1,1)

'''
1개의 그래프에 3개의 꺽은선을 추가한다.
x축은 기간으로 설정
y축은 df3.loc['충청남도',:] -> 충남 행의 전체기간을 선택
'''
axe.plot(col_years, df3.loc['충청남도',:], marker='o', markerfacecolor='green',
         markersize=10, color='olive', linewidth=2, label='서울 -> 충남')

axe.plot(col_years, df3.loc['경상북도',:], marker='o', markerfacecolor='blue',
         markersize=10, color='skyblue', linewidth=2, label='서울 -> 경북')

axe.plot(col_years, df3.loc['강원도',:], marker='o', markerfacecolor='red',
         markersize=10, color='magenta', linewidth=2, label='서울 -> 강원')

# 범례, 타이틀, 라벨, 기울기 등 설정
axe.legend(loc='best')
axe.set_title('서울->충남, 경북, 강원 인구 이동',size=20)
axe.set_xlabel('기간',size=12)
axe.set_ylabel('이동인구수',size=12)
axe.set_xticklabels(col_years, rotation=90)

# 각 축의 눈금 라벨크기 설정
axe.tick_params(axis='x', labelsize=10)
axe.tick_params(axis='y', labelsize=10)

plt.show()