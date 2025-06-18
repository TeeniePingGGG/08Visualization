import matplotlib.pyplot as plt
import seaborn as sns


# 씨본에서 제공하는 타이타닉 데이터셋 로드
titanic = sns.load_dataset('titanic')
print(titanic.head()) # 처음 데이터 5개 출력
print(titanic.tail(10)) #마지막 데이터 10개 출력
# print(titanic.info())
# print(titanic.describe())
# print(titanic.describe(include='object'))
# print(titanic['who'].value_counts())

# 스타일 테마 설정
sns.set_style('darkgrid')

# 그래프의 크기 지정
fig = plt.figure(figsize=(15,5))

# Axe 객체는 1행 2열로 지정한 후 가로형으로 2개의 그래프를 표현
axe1 = fig.add_subplot(1,2,1)
axe2 = fig.add_subplot(1,2,2)

'''
회귀(Regression): 통계학에서 변수들 간의 관계를 분석하고 예측하는데 사용되는 통계적
    방법을 의미
regplot(): 회귀선이 있는 산점도를 표현. 서로 다른 2개의 연속 변수 사이의
    산점도를 그리고 선형회귀 분석을 위한 회귀선을 출력
    회귀의 목적은 데이터에서 패턴을 학습해 새로운 데이터에 대한 예측을
    수행하는 것이다.
'''

# x축은 나이, y축은 운임요금을 표현
# fit_reg: 회귀선을 표시하기 위한 옵션으로 True가 디폴트
sns.regplot(x='age',y='fare',data=titanic, ax=axe1)
sns.regplot(x='age',y='fare',data=titanic, ax=axe2, fit_reg=False)

plt.show()
