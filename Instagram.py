import textwrap
from PIL import Image, ImageFont, ImageDraw 
from instabot import Bot
from MotivationalQuote import MotivationalQuote
class Post:
    __quote:str
    __author:str
    __bot = Bot()
    hashtags = "#motivation #inspiration #determination #goals #ambition #aspiration #drive #persistence #tenacity #resilience #dedication #grit #hustle #nevergiveup #keepgoing #keepfighting #mindset #positivemindset #growthmindset #selfimprovement #selfmotivation #nevergiveup"
    def __init__(self, response):
        self.__quote = response['q']
        self.__author = response['a']
    def create(self):
        my_image = Image.open("base.png")
        imgDraw = ImageDraw.Draw(my_image)
        #title_font = ImageFont.truetype('Feral-Regular.ttf', 60)
        text = textwrap.fill(text=self.__quote, width=25)
        box = ((230, 380, 840, 780))
        font_size = 100
        size = None
        while (size is None or size[0] > box[2] - box[0] or size[1] > box[3] - box[1]) and font_size > 0:
            font = ImageFont.truetype("MonospaceTypewriter.ttf", font_size)
            size = font.getsize_multiline(text=text)
            font_size -= 1
        imgDraw.multiline_text((box[0], box[1]), text, (255,255,255), font)
        author_font = ImageFont.truetype("MonospaceTypewriter.ttf", 25)
        imgDraw.text((800, 890), self.__author, (255, 255, 255), font = author_font)
        my_image = my_image.convert("RGB")
        my_image.save("out.jpeg")

    def upload(self):
        self.__bot.login(username = "minerva_motivation", password = "Alco2001")
        self.__bot.upload_photo("out.jpeg", caption = "Quote by: " + self.__author +"\n" + Post.hashtags)

import os 
import glob
try:
    cookie_del = glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])
except:
    print("Done")
finally:
    pst = Post(MotivationalQuote.getQuote()[0])
    pst.create()
    pst.upload()
# class Reel:
#     __quote: str
#     __author:str
