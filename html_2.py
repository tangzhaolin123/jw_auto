# -*- coding=utf-8 -*-
import  time,os

#数据部分
func_dict={"funcname":"模块1",}

funcname=['书架','书城','分类','我的']
case1={"name":"模块1","total":"10","passnum":"10","failnum":"0","radio":"80","status":"PASS"}
case2={"name":"模块2","total":"20","passnum":"15","failnum":"5","radio":"75","status":"Fail"}

VERSION_DICT={"version": '快看小说 3.8.8',"radio":'99',"runstarttime":time.strftime('%Y-%m-%d %H:%M:%S'),"runstoptime" : time.strftime('%Y-%m-%d %H:%M:%S')}


class Template_mixin(object):
    """html报告"""
    HTML_TMPL = r"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>自动化测试报告</title>
            <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
            <h2 style="font-family: Microsoft YaHei">自动化测试报告</h2>
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
                    <th>客户端及版本</th>
                    <th>通过率</th>
                    <th>开始时间</th>
                    <th>结束时间</th>
                </tr>
                %(table_tr)s
            <!-- 执行模块 -->
            <p class='attribute'><strong>测试详情 : </strong> 执行结果</p>
            <table id='result_table' class="table table-condensed table-bordered table-hover">
                <colgroup>
                   <col align='left' />
                   <col align='right' />
                   <col align='right' />
                   <col align='right' />
                   <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th colspan="2">业务模块</th>
                    <th>用例总数</th>
                    <th>通过数</th>
                    <th>状态</th>
                </tr>
                %(table_tr2)s
                %(table_tr3)s


            </table>
        </body>
        </html>"""
    #总数据
    TABLE_TMPL_TOTAL = """
        <tr class='failClass warning'>
            <td>%(version)s</td>
            <td>%(radio)s</td>
            <td>%(runstarttime)s</td>
            <td>%(runstoptime)s</td>
        </tr>"""
    #详情表头
    TABLE_TMPL_MODULE = """
        <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
            <th>%(name)s</th>
            <th>%(module)s</th>
            <th>%(casetotal)s</th>
            <th>%(passtotal)s</th>
            <th>%(status)s</th>
        </tr>"""
    #case数据
    TABLE_TMPL_CASE = """
        <tr class='failClass warning'>
            <td>%(name)s</td>
            <td>%(module)s</td>
            <td>%(casetotal)s</td>
            <td>%(passtotal)s</td>
            <td>%(status)s</td>
        </tr>"""



if __name__ == '__main__':
    table_tr0 = ''
    table_tr1=""
    table_tr2=""

    numfail = 1
    numsucc = 9
    html = Template_mixin()

    #总表数据
    table_td = html.TABLE_TMPL_TOTAL % dict(version=VERSION_DICT['version'],radio=VERSION_DICT['radio'],runstarttime=VERSION_DICT['runstarttime'],runstoptime = VERSION_DICT['runstoptime'])
    table_tr0 += table_td

    #详情数据
    table_td_module=html.TABLE_TMPL_MODULE % dict(name="",module=case1["name"],casetotal=case1["total"],passtotal=case1["passnum"],status=case1["status"],)
    table_tr1 += table_td_module

    #表头总数
    total_str = '共 %s，通过 %s，失败 %s' % (numfail + numsucc, numsucc, numfail)

    #case数据
    table_td_case=html.TABLE_TMPL_CASE % dict(name="",module=case2["name"],casetotal=case2["total"],passtotal=case2["passnum"],status=case2["status"],)
    table_tr2 += table_td_case

    output=html.HTML_TMPL % dict(value = total_str,table_tr = table_tr0,table_tr2=table_tr1,table_tr3=table_tr2)

    # 生成html报告
    filename='{date}_TestReport.html'.format(date=time.strftime('%Y%m%d%H%M%S'))

    print(filename)
    #获取report的路径
    dir= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'report')
    filename=os.path.join(dir,filename)

    with open(filename, 'wb') as f:
        f.write(output.encode('utf8'))