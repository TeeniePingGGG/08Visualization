import cx_Oracle as cx
import folium

# Oracle DB 접속 정보
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

# 사용자 입력
input_sigun = input('시군명을 입력하세요: ')

# Folium 지도 초기화
del_map = folium.Map(location=[37.40, 127.38], zoom_start=10)

# SQL 실행
sql = """
SELECT * FROM delivery_apps
WHERE sigun = :sigun AND lat IS NOT NULL AND logt IS NOT NULL
ORDER BY idx ASC
"""

cursor.execute(sql, sigun=input_sigun)

count = 0
for rs in cursor:
    idx = rs[0]
    sigun = rs[1]
    store_nm = rs[2]
    bizregno = rs[3]
    indutype = rs[4]
    logt = rs[5]
    lotnoaddr = rs[6]
    zipno = rs[7]
    lat = rs[8]
    roadnmaddr = rs[9]

    folium.Marker(location=[lat, logt],popup=f"{store_nm} ({indutype})").add_to(del_map)
    count += 1

if count > 0:
    del_map.save(f"../saveFiles/{input_sigun}.html")
else:
    print(f"{input_sigun}에 해당하는 데이터가 없습니다.")

# DB 연결 종료
conn.close()
