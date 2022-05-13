import json
import requests
from time import sleep
#
# URL = "https://oapi.dingtalk.com/robot/send?access_token=c553bbae288a266b5d2d4a382a41b54f332cdab43c1e6a94cff949766c5e05f6"  # Webhook地址
URL = "https://oapi.dingtalk.com/robot/send?access_token=0a200657eeefb39d0180cf7a292f26ed4e7038de9387b0573b5bbd35a5e58050"  # Webhook地址

# #content
def message(content):
    data = {
    "msgtype":"text",
    "text":{
        "content":"测试："+content
    }
    }
    headers1 = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    data = json.dumps(data, ensure_ascii=False)
    data = data.encode(encoding="utf-8")
    r = requests.post(url=URL, data=data,headers=headers1,timeout=3)
    r = json.loads(r.text)
    return r

#markdown
import requests
import json



def dingtalk_robot(total,pass_total,fial_total,report_url):


    # url = "https://oapi.dingtalk.com/robot/send?access_token=c553bbae288a266b5d2d4a382a41b54f332cdab43c1e6a94cff949766c5e05f6"  # Webhook地址
    url = "https://oapi.dingtalk.com/robot/send?access_token=0a200657eeefb39d0180cf7a292f26ed4e7038de9387b0573b5bbd35a5e58050"  # Webhook地址


    headers = {'Content-Type':'application/json'}

    data_dict = {
        "msgtype":"markdown",

        "markdown":{
            "title":"测试报告",

            # "text":"#### 测试报告 \n\n"
            #        "> **Application_ID:** app-20201208100505-58622\n\n"
            #        "> **Name:** compute_04\n\n"
            #        "> **Duration:** 4.4 h"
            #        "##### <font color=#FF0000>橙色预警: 夜晚将有雷阵雨 </font>"
           "text":"#### **测试报告** \n\n"
                  "![report](http://tangjw.xyz/report.png)"
                  "> **用例总数:** **"+str(total)+"**\n\n"
                  "> **PASS:** **<font color=#7CFCOO>"+str(pass_total)+"</font>**\n\n"
                  "> **FAIL:** **<font color=#FF0000>"+str(fial_total)+"</font>**\n\n"
                  "[查看详情]"+report_url
    }
    }

    json_data =json.dumps(data_dict)

    response = requests.post(url, data = json_data,headers = headers)
    print (response.text)        # {"errcode":0,"errmsg":"ok"}



if __name__ == '__main__':

    # dingtalk_robot(13,12,1,'(http://tangjw.xyz/2022-05-11_06.10.34.html)')
    content = '出现了BUG'
    message(content)
# def app_start(u):
#     u.press("home")
#     sleep(1)
#     u.press("recent")
#     sleep(2)
#     u(description="清除全部-按钮").click()
#     sleep(2)
#     u.app_start('com.yoosee')
#     sleep(8)
#     u(text="设备").exists(timeout=10)
#     sleep(2)
# content = "你1好"
# message(content)
# if __name__ == "__main__":
#     print(message("注意了!百果秘书经营总览/fms/api/applyEvaluation/upload接口数据异常：无值"))
#     # {'errcode': 0, 'errmsg': 'ok'}
