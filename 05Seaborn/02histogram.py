import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('darkgrid')

# 3개의 영역으로 구분하기 위해 와이드하게 사이즈 지정
fig = plt.figure(figsize=(15,5))

# 수평방향으로 3개의 Axe객체 생성
axe1 = fig.add_subplot(1,3,1)
axe2 = fig.add_subplot(1,3,2)
axe3 = fig.add_subplot(1,3,3)

'''
히스토그램: 도수분포표를 그래프로 표현한것. 변수가 하나인 단변수
    데이터의 빈도수를 표현한다. x축을 같은 크기의 여러 구간으로 나누고
    각 구간에 속하는 데이터의 갯수를 y축에 표시한다
도수분포표: 도수 분포는 표본의 다양한 산출 분포를 보여주는 것으로
    가령 성인 30명을 대상으로 하루에 사용하는 문자의 건수를 조사하여
    10~20건, 20~30건에 몇명이 분포하는지 표시한다.
커널밀도그래프: 주어진 데이터를 정규화시켜 넓이가 1이 되도록 그린 그래프
'''

# 히스토그램 + 커널밀도그래프를 동시에 출력
sns.distplot(titanic['fare'],ax=axe1)
# 커널밀도그래프
sns.kdeplot(x='fare',data=titanic, ax=axe2)
# 히스토그램
sns.histplot(x='fare',data=titanic,ax=axe3)

# 타이틀 설정
axe1.set_title('titanic fare - hist/ked')
axe2.set_title('titanic fare - ked')
axe3.set_title('titanic fare - hist')

plt.show()
