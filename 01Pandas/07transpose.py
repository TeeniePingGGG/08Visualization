import pandas as pd

exam_data = {'이름':['서준','우현','인아'],
             '국어':[90,80,70],
             '영어':[98,89,95],
             '음악':[85,95,100],
             '체육':[100,90,90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

'''
전치: 데이터프레임의 행과 열을 교환하는 것을 말한다
'''
# 함수를 통해 전치한 후 반환값을 지정
df = df.transpose()
print(df)
print('\n')

# 클래스 속성을 활용해서 한번 더 전치
df = df.T
print(df)