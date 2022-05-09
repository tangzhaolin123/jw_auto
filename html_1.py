from datetime import datetime
from datetime import timedelta
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
            %(caseList)s %(robotlog)s
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
    ENDING_TMPL = """
        <div id='ending'>&nbsp;</div>
            <div style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer">
            <a href="#"><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
            </span></a></div>
            """

if __name__ == '__main__':

    table_tr0 = ''

    numfail = 1

    numsucc = 9
    html = Template_mixin()

    table_td = html.TABLE_TMPL % dict(
    step = 'jwt_01',
    case_module = '进入APP',
    case_name = '同意用户服务协议',
    case_antecedents = '清除APP数据',
    case_testProcedure = '手机桌面进入有看头APP，弹出用户服务协议，点击同意',
    case_expectedResult = '进入有看头APP的登录界面',
    runresult = '<font color="red">Fail</font>',
    reason = '失败或成功原因 http://tangjw.xyz/2022-04-29_14.05.32.png',
    case_notes = '备注',
    )

    # table_td1 = html.TABLE_TMPL % dict(
    #     step=['2'],
    #     runresult='Fail',
    #     reason='失败或成功原因 http://tangjw.xyz/2022-04-29_14.05.32.png',
    # )
    table_tr0 = table_td
    # table_tr0 += table_td
    case_url = '<a href=https://docs.qq.com/slide/DTkRnVUFmRnZpRGxE?u=4dfd95e91e7744258ad9751ffecf041b>查看测试用例</a>'
    robot_log_url = '<a href=https://docs.qq.com/slide/DTkRnVUFmRnZpRGxE?u=4dfd95e91e7744258ad9751ffecf041b>机器人日志</a>'

    total_str = '共 %s，通过 %s，失败 %s，通过率 %s' % (numfail + numsucc, numsucc, numfail,str(float(numsucc/(numfail + numsucc))*100)+'%')
    start_time = '2022-04-30_15:15'
    total_time = '00:01:05'
    case_total = numfail + numsucc
    output = html.HTML_TMPL % dict(
    value = total_str,
    table_tr = table_tr0,
    startTime = start_time,
    totalTime =  total_time,
    caseList = case_url,
    robotlog = robot_log_url
    )

    # 123456生成html报告

    with open("Decision_KKD.html", 'wb') as f:
        f.write(output.encode('utf-8'))