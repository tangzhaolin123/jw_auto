#coding:utf-8
from time import sleep
import os


def doTask(case):
    e = os.system("python "+case)
    print (e)
    if e == 1:
        doTask(case)


def main():
    case = 'jwell.py'
    while True:
        try:
            doTask(case)
        except Exception as e:
            print (e)
            sleep(20)
            continue

if __name__=='__main__':
	# device_id = 'c6b4b563'
	main()