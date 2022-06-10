#coding:utf-8
from time import sleep
import os
import configparser


def doTask(case):
    e = os.system("python "+case)
    print (e)
    if e == 1:
        doTask(case)


def main():
    case = 'jwell.py'
    i = 0
    while i<1:
        try:
            doTask(case)
        except Exception as e:
            print (e)
            sleep(20)
            continue
        i = i + 1

if __name__=='__main__':
	# device_id = 'c6b4b563'
    #配置文件读取参数
    # cfgpath = "dbconf.ini"
    # config = configparser.ConfigParser()
    # config.read(cfgpath, encoding="gb2312")
    # # 控制随时输出报告
    # do_not_run = config.get('sec1', '是否继续执行自动化')
    main()