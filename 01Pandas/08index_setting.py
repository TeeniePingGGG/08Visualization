import pandas as pd

# 새로운 딕셔너리 선언
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
             'c3':[10,11,12], 'c4':[13,14,15]}

# 3행 5열인 데이터프레임으로 변환. 이때 인덱스 지정
df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(f"{'최초 출력':-^30}")
print(df)

# 새로운 인덱스로 사용할 리스트 선언
new_index1 = ['r0','r1','r2','r3','r4']
# 인덱스를 재지정하는 경우 새롭게 생성된 인덱스에는 NaN이 채워진다.
new_df2 = df.reindex(new_index1)
print(f"{'인덱스 재지정 후 출력':-^30}")
'''
NaN: Not a Number의 이니셜로 직역하면 숫자가 아니다라는 뜻을
    가지고 있다. 유효한 값이 존재하지 않는 누락데이터를 의미한다.
'''
print(new_df2)

# 완전히 새로운 인덱스로 재지정하면 모든 데이터가 NaN으로 초기화된다.
new_index2 = ['kor','eng','math','music','physical']
subject_df = df.reindex(new_index2)
print(f"{'인덱스 재지정 후 출력':-^30}")
print(subject_df)

# fill_value를 사용하면 의미있는 데이터로 초기화 할 수 있다.
new_df3 = df.reindex(new_index1,fill_value=0)
print(f"{'fill_value 사용 후 출력':-^30}")
print(new_df3)

'''행 인덱스를 정수형 인덱스로 초기화한다. 이때 기존 행 인덱스는  
컬럼으로 이동한다'''
new_df4 = df.reset_index()
print(f"{'인덱스 초기화 후 출력':-^30}")
print(new_df4)

# c0 컬럼은 삭제된 후 인덱스로 사용된다.
new_df5 = df.set_index('c0')
print(f"{'c0을 인덱스로 지정':-^30}")
print(new_df5)

# 삭제된 c0 컬럼이 복원되면서 숫자형 인덱스로 변경된다.
new_df6 = new_df5.reset_index()
print(f"{'인덱스 초기화 후 출력':-^30}")
print(new_df6)

# 행 인덱스를 기준으로 내림차순 정렬
sort_df1 = new_df3.sort_index(ascending=False)
print(f"{'인덱스를 내림차순으로 정렬':-^30}")
print(sort_df1)

# 특정 컬럼을 지정하고 싶다면 by옵션을 사용
sort_df2 = new_df3.sort_values(by='c4', ascending=True)
print(f"{'c4컬럼을 오름차순 정렬':-^30}")
print(sort_df2)
