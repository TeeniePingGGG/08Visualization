import pandas as pd

''' HTMl파일의 경로 혹은 웹URL을 통해 읽어온 웹페이지의 표(table)를
가져와서 데이터프레임으로 변환한다. '''
url = "../resData/sample.html"
tables = pd.read_html(url)

# 샘플 파일에는 테이블이 2개 존재함
print('테이블 갯수:',len(tables))

# 테이블의 갯수만큼 반복하여 내용 출력
for i in range(len(tables)):
    print("## tables[%s] ##"%i)
    # 테이블을 데이터프레임으로 변환한 내용이 여기서 출력됨
    print(tables[i])
    print("="*30)

# 두번쨰 테이블을 변수에 저장
df = tables[1]
# name컬럼을 인덱스로 지정한 후 원본에 적용
df.set_index(['name'], inplace=True)
print(df)
print("="*30)

'''
웹페이지의 테이블을 가져오려면 lxml 패키지가 설치되어 있어야 한다.
pip install lxml
설치 및 모듈 임포트 후 사용할 수 있다. 
'''
url = 'https://pann.nate.com/talk/c20023?page=1'
tables = pd.read_html(url)
# 이 페이지에는 테이블이 하나만 있으므로 1이 출려됨
print('테이블 갯수:',len(tables))
print("="*30)

# 0번 인덱스로 테이블을 가져온 후 변수에 저장
boardTable = tables[0]
print(boardTable)
print("="*30)

# columns 속성을 이용해서 데이터프레임에 컬럼명을 지정한다.
boardTable.columns = ['제목','작성자','조회수','작성일']
print(boardTable)
