'''
아나콘다 설치시 기본적으로 생성되는 base 가상환경에는 설치되어 있지
않으므로 다음과 같이 설치한다.
pip install folium
혹은 conda로 설치할 수 있다.
'''
import folium
'''
folium 라이브러리
    : 데이터를 지도로 시각화 해주는 라이브러리
    코드를 실행하면 IDE에서 직접 지도가 표시되지 않고, HTML파일로
    저장되어 웹브라우저를 통해 확인해야한다. 웹서버(Tomcat)가
    있다면 특정 경로에 저장하여 Spring(혹은 JSP)와 연동할 수 있다.
'''

# 맴표시: 인수로 시설물의 위도/경도와 줌 레벨을 지정
seoul_map1 = folium.Map(location=[37.55,126.98], zoom_start=12)
seoul_map1.save('../saveFiles/seoul1.html')

# tiles 옵션으로 산악지형 강조, 도로명 강조와 같은 표현이 가능하다.
# (버전의 문제가 있어 확인 필요)

# 데이터프레임 변환을 위해 판다스 임포트
import pandas as pd
# 엑셀 파일을 변환. 1행은 타이틀로 간주해서 2행부터 데이터로 가져온다.
df = pd.read_excel('../resData/서울지역_대학교_위치.xlsx', engine='openpyxl')

# 컬럼영 추가
df.columns=['학교명','위도','경도']

# 데이터프레임에 저장된 갯수만큼 반복하여 지도에 마커 추가
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    # 위경도는 리스트로 부여하고, popup(풍선도움말)은 학교명 지정
    folium.Marker([lat,lng],popup=name).add_to(seoul_map1)
# 마커가 추가된 Map을 HTML파일로 저장
seoul_map1.save('../saveFiles/seoul_colleages1.html')

# 원형마커 및 추가옵션 지정
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat,lng],radius=10, color='brown', fill=True,
                  fill_color='coral',fill_opacity=0.7,
                  popup=name).add_to(seoul_map1)
seoul_map1.save('../saveFiles/seoul_colleages2.html')