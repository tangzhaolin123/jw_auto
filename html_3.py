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
                    <th>步数</th>
                    <th>时间</th>
                    <th>用例执行结果</th>
                    <th>原因</th>
                </tr>
                %(table_tr)s
            </table>
        </body>
        </html>"""

    TABLE_TMPL = """
        <tr class='failClass warning'>
            <td>%(step)s</td>
            <td>%(runtime)s</td>
            <td>%(runresult)s</td>
            <td>%(reason)s</td>
        </tr>"""


if __name__ == '__main__':

    table_tr0 = ''

    numfail = 1

    numsucc = 9
    html = Template_mixin()

    table_td = html.TABLE_TMPL % dict(
    step = '1',
    runtime = datetime.now(),
    runresult = 'Fail',
    reason = '失败或成功原因',
    )
    table_tr0 += table_td

    total_str = '共 %s，通过 %s，失败 %s' % (numfail + numsucc, numsucc, numfail)
    output = html.HTML_TMPL % dict(
    value = total_str,
    table_tr = table_tr0,
    )

    # 生成html报告

    with open("Decision_KKD.html", 'wb') as f:
        f.write(output.encode('utf-8'))