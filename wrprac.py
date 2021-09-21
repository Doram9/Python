from wordcloud import WordCloud
from PIL import Image
import numpy as np


text = ''
with open("데분과 대화내용.txt","r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5: ]:
        if '] [' in  line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('사진', '').replace('삭제된 메시지입니다', '').replace('이모티콘', '').replace('ㅠ', '')



mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/WINDOWS/Fonts/malgun.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("sso.png")