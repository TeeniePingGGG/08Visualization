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


sr_one = df_seoul.loc['경기도']

'''
여러개의 Axe객체를 생성하여 서로 다른 그래프를 표현할 수 있다.
figure() 함수로 그림릐 틀을 만든 후 figsize 옵션으로 크기를 지정한다.
add_subplot() 함수를 그림의 틀로 분할한다. 여기서 분할된 틀을 Axe객체
라고 한다.
형식] add_subplot(행의 크기, 열의 크기, 서브플롯순서)
'''
plt.style.use('ggplot')
fig = plt.figure(figsize=(10, 10))
# 2행 1열 중 첫번째 Axe객체 생성
ax1 = fig.add_subplot(2,1,1)
# 두번쨰 객체 생성
ax2 = fig.add_subplot(2,1,2)

'''
marker: 마커를 표시한 선 그래프를 그려준다. 마커의 종류에는  
o, *, +, . 등이 있다.
markerfacecolor: 마커의 배경색
color : 마커의 컬러
'''
ax1.plot(sr_one, 'o', markersize=10)
ax2.plot(sr_one, marker='o', markersize=10, markerfacecolor='green',
         color='olive', linewidth=2, label='서울->경기')

ax2.legend(loc='best')

# y축의 범위
ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

# x축 눈금 라벨 지정 및 텍스트 회전 각도 설정
ax1.set_xticklabels(sr_one.index, rotation=70)
ax2.set_xticklabels(sr_one.index, rotation=-75)

plt.show()
