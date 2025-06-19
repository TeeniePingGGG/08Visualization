import pandas as pd
import requests, json
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

# API 요청 URL
url = 'https://openapi.gg.go.kr/GGEXPSDLV'

for idx in range(1,36):
    # 파라미터(pSzie: 출력데이터 갯수)
    params = dict(
        Type='json',
        p_index =idx,
        pSize='1000',
        KEY='e0845dd5683646928d7b586b81c75d61')

    # OpenAPI의 요청 URL과 파라미터를 이용해서 페이지 정보를 JSON으로 얻어온다
    raw_data = requests.get(url=url, params=params)
    # Raw(로우) 데이터를 JSON으로 변환
    binary_data = raw_data.content
    # 뱐환 완료 JSON 데이터 로드
    json_data = json.loads(binary_data)

    df = pd.DataFrame(json_data)

    '''
    JSON데이터를 분석한 후 Key를 찾았다면 아래와 같이 반복문을 통해
    필요한 값을 파싱한다.
    '''
    for jd in json_data['GGEXPSDLV'][1]['row']:
        SIGUN_NM = jd['SIGUN_NM'] # 시군명
        STR_NM = jd['STR_NM'] # 매장명
        BIZREGNO = jd['BIZREGNO'] # 사업자등록번호
        INDUTYPE_NM = jd['INDUTYPE_NM'] # 업종
        REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT'] # 정제경도
        REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR'] # 정제지번주소
        REFINE_ZIPNO = jd['REFINE_ZIPNO'] # 정제 우편번호
        REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT'] #정제 위도
        REFINE_ROADNM_ADDR = jd['REFINE_ROADNM_ADDR'] #정제 도로명 주소

        # 인파라미터가 있는 insert 쿼리문. ':변수명' 과 같이 기술한다.
        sql = """insert into delivery_apps(idx,sigun,store_nm,bizregno,indutype,logt,lotnoaddr,zipno,lat,roadnmaddr)
            values(seq_board_num.nextval, :sigun, :store_nm, :bizregno,:indutype,:logt,:lotnoaddr, :zipno,:lat,:roadnmaddr) """

        try:
            # 쿼리문 실행시 인파라미터에 값을 설정한다.
            cursor.execute(sql, sigun=SIGUN_NM, store_nm=STR_NM, bizregno=BIZREGNO, indutype=INDUTYPE_NM,
                           logt=REFINE_WGS84_LOGT, lotnoaddr=REFINE_LOTNO_ADDR, zipno=REFINE_ZIPNO, lat=REFINE_WGS84_LAT,
                           roadnmaddr=REFINE_ROADNM_ADDR)
            # 실행에 문제가 없다면 커밋해서 실제 테이블에 적용
            conn.commit()
            print("1개의 레코드 입력")
        except Exception as e:
            # 예외가 발생했다면 롤백 처리
            conn.rollback()
            print('insert 실행시 오류 발생', e)
    # db 연결 해제
conn.close()

    # print(STR_NM,BIZREGNO,INDUTYPE_NM,REFINE_WGS84_LOGT,REFINE_LOTNO_ADDR,REFINE_ZIPNO,REFINE_WGS84_LAT,REFINE_ROADNM_ADDR)