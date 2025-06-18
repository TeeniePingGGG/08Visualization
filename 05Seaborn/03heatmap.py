import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('darkgrid')
'''
히트맵: 열을 뜻하는 heat와 지도를 뜻하는 Map을 결합한 단어로  
    색상으로 표현할 수 있는 다양한 정보를 일정한 이미지 위에
    열분포 형태의 비쥬얼한 그래픽으로 출력한다.
'''
'''
데이터프레임을 피벗테이블로 정리할때 성별(sex)을 행 인덱스로
좌석등급(class)를 열의 이름으로 설정한다. aggfunc옵션은 데이터값의
크기를 기준으로 집게한다는 의미
'''

'''
히트맵 그리기
    table: 데이터프레임을 피봇테이블로 정리한 변수
    annot: 데이터값 표시 여부(False면 표시하지 않음)
    fmt: 정수형(d) 포맷으로 설정
    cmap: 컬러맵
    cbar: 컬러바 표시여부(False 이면 표시하지 않음)
'''
tabel = titanic.pivot_table(index=['sex'],columns=['class'],aggfunc='size')

sns.heatmap(tabel, annot=True, fmt='d',cmap='YlGnBu', linewidths=.5,cbar=True)

plt.show()