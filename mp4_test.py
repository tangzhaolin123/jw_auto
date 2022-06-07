#coding:utf-8
from time import sleep
import os
import uiautomator2 as u1

d = u1.connect('0.0.0.0')
d.screenrecord('output.mp4')

sleep(20)
# or do something else

d.screenrecord.stop()