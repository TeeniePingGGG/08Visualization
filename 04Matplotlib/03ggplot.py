import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 깨짐방지 설정
font_path = '../resData/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 엑셀 파일을 데이터프레임으로 변환
df = pd.read_excel("../resData/시도별_전출입_인구수.xlsx", engine='openpyxl', header=0)
df = df.fillna(method='ffill')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({"전입지별": "전입지"}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

sr_one = df_seoul.loc['경기도']

''' 그래프 스타일 지정: ggplot과 같은 스타일은 URL 참조
https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html '''
plt.style.use('ggplot')
# plt.style.use('dark_background')

# 그래프 사이즈 설정
plt.figure(figsize=(14, 5))
# x축 라벨 각도 및 크기
plt.xticks(rotation='vertical')
# 그래프에 마커와 마커사이즈를 지정하여 꺽은선 부분에 표시
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)

# 그래프의 제목과 라벨 표시 및 폰트크기 설정
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')

# 범례 표시 및 폰트 크기 설정
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)

plt.show()
