#coding:utf-8
from time import sleep
import os
import configparser


def doTask(case):
    e = os.system("python "+case)
    print (e)
    if e == 1:
        doTask(case)


def main(rounds):
    case = 'jwell.py'
    i = 0
    while i<int(rounds):
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
    cfgpath = "dbconf.ini"
    config = configparser.ConfigParser()
    config.read(cfgpath, encoding="gb2312")
    rounds = config.get('sec2', '用例执行轮次')
    main(rounds)