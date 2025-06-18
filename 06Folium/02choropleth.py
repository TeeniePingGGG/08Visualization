import pandas as pd
import folium
import json

'''
Choropleth Map(코로프레스 맵)
    : 행정구역과 같이 지도상에 경계를 표시하기 위한 맵이다.
'''

# 경기 인구 데이터를 데이터 프레임으로 변환
file_path = '../resData/경기도_인구_데이터.xlsx'
df = pd.read_excel(file_path, index_col='구분', engine='openpyxl')

# 모든 컬럼을 문자형으로 변환
df.columns = df.columns.map(str)

'''
경기도 시군구 경계 정보를 가진 geo-json 파일을 불러온다.
행정구역이 위경도를 통해 표현되어있다.
'''
geo_path = '../resData/경기도_행정구역_경계.json'
# JSON 파일 로드

try:
    geo_data = json.load(open(geo_path, encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))

# 폴리엄을 통해 지도 생성
g_map = folium.Map(location=[37.5502,126.982],zoom_start=9)

# 출력할 연도는 2017로 선택
year = '2017'

'''
geo_data: 지도 데이터 혹은 파일의 경로
data: 시각화하기 위한 데이터파일(여기서는 데이터프레임)
columns: 지도데이터와 매핑할 값. 시각화 할 변수를 지정.
fill_color: 시각화에 사용할 색상
fill_opacity,line_opacity: 투명도
key_on: 데이터 파일과 매핑할 값
legend_name: 범례
'''
folium.Choropleth(geo_data=geo_data,
                  data=df[year],
                  columns=[df.index, df[year]],
                  fill_color='PuBuGn', fill_opacity=0.7, line_opacity=1,
                  key_on='feature.properties.name',
                  legend_name='경기도_인구_데이터',
                  ).add_to(g_map)
# 선택한 연도를 파일명에 적용하여 HTML로 저장
g_map.save('../saveFiles.gyonggi_population_'+year+'.html')