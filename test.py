import textwrap
from PIL import Image, ImageFont, ImageDraw 
my_image = Image.open("base.jpg")
imgDraw = ImageDraw.Draw(my_image)
title_font = ImageFont.truetype('Feral-Regular.ttf', 60)
quote = "Hola madre.  Esto es una quote"
text = textwrap.fill(text=quote, width=25)
box = ((200, 400, 880, 780))
font_size = 100
size = None
while (size is None or size[0] > box[2] - box[0] or size[1] > box[3] - box[1]) and font_size > 0:
	font = ImageFont.truetype("MonospaceTypewriter.ttf", font_size)
	size = font.getsize_multiline(text=text)
	font_size -= 1
imgDraw.multiline_text((box[0], box[1]), text, (255,255,255), font)
author_font = ImageFont.truetype("MonospaceTypewriter.ttf", 25)
imgDraw.text((800, 890), "Author", (255, 255, 255), font = author_font)
my_image.save("out.png")

# textWidth, textHeight = imgDraw.textsize(quote, font=title_font)
# xText = (width - textWidth) / 2
# yText = (height - textHeight) / 2
# imgDraw.text((xText, yText), quote, font=title_font, fill=(255, 255, 255))
# #image_editable.text((215,315), title_text, (255, 255, 255), font=title_font)
# my_image.save("result.jpg")