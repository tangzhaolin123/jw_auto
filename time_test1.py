# from datetime import datetime
# from datetime import timedelta
# from time import sleep
# # d_time = datetime.now() + timedelta(seconds=3600)
# d_time1 = datetime.now()
# sleep(10)
# d_time2 = datetime.now()
# a = d_time2 - d_time1
# print (a<timedelta(seconds=5))
# a = 31
# total = 50
# rate = float(a/total)*100
# print (rate)
import json
import requests
URL = "https://oapi.dingtalk.com/robot/send?access_token=c553bbae288a266b5d2d4a382a41b54f332cdab43c1e6a94cff949766c5e05f6"  # Webhook地址
class DingMessage:
    def __init__(self):
        # self.URL = "https://oapi.dingtalk.com/robot/send?access_token=c553bbae288a266b5d2d4a382a41b54f332cdab43c1e6a94cff949766c5e05f6"  # Webhook地址
        self.URL = URL
        self.headers = {'Content-Type':'application/json'}


    def dingtalk_testexception(self,case_code,premise_conditions,case_name,case_steps,expected_result,operation_log,result_url):
        if "ok" in case_code:
            data_dict = {
                "msgtype":"markdown",

                "markdown":{
                    "title":"测试异常提示",
                   "text":"#### **<font color=#7CFCOO>"+case_code+"测试异常**</font>\n\n"
                          "> **用例名称:** <font color=#000000>"+case_name+"</font>\n\n"                        
                          "> **前置条件:** <font color=#000000>"+premise_conditions+"</font>\n\n"                        
                          "> **操作步骤:** <font color=#000000>"+case_steps+"</font>\n\n"
                          "> **预期结果:** <font color=#000000>"+expected_result+"</font>\n\n"
                }
            }
        else:
            data_dict = {
                "msgtype": "markdown",

                "markdown": {
                    "title": "测试异常提示",
                    "text": "#### **<font color=#FF0000>" + case_code + "测试异常**</font>\n\n"
                                                                        "> **用例名称:** <font color=#000000>" + case_name + "</font>\n\n"
                                                                                                                         "> **前置条件:** <font color=#000000>" + premise_conditions + "</font>\n\n"
                                                                                                                                                                                   "> **操作步骤:** <font color=#000000>" + case_steps + "</font>\n\n"
                                                                                                                                                                                                                                     "> **预期结果:** <font color=#000000>" + expected_result + "</font>\n\n"
                                                                                                                                                                                                                                                                                            "[查看报错时截图](" + result_url + ')'
                }
            }

        json_data =json.dumps(data_dict)

        response = requests.post(self.URL, data = json_data,headers = self.headers,timeout=3)

    def dingtalk_robot(self,total,pass_total,fial_total,report_url):
        data_dict = {
            "msgtype":"markdown",

            "markdown":{
                "title":"测试报告",
               "text":"#### 测试报告 \n\n"
                      "![report](http://tangjw.xyz/report.png)"
                      "> **用例总数:** **"+str(total)+"**\n\n"
                      "> **PASS:** **<font color=#7CFCOO>"+str(pass_total)+"</font>**\n\n"
                      "> **FAIL:** **<font color=#FF0000>"+str(fial_total)+"</font>**\n\n"
                      "[查看详情]"+report_url
            }
        }

        json_data =json.dumps(data_dict)

        response = requests.post(self.URL, data = json_data,headers = self.headers,timeout=3)
# app_version = '00.46.00.90'
# case_code = 'jwt_01'
# premise_conditions = 'APP首次安装或覆盖安装'
# case_name = '暂不使用用户服务协议'
# case_steps = '手机桌面进入有看头APP，弹出用户服务协议，点击暂不使用'
# expected_result = '退出APP'
# operation_log = "line 439, in jwt_20    assert u(text,resourceId='com.yoosee:id/tv_title').wait(timeout=5)没有前往帮助中心_添加绑定H5"
# result_url = 'http://tangjw.xyz/2022-05-17_19.51.46.png'
# DingMessage().dingtalk_testexception(case_code,premise_conditions,case_name,case_steps,expected_result,operation_log,result_url)

# "> **自动化操作日志:** <font color=#000000>"+operation_log+"</font>\n\n"
# "> **报错时截图:** " + result_url


# URL = "https://oapi.dingtalk.com/robot/send?access_token=c553bbae288a266b5d2d4a382a41b54f332cdab43c1e6a94cff949766c5e05f6"  # Webhook地址
# def dingtalk_robot(premise_conditions,case_name,case_steps,expected_result,operation_log,result_url):
#     headers = {'Content-Type':'application/json'}
#
#     data_dict = {
#         "msgtype":"markdown",
#
#         "markdown":{
#             "title":"测试异常提示",
#            "text":"#### **<font color=#FF0000>测试异常**</font>\n\n"
#                   "> **用例名称:** <font color=#000000>"+case_name+"</font>\n\n"
#                   "> **前置条件:** <font color=#000000>"+premise_conditions+"</font>\n\n"
#                   "> **操作步骤:** <font color=#000000>"+case_steps+"</font>\n\n"
#                   "> **预期结果:** <font color=#000000>"+expected_result+"</font>\n\n"
#                   "> **报错时截图:** "+ result_url
#         }
#     }
#
#     json_data =json.dumps(data_dict)
#
#     response = requests.post(URL, data = json_data,headers = headers,timeout=3)
# premise_conditions = 'APP首次安装或覆盖安装'
# case_name = '暂不使用用户服务协议'
# case_steps = '手机桌面进入有看头APP，弹出用户服务协议，点击暂不使用'
# expected_result = '退出APP'
# operation_log = "line 439, in jwt_20    assert u(text,resourceId='com.yoosee:id/tv_title').wait(timeout=5)没有前往帮助中心_添加绑定H5"
# result_url = 'http://tangjw.xyz/2022-05-17_19.51.46.png'
# dingtalk_robot(premise_conditions,case_name,case_steps,expected_result,operation_log,result_url)
#获取app id
URL = "http://www.pgyer.com/apiv1/app/getAppKeyByShortcut"
def app_id():
    headers = {'Content-Type':'application/json'}

    data = {
        "shortcut": (None, "ptY3"),
        "_api_key": (None, "cbe11636fc4031641cccbcb648227d6c")
    }

    response = requests.request("POST", URL, files=data)
    jdata = json.loads(response.text)
    print(type(jdata),jdata)
    print (jdata['data']['appKey'])

# app_id()

# 20357c04ef7614ab96688dd5d136e408
# def install_url():
#     URL = 'http://www.pgyer.com/apiv1/app/install'
#     headers = {'Content-Type': 'application/json'}
#     data_dict = {
#         "aKey": "20357c04ef7614ab96688dd5d136e408",
#         "_api_key":'cbe11636fc4031641cccbcb648227d6c'
#     }
#
#     json_data = json.dumps(data_dict)
#
#     response = requests.get(URL, data=json_data, headers=headers, timeout=3)
#     print (response)
# install_url()
data_dict = {
        "aKey": "20357c04ef7614ab96688dd5d136e408",
        "_api_key":'cbe11636fc4031641cccbcb648227d6c'
    }
install_url = 'http://www.pgyer.com/apiv1/app/install?aKey=%s&_api_key=%s'%(data_dict['aKey'],data_dict['_api_key'])
print (install_url)


import requests

url = install_url
# r = requests.get(url)
# print (r)
# with open('1.apk',"wb") as code:
#     code.write(r.content)


r = requests.get(url, stream=True)
f = open("1.apk", "wb")
for chunk in r.iter_content(chunk_size=512):
    if chunk:
        f.write(chunk)
