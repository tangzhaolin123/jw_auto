# -*- coding:utf-8 -*-
import uiautomator2 as u2
from time import sleep
# # 连接被叫设备
u = u2.connect('3f3582df')

# 注册一个名字为"DECLINE"的watcher，当存在UiSelector的description="拒绝"时，点击



# d.watcher.when("同意").click(text = '同意')
# d.watcher.start()
#
#
# print("Watchers 1:", d.watcher)
# with d.watch_context() as ctx:
#     # ctx.when("^立即(下载|更新)").when("取消").click()  # 当同时出现 （立即安装 或 立即取消）和 取消 按钮的时候，点击取消
#     ctx.when("同意").click()
    # ctx.when("确定").click()
    # # 上面三行代码是立即执行完的，不会有什么等待
    #
    # ctx.wait_stable()  # 开启弹窗监控，并等待界面稳定（两个弹窗检查周期内没有弹窗代表稳定）
    #
    # # 使用call函数来触发函数回调
    # # call 支持两个参数，d和el，不区分参数位置，可以不传参，如果传参变量名不能写错
    # # eg: 当有元素匹配仲夏之夜，点击返回按钮
    # ctx.when("仲夏之夜").call(lambda d: d.press("back"))
    # ctx.when("确定").call(lambda el: el.click())

    # 其他操作
#方式  1
# ctx = d.watch_context()
# ctx.when("暂不使用").click()
# ctx.wait_stable() # 等待界面不在有弹窗了
#
# sleep(60)
#
# ctx.close()

#方式2
# d.watcher.when("暂不使用").click()
# d.watcher.start()
# sleep(60)
# 为了方便也可以使用代码中默认的弹窗监控逻辑
# 下面是目前内置的默认逻辑，可以加群at群主，增加新的逻辑，或者直接提pr
# when("继续使用").click()
# when("移入管控").when("取消").click()
# when("^立即(下载|更新)").when("取消").click()
# when("同意").click()
# when("^(好的|确定)").click()
# with d.watch_context(builtin=True) as ctx:
#     # 在已有的基础上增加
#     ctx.when("@tb:id/jview_view").when('//*[@content-desc="图片"]').click()

    # 其他脚本逻辑
# class SameOperation():
#     # def __init__(self, u: "uiautomator2.Device"):
#     #     self._u = u
#
#     def write_off(self):
#         # if not u(text='登录').exists:
#         #     #退出登录
#         #     u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
#         #     sleep(1)
#         #     u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
#         #     u(resourceId='com.yoosee:id/iv_headimg').click(timeout=5)
#         #     u(resourceId='com.yoosee:id/btn_logout').click(timeout=5)
#         #     sleep(5)
#         print ('1')
# SameOperation.write_off(u)

def find_deldevices(u,set_name):
    screen = u.window_size()
    u(resourceId="com.yoosee:id/setting_more_iv").click(timeout=5)
    sleep(2)
    u(resourceId="com.yoosee:id/pop_set_ll").click(timeout=5)
    for del_i in range(0, 5):
        if u(text=set_name).exists:
            break
        else:
            try:
                u.drag(screen[0] / 2, (screen[1] - 600), screen[0] / 2, screen[1] / 3, 0.3)
                sleep(3)
            except:
                pass
    sleep(1)
while True:
    try:
        find_deldevices(u,'删除设备')
        u.press('back')
    except:
        break

u.press("recent")
sleep(2)
u(description="清除全部-按钮").click()
sleep(2)
# u(resourceId="com.android.systemui:id/recent_apps").click()