#coding:utf-8
from time import sleep
import os


def doTask(case):
    e = os.system("python "+case)
    print (e)
    if e == 1:
        # send_move()
        # os.popen("adb shell input swipe 20 1000 1060 1000 100")
        # os.popen("password.exe")
        # sleep(2)
        # os.popen("adb -s "+ device_id +" shell input tap 790 1279")
        # sleep(2)
        # dt1 = datetime.now()
        # dt2 = dt1.strftime('%Y-%m-%d.%H.%M.%S')
        # os.popen("adb -s " + device_id + " shell dumpsys dropbox > d:\\3\\" + dt2 + ".txt")
        # sleep(2)
        doTask(case)


def main():
    case = 'tk.py'
    while True:
        try:
            # os.popen("adb shell input swipe 20 1000 1060 1000 100")
            doTask(case)
        except Exception as e:
            print (e)
            sleep(20)
            continue

if __name__=='__main__':
	# device_id = 'c6b4b563'
	main()