from numpy.core.fromnumeric import size
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

size_overflow = []
data = pd.read_excel(r'names.xlsx')

name_list = data["Name"].tolist()
for i in name_list:
    im = Image.open(r'certificate.jpeg')
    if im.mode == 'RGBA':
        im = im.convert('RGB')
    d = ImageDraw.Draw(im)
    location = (215, 255)
    text_color = (0, 0, 0)
    font = ImageFont.truetype("arial.ttf", 75)
    contloc = (185, 338)
    fnt = ImageFont.truetype("josefinsans.ttf", 22)
    cnt = "for his/her participation in "
    if len(i) > 13 and len(i) < 20:
        font = ImageFont.truetype("arial.ttf", 50)
    elif len(i) > 20 and len(i) < 27:
        font = ImageFont.truetype("arial.ttf", 40)
        location = (120, 255)
    elif len(i) >= 30 and len(i) <= 40:
        font = ImageFont.truetype("arial.ttf", 30)
        location = (100, 255)
    else:
        size_overflow.append(i)

    d.text(location, i.capitalize(), fill=text_color, font=font)
    d.text(contloc, cnt, fill=text_color, font=fnt)
    im.save("certificate_" + i + ".png")


print("ERROR! seems like some certificates couldnt be printed ", size_overflow)
print("*****************************certificates printed and sent to the participants successfully!!!**************************************")
