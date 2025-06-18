from konlpy.tag import Okt

test = ("동해물돠 백두산이 마르고 닳도록"
        "하느님이 보우하사 우리나라 만세 korea ^^"
        )
okt = Okt()

print(okt.morphs(test))

print(okt.nouns(test))

result1 = okt.phrases(test)
print(result1)

'''
pos: 형태소 단위로 쪼갠 후 각 품사들을 태깅해서 리스트 형태로 반환
영어단어는 Alpha
특수기호는 Puntuation
한글은 koreanParticle 등
'''
result2 = okt.pos(test)
print(result2)