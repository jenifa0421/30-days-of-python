from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import os
df=pd.read_csv('venv/Lib/Book1.csv')
font=ImageFont.truetype('arial.ttf',25)
for index,j in df.iterrows():
    img=Image.open('venv/Lib/certificate.jpg')
    draw=ImageDraw.Draw(img)
    draw.text(xy=(80,310),text='{}'.format(j['Name']),fill=(255,0,0),font=font)
    draw.text(xy=(80, 370), text='{}'.format(j['Project Name']), fill=(255, 0, 0), font=font)
    draw.text(xy=(900, 510), text='{}'.format(j['Certificate Number']), fill=(255, 0, 0), font=font)
    img.save('venv/Lib/certificates/{}.jpg'.format(j['Name']))
