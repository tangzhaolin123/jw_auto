#coding:utf-8
from time import sleep
import os
import configparser
import multiprocessing
import threading
import json
import requests

def doTask(case):
    e = os.system("python "+case)
    print (e)
    if e == 1:
        doTask(case)

from urllib.parse import urljoin
space2url ={
    "jwtime1":"http://tangjw.xyz",
    "x":"123"
}
def up2qiniu(local_img,space_name,img_name):
    """
    本图图片的上传
    :param local_img: 本地图片路径
    :param space_name: 云服务器的空间名称
    :param img_name: 上传后的网络上保存的图片名称
    :return img_url: 远程图片的路径(绝对路径)
    """

    from qiniu import Auth, put_file, etag
    import qiniu.config

    access_key = 'YX6Pck4xl_IXjhy9Oay7SsTB_d_XXyCrGlnnvTX7'
    secret_key = 'DQNnoew9MuGzXV3s6BL5B5BD711IQHcEQwhtnMww'

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'jwtime1'

    # 上传后保存的文件名
    key = img_name

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    # 要上传文件的本地路径
    # localfile = r'D:\jw8'

    ret, info = put_file(token, key, local_img, version='v2')
    img_url = urljoin(space2url[space_name], img_name)
    return img_url

def main_2():
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
def find_queue(queue):
    file_list = os.listdir()
    print(file_list)
    # file_list =['1234.txt', '2022-202.zip', '2022-203.zip']
    for file_name in file_list:
        if queue.full():
            print("队列已满!")
            break
        if 'jw2022-' in file_name:
            queue.put(file_name)
            print(file_name)
            sleep(0.5)

def up_queue(queue):
    # 循环读取队列消息
    while True:
        # 队列为空，停止读取
        if queue.empty():
            print("---队列已空---")
            break

    # 读取消息并输出
    result = queue.get()
    #print(result)
    res = up2qiniu(result, "jwtime1", result)
    r = requests.get(url=res)
    if r.status_code == 200:
        os.remove(result)

def main_1():
    #while True:
    # 创建消息队列
    queue = multiprocessing.Queue(1)
    # 创建子进程
    p1 = multiprocessing.Process(target=find_queue, args=(queue,))
    p1.start()
    # 等待p1写数据进程执行结束后，再往下执行
    p1.join()
    p1 = multiprocessing.Process(target=up_queue, args=(queue,))
    p1.start()
    sleep(1)

def main():

    t1 = threading.Thread(target=main_1)
    t1.start()
    sleep(1)
    t2 = threading.Thread(target=main_2)
    t2.start()

if __name__=='__main__':
	# device_id = 'c6b4b563'
    #配置文件读取参数
    # cfgpath = "dbconf.ini"
    # config = configparser.ConfigParser()
    # config.read(cfgpath, encoding="gb2312")
    # # 控制随时输出报告
    # do_not_run = config.get('sec1', '是否继续执行自动化')
    main_1()
    # while True:
    #     # 保活
    #     sleep(10)