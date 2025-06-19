import pandas as pd
import requests, json

# API 요청 URL
url = 'https://openapi.gg.go.kr/GGEXPSDLV'

# 파라미터(pSzie: 출력데이터 갯수)
params = dict(
    Type='json',
    pSize='10',
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

    print(STR_NM,BIZREGNO,INDUTYPE_NM,REFINE_WGS84_LOGT,REFINE_LOTNO_ADDR,REFINE_ZIPNO,REFINE_WGS84_LAT,REFINE_ROADNM_ADDR)