import requests, json

'''
경기 데이터 드림(https://data.gg.go.kr)
에서 제공하는 "전문 및 대학교 현황" OpenAPI
'''
# API 요청 URL
url = 'https://openapi.gg.go.kr/Jnclluniv?Type=json&pSize=252&KEY=37036b829e80435b9bd513cb9d7cdfd3'
# 파라미터(pSzie: 출력데이터 갯수)
params = dict(
    Type='json',
    pSzie='10',
    KEY='37036b829e80435b9bd513cb9d7cdfd3')

# OpenAPI의 요청 URL과 파라미터를 이용해서 페이지 정보를 JSON으로 얻어온다
raw_data = requests.get(url=url, params=params)
# Raw(로우) 데이터를 JSON으로 변환
binary_data = raw_data.content
# 뱐환 완료 JSON 데이터 로드
json_data = json.loads(binary_data)
# print(json_data)

'''
JSON데이터를 분석한 후 Key를 찾았다면 아래와 같이 반복문을 통해
필요한 값을 파싱한다.
'''
for jd in json_data['Jnclluniv'][1]['row']:
    SIGUN_NM = jd['SIGUN_NM']
    FACLT_NM = jd['FACLT_NM']
    REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR']
    REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']
    REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT']
    print(FACLT_NM, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)