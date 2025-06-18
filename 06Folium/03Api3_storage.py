import cx_Oracle as cx
import requests, json

# 오라클 연결
host_name = 'localhost'
oracle_port = 1521
service_name='xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education','1234',connect_info)

# 커서 생성
cursor = conn.cursor()

# 경기데이터드림에서 제공하는 OpenAPI 사용
url = 'https://openapi.gg.go.kr/Jnclluniv?Type=json&pSize=252&KEY=37036b829e80435b9bd513cb9d7cdfd3'
# 파라미터 작성시 모든 데이터를 가져오기 위해 pSize는 252로 설정
params = dict(
    Type='json',
    pSize='252',
    KEY='37036b829e80435b9bd513cb9d7cdfd3')

# JSON데이터 읽어오기
raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)
# print(json_data)

# 제공된 데이터의 갯수만큼 반복
for jd in json_data['Jnclluniv'][1]['row']:
    SIGUN_NM = jd['SIGUN_NM']
    FACLT_NM = jd['FACLT_NM']
    REFINE_LOTNO_ADDR = '주소'
    REFINE_WGS84_LAT = '37.123'
    REFINE_WGS84_LOGT = '127.123'
    # print(FACLT_NM, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)

    # 인파라미터가 있는 insert 쿼리문 작성
    sql = """insert into g_univ(idx,sigun,faclt,addr,latitude,longitude)
        values(seq_board_num.nextval, :sigun, :faclt, :addr,:latitude,:longitude) """

    try:
        # 커서를 통해 쿼리문 실행.
        cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM, addr=REFINE_LOTNO_ADDR,
                       latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
        conn.commit()
        print("1개의 레코드 입력")
    except Exception as e:
        conn.rollback()
        print('insert 실행시 오류 발생',e)

conn.close()