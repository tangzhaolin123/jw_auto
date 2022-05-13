#coding:utf-8
from time import sleep
import traceback
import uiautomator2 as u1
import random
import configparser
from jw_case import JiWei
from datetime import datetime
from datetime import timedelta
import re
import os
import json
import requests
import xlrd

# u = u1.connect('3f3582df')
# u = u1.connect('VS7P9L4PB6LFMRVW')
u = u1.connect('0.0.0.0')
#debug
URL = "https://oapi.dingtalk.com/robot/send?access_token=c553bbae288a266b5d2d4a382a41b54f332cdab43c1e6a94cff949766c5e05f6"  # Webhook地址
#测试
# URL = "https://oapi.dingtalk.com/robot/send?access_token=0a200657eeefb39d0180cf7a292f26ed4e7038de9387b0573b5bbd35a5e58050"  # Webhook地址

def message(content):
	try:
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
	except:
		pass

def dingtalk_robot(total,pass_total,fial_total,report_url):
    headers = {'Content-Type':'application/json'}

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

    response = requests.post(URL, data = json_data,headers = headers,timeout=3)


# access_key = 'gMQ_x2DD6xcBsHf7Bwn4iRGFLwLilsmiW5DG3RsI'
# secret_key = 'CAvmXjwUEZm8d8h_gStjOLKqy9ssx6mSHtlcFsdf'


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

    ret, info = put_file(token, key, local_img)
    img_url = urljoin(space2url[space_name], img_name)
    return img_url
# res = up2qiniu(r'c.png', "jwtime1","c.png")

class Template_mixin(object):
    """html报告"""
    HTML_TMPL = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>自动化测试报告</title>
            <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
            <h1 style="font-family: Microsoft YaHei">自动化测试报告</h1>
            <p class='attribute'><strong>测试人员 : </strong> 钉钉机器人</p>
            <p class='attribute'><strong>开始时间 : </strong> %(startTime)s</p>
            <p class='attribute'><strong>合计耗时 : </strong> %(totalTime)s</p>
            <p class='attribute'><strong>测试结果 : </strong> %(value)s</p>
            <style type="text/css" media="screen">
        body  { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px;}
        </style>
        </head>
        <body>
            <table id='result_table' class="table table-condensed table-bordered table-hover">
                <colgroup>
                    <col align='left' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th>用例编号</th>
                    <th>模块</th>
                    <th>用例名称</th>
                    <th>前置条件</th>
                    <th>测试步骤</th>
                    <th>预期结果</th>
                    <th>用例执行结果</th>
                    <th>失败原因</th>
                    <th>备注</th>
                </tr>
                %(table_tr)s
            </table>
            %(caseList)s
            %(robotlog)s
        </body>
        </html>"""

    TABLE_TMPL = """
        <tr class='failClass warning'>
            <td>%(step)s</td>
            <td>%(case_module)s</td>
            <td>%(case_name)s</td>
            <td>%(case_antecedents)s</td>
            <td>%(case_testProcedure)s</td>
            <td>%(case_expectedResult)s</td>
            <td>%(runresult)s</td>
            <td>%(reason)s</td>
            <td>%(case_notes)s</td>
        </tr>"""

def app_excel_field(case_code):
    # app_xlsfile = os.getcwd() + '\\app_auto_case.xlsx'  # 打开指定路径中的xls文件
	app_xlsfile = 'app_auto_case.xlsx'
	app_book = xlrd.open_workbook(app_xlsfile)
	app_sheet0 = app_book.sheet_by_index(1)
	app_row_n = app_sheet0.nrows - 1
	for row_i in range(0,app_row_n):
		if case_code == app_sheet0.col_values(0, start_rowx=0, end_rowx=None)[row_i]:
			return app_sheet0.row_values(row_i, start_colx=0, end_colx=7)

if __name__ == '__main__':
	# u.implicitly_wait(15)
	video_camera_name = '18726303'
	# video_camera_name = input("input:")
	# u.app_install('http://tangjw.xyz/1234.apk')
	u.press("back")
	sleep(1)
	u.press("back")
	sleep(1)
	u.press("home")
	sleep(3)
	u.app_start('com.termux')
	sleep(1)
	u.press("home")
	sleep(3)

	#监控弹框
	u.watcher.when("同意").click()
	u.watcher.when("允许").click()
	u.watcher.when("仅在前台使用应用时允许").click()
	u.watcher.when("双指可放大画面").click()
	u.watcher.when("可以尝试上下左右拖动画面").click()
	u.watcher.when("深入了解").click()
	u.watcher.when("我知道了").click()
	u.watcher.when("消息通知说明").press("back")
	# u.watcher.start()


	i = 0
	while i<1000:
		i=i+1
		print(('Testing time: %d') % (i))
		#list1 = [1]
		# cfgfile = os.getcwd() + '\\dbconf.ini'
		# config = configparser.ConfigParser()
		# config.read(cfgfile, encoding="utf-8-sig")
		# print(listx
		# Caselist = [1,2,4,5,6,7,8,9,10,11,12,13,3]
		Caselist = [1,2,3,4,5,6,7,8,9,10]
		# Caselist = [9,10]
		case_len = len(Caselist)
		count_success = 0
		fail_caselog = []
		robot_loglist = []
		case_number = []
		start_time = datetime.now()
		u.watcher.stop()
		for l0 in range(1, len(Caselist) + 1):
			a0 = Caselist[l0 - 1]
			#print(a, len(list1))
			w_report = ''
			robot_log_w = ''
			try:
				if a0 < 10:
					u0 = "JiWei.jwt_0" + str(a0)
					print(u0)
					eval(u0)(u,video_camera_name)
				else:
					u0 = "JiWei.jwt_" + str(a0)
					print(u0)
					eval(u0)(u,video_camera_name)
				# u.app_start('com.termux')
				# u.press("home")
				count_success = count_success + 1
			except Exception as err:
				# print ('出错',err)
				# a1 = traceback.format_exc()
				# print(a1)
				# message(a1)
				# dt1 = datetime.now()
				# dt2 = dt1.strftime('%Y-%m-%d %H.%M.%S')
				#截图
				try:
					dt1 = datetime.now()
					dt2 = dt1.strftime('%Y-%m-%d_%H.%M.%S')
					image = dt2 + ".png"
					u.screenshot(image)
					res = up2qiniu(image, "jwtime1", image)
					os.remove(image)
				except:
					res = "获取链接失败"

				#本次不算，重新开始
				# if l0 == 1:
				# 	i=i - 1
				# 	break

				# image = os.getcwd() + "\\" + dt2 + ".png"
				# d.screenshot(image)

				a1 = traceback.format_exc()
				print(a1)
				# if a1.find("AssertionError") >= 0:
				# 	pos1 = a1.find('AssertionError')
				# # print (pos1)
				# 	pos3 = a1[pos1 + 15:(pos1 + 40)]
				# else:
				pos1 = a1.find('in jwt')
				pos2 = a1.find('\n',pos1+10)
				pos_1 = a1[pos1-23:pos2]
				pos3 = re.sub('\n', "", pos_1)
				#pos2 = re.sub('\n', "", pos_1)
				#pos3 = re.sub("assert", "", pos2).strip()
				# if pos3.find("AssertionError") >= 0:
				# 	pos5 = re.sub("AssertionError",
				# 				  '执行编号Veri_' + str(j + 1) + '的用例' + app_element_url[j][0] + '进入页面失败:' +
				# 				  app_element_name['Veri_' + str(j + 1)] + '名字它在进入的页面不存在', pos3)
				# elif pos3.find("uiautomator2.exceptions.XPathElementNotFoundError") >= 0:
				# 	pos5 ='编号Veri_'+str(j+1)+app_element_url[j][0] + ',操作元素不存在'
				# else:
				# 	pos5 = '执行编号Veri_' + str(j + 1) + '的用例' + app_element_url[j][0] + ',操作元素不存在'
				# w = 'APP自动化测试' + '\n' + pos5
				w = pos3 + '\n' + res
				# w_report += u0 + pos3 + '\n' + '<br />' + '<a href=' + res + '>查看报错图片</a>' + '<br />'  # '<a href='+res+'>图片</a>'
				w_report += '<a href=' + res + '>查看报错图片</a>' + '<br />'  # '<a href='+res+'>图片</a>'
				robot_log_w += dt2 + u0 + pos3 + '\n'
				try:
					interval_time2 = datetime.now()
					if interval_time2 - start_time > timedelta(seconds=6*int(l0)):
						message(w)
				except:
					pass
				# if u(text="推送消息提醒").exists:
				# 	u(resourceId='com.yoosee:id/tx_deep_understand').click(timeout=5)
				# 	u(resourceId='com.yoosee:id/iv_back').click(timeout=5)
				# 	sleep(3)
				# u.press("back")
				# sleep(1)
				# u.press("back")
				# sleep(1)
				# u.press("home")
				# sleep(2)
				# u.app_stop('com.yoosee')
				# sleep(2)

				for retry_n in range(1,3):
				#重试一次
					try:
						eval(u0)(u,video_camera_name)
						message(u0+"重新执行"+str(retry_n)+"次OK")
						count_success = count_success + 1
						break
					except Exception as err:
						a1 = traceback.format_exc()
						print(a1)
						#截图
						try:
							dt1 = datetime.now()
							dt2 = dt1.strftime('%Y-%m-%d_%H.%M.%S')
							image = dt2 + ".png"
							u.screenshot(image)
							res = up2qiniu(image, "jwtime1", image)
							os.remove(image)
						except:
							res = "获取链接失败"
						# if a1.find("AssertionError") >= 0:
						# 	pos1 = a1.find('AssertionError')
						# 	# print (pos1)
						# 	pos3 = a1[pos1 + 15:(pos1 + 40)]
						# else:
						pos1 = a1.find('in jwt')
						pos2 = a1.find('\n', pos1 + 10)
						pos_1 = a1[pos1 - 23:pos2]
						pos3 = re.sub('\n', "", pos_1)
						w = u0+"重新执行"+str(retry_n)+"次仍报错"+pos3+'\n'+ res
						# w_report += u0+"重新执行"+str(retry_n)+"次仍报错"+pos3+'\n' +'<br />'+ '<a href='+res+'>查看报错图片</a>' +'<br />' #'<a href='+res+'>图片</a>'
						w_report += '<a href='+res+'>查看重新测试第'+str(retry_n)+'次报错图片</a>' +'<br />' #'<a href='+res+'>图片</a>'
						robot_log_w += dt2+u0+"重新执行"+str(retry_n)+"次仍报错"+pos3+'\n'
						# fail_caselog.append(w_report)
						# case_number.append(u0)
						try:
							message(w)
						except:
							pass

					if retry_n == 2:
						fail_caselog.append(w_report)
						case_number.append(u0)
						robot_loglist.append(robot_log_w)
					# if a0 > 7:
					# 	break
					# u.press("back")
					# sleep(1)
					# u.press("back")
					# sleep(1)
					# u.press("home")
					# sleep(2)
					# u.app_stop('com.yoosee')
					# sleep(2)
				if u.uiautomator.running() != True:
					u.uiautomator.start()
		# if l0 != 1:
		# try:
		count_case_fail = case_len - count_success
		#报告详情
		report_time = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
		report_file = report_time + ".html"
		total_time = datetime.now() - start_time

		#机器人日志
		dt3 = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
		robot_log_file = dt3 + ".txt"

		robot_log = open(robot_log_file, 'a')
		for robot_i in range(0, len(robot_loglist)):
			robot_log.write('\n' + robot_loglist[robot_i] + '\n')
		# robot_log.flush()
		robot_log.close()
		robot_log_singleurl =up2qiniu(robot_log_file, "jwtime1", robot_log_file)
		os.remove(robot_log_file)
		robot_log_url = '<a href='+robot_log_singleurl+'>查看机器人日志</a>'
		# print (robot_log_singleurl)

		# f = open(report_file, 'a')
		# f.write('自动化测试')
		# f.write('\n' + '测试人员：钉钉机器人' + '\n')
		# f.write('\n' + '开始时间：' + str(start_time) + '\n')
		# f.write('\n' + '合计耗时：' + str(total_time) + '\n')
		# f.write(
		# 	'\n' + '测试结果: ' + '共 ' + str(case_len) + '，' + '通过 ' + str(count_success) + '，' + '失败 ' + str(count_case_fail) + '，' + '通过率=' + str(float(count_success/case_len)*100) + '%' + '\n')
		# f.write(
		# 	'\n' + '************************************************************失败**********************************************')
		# # report_message = "功能数:"+str(case_len)+'个，'+"成功:"+str(count_success)+'条，'+'失败'+str(count_case_fail)+'条。'
		# for i in range(0, len(fail_caselog)):
		# 	f.write('\n' + fail_caselog[i] + '\n')
		# # f.flush()
		# f.close()
		#html报告
		table_tr0 = ''
		html = Template_mixin()
		for n in range(0,len(fail_caselog)):
			case_information = app_excel_field(case_number[n].replace('JiWei.', ''))
			table_td = html.TABLE_TMPL % dict(
				step= case_information[0],
				case_module=case_information[1],
				case_name=case_information[2],
				case_antecedents=case_information[3],
				case_testProcedure=case_information[4],
				case_expectedResult=case_information[5],
				runresult='<font color="red">Fail</font>',
				reason=fail_caselog[n],
				case_notes=case_information[6],

			)
			table_tr0 += table_td
		case_url = '<a href=https://docs.qq.com/sheet/DTlZ5aEJEcUJwSVl6>查看测试用例</a>'
		total_str = '共 %s，通过 %s，失败 %s，通过率 %s' % (
		count_case_fail + count_success, count_success, count_case_fail, str(round(count_success / (count_case_fail + count_success),2) * 100) + '%')
		# start_time = '2022-04-30_15:15'
		# total_time = '00:01:05'
		output = html.HTML_TMPL % dict(
			value=total_str,
			table_tr=table_tr0,
			startTime=start_time,
			totalTime=total_time,
			caseList=case_url,
			robotlog= robot_log_url
		)

		# 生成html报告

		with open(report_file, 'wb') as f:
			f.write(output.encode('utf-8'))

		report_url = '('+up2qiniu(report_file, "jwtime1", report_file)+')'
		os.remove(report_file)

		dingtalk_robot(str(case_len),str(count_success),str(count_case_fail),report_url)
		# u.press("recent")
				# sleep(2)
				# u(description="清除全部-按钮").click(timeout=5)
				# sleep(2)
		# except:
		# 	w = '生成报告失败'
		# 	message(w)
