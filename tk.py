#coding:utf-8
import uiautomator2 as u1
from time import sleep
#import traceback
from datetime import datetime
from datetime import timedelta
from tang import Tiktok
import re
import os
import random
import configparser
import traceback
# u = u1.connect('0.0.0.0')
# u = u1.connect('5806c062')
u = u1.connect('eff85ca1')


# def wechat_notification(p1, w):
# 	# string = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]",".",w)
# 	url = "https://sc.ftqq.com/SCU23017T9ed8e384ce9b90da84afc89d9f8099095aa7467ddd1bc.send?text=%s&desp=%s" % (p1, w)
# 	requests.get(url)

if __name__ == '__main__':
	# screen = u.window_size()
	# u.swipe(screen[0] / 2, (screen[1] - 350), screen[0] / 2, 350,800)
	# sleep(3)

	# u.implicitly_wait(20)
	# print (datetime.now())
	# u.press("home")
	# sleep(2)
	# u.press("menu")
	# sleep(2)
	# u(resourceId="com.android.systemui:id/clearAnimView").click()

	# u(resourceId="com.android.systemui:id/recent_apps").click()
	# u(resourceId="com.oppo.launcher:id/btn_clear").click()
	u.set_fastinput_ime(True)
	sleep(3)
	if u.uiautomator.running()!= True:
		u.uiautomator.start()
	i = 0
	# u.app_start('com.zhiliaoapp.musically')
	while i<100:
		i=i+1
		print(('Testing time: %d') % (i))
		list1 = [3]
		# cfgpath = "dbconf.ini"
		# config = configparser.ConfigParser()
		# config.read(cfgpath, encoding="gb2312")
		# listx = config.get('tang1', 'x1')
		# print(listx)
		# a = list1[0]
		# d_time1 = datetime.strptime(str(datetime.now().date()) + '00:21', '%Y-%m-%d%H:%M')
		# d_time2 = datetime.strptime(str(datetime.now().date()) + '21:00', '%Y-%m-%d%H:%M')
		# re = 0
		for l0 in range(0, len(list1)):
			a = list1[l0]
			day1 = datetime.now() + timedelta(seconds=1800)
			if u(text='确定').exists:
				u(text='确定').click()
			try:
				if a<10:
					u2 = "Tiktok.tok_0" + str(a)
					print(u2)
					eval(u2)(u,day1)
				else:
					u2 = "Tiktok.tok_"+str(a)
					print (u2)
					eval(u2)(u,day1)
			except Exception as e:
				error = str(e)
				str1 = traceback.format_exc()
				print ("出错",error,str1)
				# re = re+1
				u.press("menu")
				u(resourceId="com.android.systemui:id/clearAnimView").click()
				try:
					#sleep(2)
					u.press("back")
					#sleep(1)
					u.press("back")
					#sleep(1)
					u.press("back")
					#sleep(2)
					u.press("home")
					#sleep(2)
					u.press("home")
					sleep(1)
					u.press("menu")
					u(resourceId="com.android.systemui:id/clearAnimView").click()
					# u(resourceId="com.android.systemui:id/recent_apps").click()
					# u(resourceId="com.oppo.launcher:id/btn_clear").click()
					sleep(3)
					if u.uiautomator.running() != True:
						u.uiautomator.start()
				except:
					pass