'''
오라클 연결을 위한 모듈 임포트
설치: conda install cx_oracle
'''
import cx_Oracle as cx

# 오라클 접속을 위한 정보를 변수로 정의
host_name = 'localhost'
oracle_port = 1521
service_name='xe'

# 연결정보를 객체로 정의
connect_info = cx.makedsn(host_name, oracle_port, service_name)

# 커넥션 객체 생성
conn = cx.connect('education','1234',connect_info)
# 쿼리문 실행을 위한 커서 생성
cursor = conn.cursor()

# 테스트 데이터는 하드코딩으로 준비
SIGUN_NM = "나의시군"
FACLT_NM = "코스모대학교"
REFINE_LOTNO_ADDR = "서울시 금천구 가산동 월드메르디앙"
REFINE_WGS84_LAT = 37.1234
REFINE_WGS84_LOGT = 126.1234

# 인파라미터가 있는 insert 쿼리문. ':변수명' 과 같이 기술한다.
sql = """insert into g_univ(idx,sigun,faclt,addr,latitude,longitude)
    values(seq_board_num.nextval, :sigun, :faclt, :addr,:latitude,:longitude) """

try:
    # 쿼리문 실행시 인파라미터에 값을 설정한다.
    cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM, addr=REFINE_LOTNO_ADDR,
                   latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
    # 실행에 문제가 없다면 커밋해서 실제 테이블에 적용
    conn.commit()
    print("1개의 레코드 입력")
except Exception as e:
    # 예외가 발생했다면 롤백 처리
    conn.rollback()
    print('insert 실행시 오류 발생',e)
# db 연결 해제
conn.close()
