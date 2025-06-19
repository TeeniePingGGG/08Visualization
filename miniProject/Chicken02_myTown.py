import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import  font_manager, rc


df = pd.read_csv('../saveFiles/치킨집가공.csv')

def splad(addr):
    parts = addr.split()
    if len(parts) > 2:
        return parts[2]
    else:
        return '알수없음'

df['행정동'] = df['소재지전체주소'].apply(splad)

dongCount = df['행정동'].value_counts().reset_index()
dongCount.columns = ['행정동','가게수']

dongCount['label'] = dongCount['행정동'] + '\n(' + dongCount['가게수'].astype(str) + ')'

plt.style.use('ggplot')
font_name = (font_manager.FontProperties(fname='../resData/malgun.ttf').
             get_name())
rc('font',family = font_name)

squarify.plot(sizes=dongCount['가게수'], label=dongCount['label'], alpha=0.8)
plt.axis('off')
plt.title('행정동별 치킨집 개수')
plt.show()