import pandas as pd

data = {
    'name':['Jerry','Riah','Paul'],
    'algol':['A','A+','B'],
    'basic':['C','B','B+'],
    'c++':["B+","C","C+"]
}

# 데이터 프레임으로 변환 후 name컬럼을 인덱스로 저장
df = pd.DataFrame(data)
df.set_index('name',inplace=True)
print(df)

# 데이터 프레임을 csv파일로 저장
df.to_csv("../saveFiles/hakjum.csv")