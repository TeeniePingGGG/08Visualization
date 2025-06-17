import pandas as pd

'''
read_execel(): 엑셀을 데이터프레임으로 변환
    첫행은 타이틀로 인식하므로 header=0 이 디폴트 값이다.
    또한 엑셀을 읽어오기 위해 openpyxl 패키지 설치가 필요하다.
'''
df1 = pd.read_excel('../resData/남북한_발전_전력량.xlsx',
                    engine='openpyxl')
print(df1)
print("="*30)

'''
header=1은 인덱스 1 즉, 1행을 타이틀로 간주하겠다는 의미이므로
2행부터는 타이틀로 인식되어 데이터 프레임으로 변환한다. 
'''
df2 = pd.read_excel('../resData/남북한_발전_전력량.xlsx',
                    engine='openpyxl', header=1)
# print(df2)
print("="*30)

'''
데이터를 가져오는 것은 df1과 동일하지만 타이틀이 없는 것으로
간주되어 정수형 컬럼명이 타이틀로 지정된다.
'''
df3 = pd.read_excel('../resData/남북한_발전_전력량.xlsx',
                    engine='openpyxl', header=None)
print(df3)
print("="*30)

# header옵션이 없으므로 0으로 지정되어 첫번쨰 행이 컬럼이 된다.
df4 = pd.read_excel('../resData/남북한_발전_전력량.xlsx',
                    engine='openpyxl')
print(df4)
print("="*30)

# 데이터 프레임 변경 시작
'''
5~8행까지의 데이터를 삭제한다. 즉 북한의 데이터를 모두 삭제하고
남한의 데이터만 남긴다.
'''
new_df = df4.drop(df4.index[5:9])
print(new_df)
print("="*30)

'''
전력량 컬럼을 삭제한다. 축(axis)옵션을 부여하면 행이 아닌 컬럼을 
삭제한다. 만약 해당 옵션이 없으면 행이 삭제된다.
'''
new_df = new_df.drop(['전력량 (억㎾h)'], axis=1)
print(new_df)
print("="*30)

# 컬럼명 변경: 축 옵션을 부여해야 컬럼명이 변경된다.
new_df = new_df.rename({'발전 전력별':'전력구분'},axis=1)
print(new_df)
print("="*30)

'''
앞에서 이름을 변경한 '전력구분' 컬럼을 인덱스로 지정한다.
원본 데이터프레임을 변경하기 위해 inplace 옵션을 부여한다.
'''
new_df.set_index('전력구분',inplace=True)
print(new_df)

# 남한의 데이터만 남긴 상태로 저장한다.
new_df.to_excel("../saveFiles/남한전력량.xlsx")

