# 데이터프레임 사용을 위한 모듈
import pandas as pd
# 데이터 시각화를 위한 모듈
import  matplotlib.pyplot as plt

''' 엑셀파일을 데이터프레임으로 변환. header가 0이므로 첫번쨰 행은 타이틀로
인식하여 제외한다. '''
df = pd.read_excel("../resData/시도별_전출입_인구수.xlsx", engine='openpyxl', header=0)
print(df)

# 누락값(NaN)을 앞 부분의 데이터로 채워준다.
df = df.fillna(method='ffill')
# NaN이 '전국'으로 대체된다.
''' 데이터는 일반적으로 근접한 것까리 관련이 높을 수 있으므로 누락값은
보통 이런 방식으로 대체하게된다. '''
print(df.head())

'''
'전출지별'에서는 '서울특별시'만 추출
'전입지별'에서는 '서울특별시'가 아닌 데이터만 추출한다.
즉 서울에서 다른 지역으로 전출한 데이터만 남게된다
'''
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')

# 위의 조건을 데이터프레임에 적용한다.
df_seoul = df[mask]

''' 전출지별 컬럼(열)을 삭제한다. 축 옵션을 1로 설정했다. inplace 옵션이
없으므로 변경된 새로운 객체를 반환한다.'''
df_seoul = df_seoul.drop(['전출지별'], axis=1)

# 컬럼명을 변경한 후 원본 데이터프레임을 저장한다.
df_seoul.rename({"전입지별":"전입지"},axis=1,inplace=True)

# '전입지' 컬럼을 인덱스로 설정한다. 설정 전에는 정수형 인덱스가 부여된다.
df_seoul.set_index('전입지',inplace=True)
print(df_seoul)

''' 문자형 인덱스를 이용해서 서울에서 경기도호 전출한 행만 추출한다.
만약 숫자형 인덱스를 사용하려면 iloc를 사용한다.'''
sr_one = df_seoul.loc['경기도']
print(sr_one)
# 여기까지 데이터 전처리를 완료함

# 그래프의 x,y축에 데이터를 적용
plt.plot(sr_one.index, sr_one.values)

# 그래프의 제목과 x,y축의 라벨을 추가
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')

plt.show() # 모든 변경사항을 저장한 후 그래프 출력