from konlpy.tag import Okt
from collections import Counter

from numpy.ma.core import count
from wordcloud import WordCloud

filename = '../resData/애국가.txt'
# read모드로 오픈한 후 내용을 읽어 변수에 저장
f = open(filename,'r',encoding='utf-8')
news = f.read()
f.close()

okt = Okt()
# 명사만 추출
noun = okt.nouns(news)
new_noun = []

# 한 글자인 명사는 제거
for v in noun:
    # 문자열의 길이가 2이상인것만 골라 리스트에 추가
    if len(v) >= 2:
        new_noun.append(v)

# 각 문자열의 등장 횟수 확인
count = Counter(new_noun)
print("카운트:",count)

noun_list = count.most_common(100)
for v in noun_list:
    print(v)

# 워드클라우드 생성(기본 사각형 모양)
# 폰트, 배경색, 가로, 세로 크기 등의 옵션을 설정
wc = WordCloud(font_path='../resData/malgun.ttf',
               background_color='white',colormap='Accent_r',
               width=1000, height=1000, max_words=100, max_font_size=300)

# 텍스트 파일의 내용을 통째로 넘겨주기
wc.generate(news)
wc.to_file("../saveFiles/wordcloud1.png")

# 빈도 데이터 넘겨주기
wc.generate_from_frequencies(dict(noun_list))
wc.to_file("../saveFiles/wordcloud2.png")
