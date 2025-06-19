import cx_Oracle as cx
import folium
import requests, json

host_name = 'localhost'
oracle_port = 1521
service_name='xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education','1234',connect_info)

cursor = conn.cursor()

# 폴리엄으로 지도 생성
univ_map = folium.Map(location=[37.40, 127.38], zoom_start=10)
univ_map.save('../saveFiles/univ_map.html')

# 지도 데이터를 오름차순 정렬해서 인출
sql = "select * from g_univ order by idx asc"

cursor.execute(sql)
for rs in cursor:
    idx = rs[0]
    sigun = rs[1]
    faclt = rs[2]
    addr = rs[3]
    latitude = rs[4]
    longitude = rs[5]

    # 대학 정보를 톨해 마커 생성
    folium.Marker([latitude,longitude],popup=faclt).add_to(univ_map)
    print(faclt,latitude,longitude)

# 마커가 포함된 지도 생성 및 저장
univ_map.save("../saveFiles/univ_map_marker.html")
print("맵이 생성되었습니다")

