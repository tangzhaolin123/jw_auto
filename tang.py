#-*- coding:utf-8 -*-
from time import sleep
import os
import re

from PIL import Image
import math
import operator
from functools import reduce
# import operator
# import pytesseract
import tempfile
import random
from datetime import datetime

from datetime import timedelta
import uiautomator2
import traceback


# accessibility 定位取content-desc的属性值
#driver.find_element_by_accessibility_id(u"除").click()# 点击“除号”
# tempDir = tempfile.gettempdir()
# #print (tempDir)
# driver_name = '979fd62b'
class Tiktok:
    @classmethod
    def tok_01(cls, u,d_time):#swip
        #sleep(1)
        u.press("home")
        #sleep(1)
        u.press("home")
        #sleep(2)
        # screen = u.window_size()
        #print (screen,screen[0])
        # a = screen.values()
        # t1_kuai = 0
        #start1 = datetime.now()
        u.app_start('com.zhiliaoapp.musically')
        sleep(8)
        # try:
        #     assert u(text="我知道了").exists
        #     u.press("back")
        #     sleep(2)
        # except:
        #     pass
        #u.tap([(540, 960)], )
        #sleep(1)
        times = [15, 6, 10,20]
        rtimes = [1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6]
        rtimes2 = [1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]
        keywords =['gymfit','outfit','yogababe','fitness','clothes','gymgirl','girlsport','girloutdoors',"girlleggings",'girlyoga','yoga']
        # kw = u(resourceId="com.zhiliaoapp.musically:id/aqw").get_text()
        #print (type(kw),kw)
        #查
        # xz = [0,1]
        # if random.choice(xz) == 0:
        u(resourceId="com.zhiliaoapp.musically:id/b8b").click()
        sleep(random.choice(rtimes))
        # u.set_fastinput_ime(True)
        u(resourceId="com.zhiliaoapp.musically:id/bd3").click()
        u.send_keys(random.choice(keywords))
        sleep(random.choice(rtimes))
        u(resourceId="com.zhiliaoapp.musically:id/eel").click()
        sleep(random.choice(rtimes))
        u(resourceId="android:id/text1")[2].click()
        sleep(random.choice(rtimes))
        swc = [i for i in range(1,15)]
        for sw in range(0,random.choice(swc)+1):
            u.drag(450, 1580, 450, 350, 0.2)
            sleep(random.choice(rtimes2))
        u(resourceId="com.zhiliaoapp.musically:id/e_0")[0].click()
        sleep(random.choice(rtimes))

        while True:
            if datetime.now() > d_time:
                break
            # for to in range(0, random.choice(times)):
            if  u(resourceId="com.zhiliaoapp.musically:id/aqw").exists:
                try:
                    kw = u(resourceId="com.zhiliaoapp.musically:id/aqw").get_text()
                    for ky in range(0,len(keywords)):
                        if keywords[ky] in kw:
                            sleep(random.choice(times))
                            if random.choice(times) == 20 or random.choice(times) == 15 or random.choice(times) == 10:
                                # u(resourceId="com.zhiliaoapp.musically:id/asx").click()
                                # sleep(1)

                                image_a = Image.open("freak.png")
                                u.screenshot("freak1.png")
                                image1 = Image.open("freak1.png")
                                img1 = image1.crop((961, 980, 1014, 1006))
                                img1.save("1.png")
                                image_b = Image.open("1.png")

                                h1 = image_a.histogram()
                                h2 = image_b.histogram()
                                rms = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
                                print (rms)
                                if rms > 82:
                                    # u(resourceId="com.zhiliaoapp.musically:id/asx").click()
                                    x1 = random.uniform(0.888,0.953)
                                    y1 = random.uniform(0.508,0.520)
                                    u.click(x1,y1)
                                    sleep(random.choice(rtimes))
                                if u(resourceId="com.zhiliaoapp.musically:id/bex").exists:
                                    x2 = random.uniform(0.904,0.934)
                                    y2 = random.uniform(0.445,0.456)
                                    u.click(x2,y2)
                                    #u.tap([(random.choice(i for i in range(0.904, 0.934, 0.05)),random.choice(i for i in range(0.445, 0.456, 0.03)),)], )
                                #     u(resourceId="com.zhiliaoapp.musically:id/bex").click()
                                    sleep(random.choice(rtimes))
                                    pl = ['WOW','nice','fine','Cool','Well','thanks','what happened ?','i like it']
                                    u(resourceId="com.zhiliaoapp.musically:id/afy").click()
                                    sleep(random.choice(rtimes))
                                    try:
                                        x3 = random.uniform(0.174, 0.544)
                                        y3 = random.uniform(0.961, 0.968)
                                        u.click(x3, y3)
                                        u.send_keys(random.choice(pl))
                                        sleep(random.choice(rtimes))
                                        u(resourceId="com.zhiliaoapp.musically:id/agi").click()
                                        sleep(random.choice(rtimes))
                                        u(resourceId="com.zhiliaoapp.musically:id/v5").click()
                                        sleep(random.choice(rtimes))
                                    except:
                                        u(resourceId="com.zhiliaoapp.musically:id/v5").click()
                                        sleep(random.choice(rtimes))


                    dx1 = random.randint(300,400)
                    dy1 = random.randint(350,420)
                    dx2 = random.randint(300, 400)
                    dy2 = random.randint(1500, 1600)
                    u.drag(dx1, dy2, dx2, dy1, 0.2)
                    sleep(random.choice(rtimes2))
                    try:
                        kw1 = u(resourceId="com.zhiliaoapp.musically:id/aqw").get_text()
                        if kw1 == kw:
                            u.press("back")
                            sleep(1)
                            u.press("back")
                            sleep(1)
                            u.press("back")
                            sleep(1)
                            u.press("back")
                            sleep(1)
                            u.press("back")
                            sleep(1)
                            u.press("home")
                            sleep(1)
                    except:
                        pass
                except:
                    pass
            elif not u(resourceId="com.zhiliaoapp.musically:id/aqw", className='android.widget.TextView').exists:
                ex1 = random.randint(300, 400)
                ey1 = random.randint(350, 420)
                ex2 = random.randint(300, 400)
                ey2 = random.randint(1550, 1600)
                u.drag(ex1, ey2, ex2, ey1, 0.2)
                sleep(random.choice(rtimes2))
            # else:
            #     u.drag(450, 1580, 450, 350, 0.2)
            #     sleep(1)
            if u(resourceId="com.zhiliaoapp.musically:id/d7z").exists:
                u(resourceId="com.zhiliaoapp.musically:id/d7z").click()
            if not u(resourceId="com.zhiliaoapp.musically:id/asx").exists:
                break
        # u.swipe(screen[0] / 2, (screen[1] - 100), screen[0] / 2, screen[1] / 2)
        # sleep(2)
        # u.swipe(screen[0] / 2, (screen[1] - 100), screen[0] / 2, screen[1] / 3)
        # sleep(2)
        # u.swipe(screen[0] / 2, (screen[1] - 100), screen[0] / 2, screen[1] / 3)
        # sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(2)

        # while True:
        #     if datetime.now() > d_time:
        #         # print(datetime.now())
        #         break

    @classmethod
    def tok_02(cls, u, d_time):  # zhangfen
        # sleep(1)
        u.press("home")
        # sleep(1)
        u.press("home")
        # sleep(2)
        # screen = u.window_size()
        # print (screen,screen[0])
        # a = screen.values()
        # t1_kuai = 0
        # start1 = datetime.now()
        u.app_start('com.zhiliaoapp.musically')
        sleep(8)
        # times = [15, 6, 10, 20]
        rtimes = [1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
        rtimes2 = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]
        while True:
            if datetime.now() > d_time:
                break
            # if  u(resourceId="com.zhiliaoapp.musically:id/aqw").exists:
            u(resourceId="com.zhiliaoapp.musically:id/g14").click()
            sleep(random.choice(rtimes2))
            gzs = u(resourceId="com.zhiliaoapp.musically:id/bg4").get_text()
            print (type(gzs),gzs,len(gzs))
            sleep(random.choice(rtimes2))
            if len(gzs) >= 3:
                if u(resourceId="com.zhiliaoapp.musically:id/dr2").exists:
                    u(resourceId="com.zhiliaoapp.musically:id/dr2").click()
                    sleep(random.choice(rtimes2))
                    swc = [i for i in range(1, 3)]
                    for sw in range(0, random.choice(swc) + 1):
                        u.drag(450, 1580, 450, 350, 0.2)
                        sleep(random.choice(rtimes2))
                    u(resourceId="com.zhiliaoapp.musically:id/aju")[0].click()
                    sleep(random.choice(rtimes))
                    pl = ['WOW', 'nice', 'fine', 'Cool', 'Well', 'thanks', 'what happened ?', 'i like it']
                    u(resourceId="com.zhiliaoapp.musically:id/afy").click()
                    sleep(random.choice(rtimes))
                    try:
                        x3 = random.uniform(0.174, 0.544)
                        y3 = random.uniform(0.961, 0.968)
                        u.click(x3, y3)
                        u.send_keys(random.choice(pl))
                        sleep(random.choice(rtimes))
                        u(resourceId="com.zhiliaoapp.musically:id/agi").click()
                        sleep(random.choice(rtimes))
                        u(resourceId="com.zhiliaoapp.musically:id/v5").click()
                        sleep(random.choice(rtimes))
                        u.press("back")
                        sleep(random.choice(rtimes))
                        u.press("back")
                        sleep(random.choice(rtimes))
                        # u.press("back")
                        # sleep(random.choice(rtimes))
                    except:
                        u(resourceId="com.zhiliaoapp.musically:id/v5").click()
                        sleep(random.choice(rtimes))
                        u.press("back")
                        sleep(random.choice(rtimes))
                        u.press("back")
                        sleep(random.choice(rtimes))
                        # u.press("back")
                        # sleep(random.choice(rtimes))
                else:
                    u.press("back")
                    sleep(random.choice(rtimes))
            else:
                u.press("back")
                sleep(random.choice(rtimes))
            dx1 = random.randint(300, 400)
            dy1 = random.randint(350, 420)
            dx2 = random.randint(300, 400)
            dy2 = random.randint(1500, 1600)
            u.drag(dx1, dy1, dx2, dy2, 0.2)
            sleep(random.choice(rtimes2))

    @classmethod
    def tok_03(cls, u, d_time):  # tuixiao
        # sleep(1)
        u.press("home")
        # sleep(1)
        u.press("home")
        # sleep(2)
        # screen = u.window_size()
        # print (screen,screen[0])
        # a = screen.values()
        # t1_kuai = 0
        # start1 = datetime.now()
        u.app_start('com.zhiliaoapp.musically')
        sleep(8)
        # try:
        #     assert u(text="我知道了").exists
        #     u.press("back")
        #     sleep(2)
        # except:
        #     pass
        # u.tap([(540, 960)], )
        # sleep(1)
        times = [15, 6, 10, 20]
        rtimes = [1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
        rtimes2 = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]
        keywords = ['gymfit', 'outfit', 'yogababe', 'fitness', 'clothes', 'gymgirl', 'girlsport', 'girloutdoors','girlyoga', 'yoga']
        # kw = u(resourceId="com.zhiliaoapp.musically:id/aqw").get_text()
        # print (type(kw),kw)
        # 查
        # xz = [0,1]
        list2 = random.sample(list1, 1)
        list3 = [f for f in list1 if f not in list2]
        # if random.choice(xz) == 0:
        u(resourceId="com.zhiliaoapp.musically:id/b8b").click()
        sleep(random.choice(rtimes))
        # u.set_fastinput_ime(True)
        u(resourceId="com.zhiliaoapp.musically:id/bd3").click()
        u.send_keys(random.choice(keywords))
        sleep(random.choice(rtimes))
        u(resourceId="com.zhiliaoapp.musically:id/eel").click()
        sleep(random.choice(rtimes))

        u(text="Videos").click()
        sleep(random.choice(rtimes))
        u(resourceId="com.zhiliaoapp.musically:id/ccn").click()
        sleep(random.choice(rtimes))
        u(resourceId="com.zhiliaoapp.musically:id/baa")[2].click()
        sleep(random.choice(rtimes))
        u(resourceId="com.zhiliaoapp.musically:id/aja").click()
        sleep(random.choice(rtimes))

        #u(resourceId="android:id/text1")[2].click()
        # sleep(random.choice(rtimes))
        swc = [i for i in range(1, 5)]
        for sw in range(0, random.choice(swc) + 1):
            u.drag(450, 1580, 450, 350, 0.2)
            sleep(random.choice(rtimes2))
        u(resourceId="com.zhiliaoapp.musically:id/e_0")[0].click()
        sleep(random.choice(rtimes))

        while True:
            if datetime.now() > d_time:
                break
            # if  u(resourceId="com.zhiliaoapp.musically:id/aqw").exists:
            u(resourceId="com.zhiliaoapp.musically:id/g14").click()
            sleep(random.choice(rtimes2))
            gzs = u(resourceId="com.zhiliaoapp.musically:id/bg4").get_text()
            print(type(gzs), gzs, len(gzs))
            sleep(random.choice(rtimes2))
            if len(gzs) >= 4:
                if u(resourceId="com.zhiliaoapp.musically:id/dr2").exists:
                    u(resourceId="com.zhiliaoapp.musically:id/dr2").click()
                    sleep(random.choice(rtimes2))
            swc = [i for i in range(1, 5)]
            for sw in range(0, random.choice(swc) + 1):
                u.drag(450, 1580, 450, 350, 0.2)
                sleep(random.choice(rtimes2))
            try:
                u(resourceId="com.zhiliaoapp.musically:id/aju")[0].click()
            except:
                u(resourceId="com.zhiliaoapp.musically:id/fr2")[0].click()
            sleep(random.choice(rtimes))
            pl = ['we make gym leggings,Comfortable, sturdy, amazing for working out & lounging','Munvot yoga pant Very stretchy and comfortable making them great for any type of workout.','Munvot working legging .A good choice if you like to wear louder leggings to the gym.','Munvot yoga capri legging.Great fit and comfort ideal for walking and are lightweight perfect for spring/summer.','Munvot workout pants.So whether you want them for gym or for outside activity I can recommend this brand']
            u(resourceId="com.zhiliaoapp.musically:id/afy").click()
            sleep(random.choice(rtimes))
            try:
                x3 = random.uniform(0.174, 0.544)
                y3 = random.uniform(0.961, 0.968)
                u.click(x3, y3)
                u.send_keys(random.choice(pl))
                sleep(random.choice(rtimes))
                u(resourceId="com.zhiliaoapp.musically:id/agi").click()
                sleep(random.choice(rtimes))
                u(resourceId="com.zhiliaoapp.musically:id/v5").click()
                sleep(random.choice(rtimes))
                u.press("back")
                sleep(random.choice(rtimes))
                u.press("back")
                sleep(random.choice(rtimes))
                # u.press("back")
                # sleep(random.choice(rtimes))
            except:
                u(resourceId="com.zhiliaoapp.musically:id/v5").click()
                sleep(random.choice(rtimes))
                u.press("back")
                sleep(random.choice(rtimes))
                u.press("back")
                sleep(random.choice(rtimes))
                # u.press("back")
                # sleep(random.choice(rtimes))
            # else:
            #     u.press("back")
            #     sleep(random.choice(rtimes))
            dx1 = random.randint(300, 400)
            dy1 = random.randint(350, 420)
            dx2 = random.randint(300, 400)
            dy2 = random.randint(1500, 1600)
            u.drag(dx1, dy2, dx2, dy1, 0.2)
            sleep(random.choice(rtimes2))