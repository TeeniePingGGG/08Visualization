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

col_years = list(map(str,range(2010,2018)))
df4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],col_years]

# 행과 열을 정치
df4 = df4.transpose()
# 스타일 설정
plt.style.use('ggplot')
# 데이터프레임의 인덱스를 정수형으로 변경
df4.index = df4.index.map(int)

# 막대 그래프를 세로형(수직방향)으로 생성. 막대의 두께와 색깔을 설정.
df4.plot(kind='bar',figsize=(20,10), width=0.7,
         color=['orange','green','skyblue','blue'])

# 라벨 및 범위 설정
plt.title('서울 -> 타시도 인구 이동',size=30)
plt.ylabel('이동 인구 수',size=20)
plt.xlabel('기간',size=20)
plt.ylim(5000,30000)
plt.legend(loc='best', fontsize=15)

plt.show()
