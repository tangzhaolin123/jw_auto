#coding:utf-8
from time import sleep
import configparser


#配置文件读取参数
cfgpath = "dbconf.ini"
config = configparser.ConfigParser()
config.read(cfgpath, encoding="gb2312")
list1 = config.get('sec1', '摄像头设备ID')
list2 = config.get('sec1', '手机设备名')
list3 = config.get('sec1', '钉钉消息Webhook地址')
list4 = config.get('sec1', 'APP的id')
print (list1,list2,list3,list4)

config.set("sec1", "APP的id", '255454545')
config.write(open("dbconf.ini", "w"))
list4 = config.get('sec1', 'APP的id')
print (list4)