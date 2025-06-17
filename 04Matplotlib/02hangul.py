import pandas as pd
import  matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트메니져 임포트
from matplotlib import font_manager,rc
# 폰트 경로 설정
font_path = '../resData/malgun.ttf'
# 폰트 파일의 이름을 속성으로 지정
font_name = font_manager.FontProperties(fname=font_path).get_name()
# 폰트 적용
rc('font',family=font_name)

# 엑셀파일에서 서울 > 경기도로 이동한 데이터만 추출
df = pd.read_excel("../resData/시도별_전출입_인구수.xlsx", engine='openpyxl', header=0)
print(df)

df = df.fillna(method='ffill')
print(df.head())

# 서울에서 경기로 전출할 데이터만 추출
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')

df_seoul = df[mask]

df_seoul = df_seoul.drop(['전출지별'], axis=1)

df_seoul.rename({"전입지별":"전입지"},axis=1,inplace=True)

df_seoul.set_index('전입지',inplace=True)
print(df_seoul)

sr_one = df_seoul.loc['경기도']
print(sr_one)

# 그래프 이미지의 전체 사이즈 지정. 14:5로 비율을 설정한다.
plt.figure(figsize=(14,5))

# x축 라벨을 수직 방향으러 설정. 텍스트가 겹치는 부분 처리
# plt.xticks(rotation='vertical')
# plt.xticks(rotation=90) 90인 경우 vertical과 동일
plt.xticks(rotation=300) # 정수형으로 기술할 수 있음

# 그래프 설정
plt.plot(sr_one.index, sr_one.values)
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')

# 범례 표시(그래프의 우상단에 설명 문구가 추가됨)
plt.legend(labels=['서울 -> 경기'], loc='best')

plt.show()