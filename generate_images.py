from PIL import Image, ImageDraw, ImageFont
import os
os.makedirs('images', exist_ok=True)
labels=['peta','letak','pakaian','tarian','rumah']
colors=['red','green','blue','orange','purple']
for lab,col in zip(labels,colors):
    img=Image.new('RGB',(400,200),col)
    d=ImageDraw.Draw(img)
    try:
        f=ImageFont.load_default()
        d.text((10,90),lab.capitalize(),font=f,fill='white')
    except Exception:
        d.text((10,90),lab.capitalize(),fill='white')
    path=f'images/{lab}.png'
    img.save(path)
    print('created',path)
