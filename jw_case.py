#-*- coding:utf-8 -*-
from time import sleep
import os
import re
import uiautomator2 as u2
from PIL import Image
import math
import operator
from functools import reduce
import threading


# def app_start(u):
#     u.press("home")
#     sleep(1)
#     u.press("recent")
#     sleep(2)
#     u(description="清除全部-按钮").click()
#     sleep(2)
#     u.app_start('com.yoosee')
#     sleep(6)
#     st = 0
#     while True:
#         st = st + 1
#         if u(text="设备").exists(timeout=3):
#             break
#         else:
#             sleep(2)
#         if st == 3:
#             break
#     assert u(text='设备').exists, '没有进入首页设备列表'

class JiWei:
    def app_start(u):
        u.press("home")
        sleep(1)
        u.press("home")
        sleep(1)
        u.press("recent")
        sleep(2)
        u(description="清除全部-按钮").click(timeout=5)
        sleep(3)
        # u.app_start('com.yoosee')
        # screen = u.window_size()
        u.app_start('com.yoosee')
        sleep(8)

    @classmethod
    def jwt_01(cls, u):  # 登录、权限、弹窗处理
        # 当天的日期
        # datetime.now().strftime('%Y-%m-%d')
        u.app_clear('com.yoosee')  # 清除应用数据
        # http_method_01 = 'post'  # 请求方式
        # sleep(1)
        # u.press("home")
        # sleep(1)
        # u.press("home")
        # sleep(2)
        # screen = u.window_size()
        # print (screen,screen[0])
        # a = screen.values()
        # start1 = datetime.now()
        u.app_start('com.yoosee')
        sleep(8)
        if u(text='用户服务协议和隐私政策概要').exists:
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
            sleep(3)
            assert u(text='登录').exists, '未进入登录界面'
        else:
            assert u(text='用户服务协议和隐私政策概要').exists, '用户服务协议弹窗不存在'

        #登录
        u(resourceId="com.yoosee:id/et_account").set_text("18124033125")
        sleep(2)
        u(resourceId="com.yoosee:id/et_pwd").set_text("@tang123")
        sleep(2)
        u(resourceId='com.yoosee:id/btn_login').click(timeout=5)
        sleep(3)
        assert not u(text='登录').exists, '密码正确仍在登录界面，可能网络有问题'
        #弹框点击
        T = 0
        while True:
            # if u(text='立即更新').exists:
            #     u(resourceId='com.yoosee:id/iv_close_device_update').click(timeout=5)
            if u(text='检测到新版本').exists:
                u(resourceId='com.yoosee:id/tx_next').click(timeout=5)
            elif u(resourceId='com.yoosee:id/iv_close_device_update').exists:#com.yoosee:id/dialog_content
                    u(resourceId='com.yoosee:id/tx_next').click(timeout=5)
            elif u(resourceId='com.yoosee:id/content_text4').exists:
                    u(resourceId='com.yoosee:id/right_btn').click(timeout=5)
            elif u(text='权限请求').exists:
                    u(resourceId='com.android.permissioncontroller:id/permission_allow_foreground_only_button').click(timeout=5)
            elif u(text='设备').exists:
                u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
                sleep(6)
                try:
                    u(text="推送消息提醒").exists
                    u(resourceId='com.yoosee:id/tx_deep_understand').click(timeout=5)
                    u(resourceId='com.yoosee:id/iv_back').click(timeout=5)
                except:
                    pass
                break
            elif T == 5:
                break
            T = T + 1
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_02(cls, u):  # 添加有线设备
        u.app_start('com.yoosee')
        sleep(8)
        if u(text="推送消息提醒").exists:
            u(resourceId='com.yoosee:id/tx_deep_understand').click(timeout=5)
            u(resourceId='com.yoosee:id/iv_back').click(timeout=5)
            sleep(3)
        screen = u.window_size()
        if not u(text="有线连接自动化测试",resourceId="com.yoosee:id/tv_name").exists and not u(text="27098235",resourceId="com.yoosee:id/tv_name").exists:
        # u(text='添加新设备').click_exists(timeout=5.0)
            u(resourceId="com.yoosee:id/button_add").click(timeout=5)
            sleep(2)
            if u(text='权限请求').exists:
                u(resourceId='com.android.permissioncontroller:id/permission_allow_button').click(timeout=5)
            u(resourceId='com.yoosee:id/line_add').click(timeout=5)
            u(resourceId="com.yoosee:id/config_cb").click(timeout=5)
            u(text='下一步').click(timeout=5)
            for wt in range(0,10):
                if u(text='27098235').exists:
                    u(text='27098235').click(timeout=5)
                    break
                try:
                    u.drag(screen[0] / 2, screen[1] / 3, screen[0] / 2,(screen[1] - 600), 0.2)
                    sleep(8)
                except:
                    pass
            # u(resourceId="com.yoosee:id/et_name").click_exists(timeout=5.0)
            # sleep(2)
            u(resourceId='com.yoosee:id/et_name').set_text("有线连接自动化测试")
            sleep(2)
            u.press("back")
            sleep(2)
            u(text='确定').click(timeout=5)
            u(text='分享给亲友').click(timeout=5)
            u(text='设备分享').click(timeout=5)
            u(text='二维码分享').click(timeout=5)
            sleep(3)
            if u(text='确定').exists:
                u(text='确定').click(timeout=5)
                sleep(3)
            assert u(resourceId='com.yoosee:id/qrcode_iv').exists,'没有生成二维码'
            sleep(2)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_03(cls, u):  # 删除设备
        u.app_start('com.yoosee')
        sleep(8)
        try:
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
            sleep(3)
        except:
            pass
        if u(resourceId='com.yoosee:id/setting_more_iv').exists:
            screen = u.window_size()
            u(resourceId="com.yoosee:id/setting_more_iv").click(timeout=5)
            u(resourceId="com.yoosee:id/pop_set_ll").click(timeout=5)
            for i in range(0,5):
                try:
                    u.drag(screen[0] / 2, (screen[1] - 600), screen[0] / 2, screen[1] / 3, 0.3)
                    sleep(3)
                except:
                    pass
                if u(text='删除设备').exists:
                    break
            sleep(1)
            u(text='删除设备').click(timeout=5)
            u(text='确定').click(timeout=5)
            sleep(3)
            assert u(text='设备').exists, '没有删除'
            sleep(2)
            u.press("back")
            sleep(1)
            u.press("back")
            sleep(1)
            u.press("back")
            sleep(1)
            u.press("back")
            sleep(1)

    @classmethod
    def jwt_04(cls, u):  # 警报
        u.app_start('com.yoosee')
        sleep(8)
        screen = u.window_size()
        try:
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
            sleep(3)
        except:
            pass
        u.drag(screen[0] / 2, screen[1] / 3, screen[0] / 2, (screen[1] - 600), 0.2)
        sleep(5)
        if u(text='不报警').exists:
            u(text='不报警').click(timeout=5)
            u(text='我知道了').click(timeout=5)
            sleep(1)
            try:
                assert u(text='警戒中').exists, '警戒中按键点击状态不对'
            except:
                if  u(text='检测到画面变化').exists:
                    u.press("back")
                    sleep(2)
                    assert u(text='警戒中').exists, '警戒中按键点击状态不对'
            # sleep(3)
            u(text='警戒中').click(timeout=5)
            u(text='我知道了').click(timeout=5)
            # if u(text='我知道了').exists:
            #     u(text='我知道了').click(timeout=5)
            # if  u(text='检测到画面变化').exists:
            #     u.press("back")
            #     sleep(2)
            # sleep(5)
            sleep(1)
            assert u(text='不报警').exists, '不报警按键点击状态不对'
            sleep(2)
        elif u(text='警戒中').exists:
            u(text='警戒中').click(timeout=5)
            u(text='我知道了').click(timeout=5)
            # if u(text='我知道了').exists:
            #     u(text='我知道了').click(timeout=5)
            # if  u(text='检测到画面变化').exists:
            #     u.press("back")
            #     sleep(2)
            sleep(1)
            assert u(text='不报警').exists, '不报警按键点击状态不对'
            u(text='不报警').click(timeout=5)
            u(text='我知道了').click(timeout=5)
            # if u(text='我知道了').exists:
            #     u(text='我知道了').click(timeout=5)
            #     sleep(2)
            #     assert u(text='警戒中').exists, '警戒中按键点击状态不对'
            # if u(text='检测到画面变化').exists:
            #     u.press("back")
            #     sleep(2)
            sleep(1)
            assert u(text='警戒中').exists, '警戒中按键点击状态不对'
            u(text='警戒中').click(timeout=5)
            u(text='我知道了').click(timeout=5)
        sleep(2)
        assert u(text='警戒中').exists or u(text='不报警').exists, '无报警按键'
        sleep(3)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_05(cls, u):  # 监控屏幕清晰度
        u.app_start('com.yoosee')
        sleep(8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(2)
        if u(text='新功能来啦！').exists:
            u(text='我知道了').click(timeout=5)
        sleep(2)
        if u(text='“有看头”需要您的存储权限，才能保存文件').exists:
            u(text='同意').click(timeout=5)
        sleep(2)
        if u(text='权限请求').exists:
            u(text='允许').click(timeout=5)
        sleep(5)
        for kc in range(0,2):
            if u(resourceId='com.yoosee:id/iv_raw').exists:
                u(resourceId='com.yoosee:id/iv_raw').click(timeout=5)
                sleep(1)
        sleep(2)
        if u(text='新功能来啦！').exists:
            u(text='我知道了').click(timeout=5)
            sleep(2)
        assert u(resourceId='com.yoosee:id/center_direction_view').exists, '未进入监控屏幕'
        sleep(6)
        assert not u(resourceId='com.yoosee:id/tv_iot_definition').exists, '分辨率展示没有消失'
        sleep(1)
        u.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        u(resourceId='com.yoosee:id/tv_iot_definition').click(timeout=5)
        u(text='超清').click(timeout=5)
        assert u(text='超清').exists, '切换超清未成功'
        sleep(1)
        u(resourceId='com.yoosee:id/iv_set').click(timeout=5)
        sleep(2)
        u.press("back")
        sleep(1)
        u.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        sleep(2)
        try:
            assert u(text='超清').exists, '进入设置返回未保存上一次分辨率'
        except:
            u.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
            sleep(2)
            assert u(text='超清').exists, '进入设置返回未保存上一次分辨率'
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod # 监控屏幕声音
    def jwt_06(cls, u):  # 监控屏幕
        u.app_start('com.yoosee')
        sleep(8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        #进入后截取声音图标
        voice_icon_coordinates = u(resourceId='com.yoosee:id/iv_p_voice').center()
        u.screenshot("voice1.png")
        Image.open("voice1.png").crop((voice_icon_coordinates[0], voice_icon_coordinates[1], voice_icon_coordinates[0]+50, voice_icon_coordinates[1]+50)).save("a.png")
        #点击声音后截取图标
        u(resourceId='com.yoosee:id/iv_p_voice').click(timeout=5)
        sleep(2)
        u.screenshot("voice2.png")
        Image.open("voice2.png").crop((voice_icon_coordinates[0], voice_icon_coordinates[1], voice_icon_coordinates[0]+50, voice_icon_coordinates[1]+50)).save("b.png")
        image_a = Image.open("a.png")
        image_b = Image.open("b.png")
        h1 = image_a.histogram()
        h2 = image_b.histogram()
        rms = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        # print (rms)
        assert rms > 10,'切换声音图标不正确'
        sleep(2)
        u(resourceId='com.yoosee:id/iv_p_voice').click(timeout=5)
        sleep(2)
        u.screenshot("voice3.png")
        Image.open("voice3.png").crop((voice_icon_coordinates[0], voice_icon_coordinates[1], voice_icon_coordinates[0]+50, voice_icon_coordinates[1]+50)).save("c.png")
        image_c = Image.open("c.png")
        image_a = Image.open("a.png")
        h1 = image_c.histogram()
        h2 = image_a.histogram()
        rms = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        # print(rms)
        assert rms < 10, '切换回声音图标不正确'
        sleep(2)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_07(cls, u):   # 监控屏幕录像
        u.app_start('com.yoosee')
        sleep(8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        u(resourceId='com.yoosee:id/iv_p_video').click(timeout=5)
        sleep(2)
        assert u(text='REC').exists, '没有录像'
        sleep(5)
        u(resourceId='com.yoosee:id/iv_p_video').click(timeout=5)
        assert not u(text='REC').exists, '未停止录像'
        sleep(2)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_08(cls, u):  # 监控屏幕对讲
        u.app_start('com.yoosee')
        sleep(8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        u(resourceId='com.yoosee:id/iv_p_speak').click(timeout=5)
        sleep(2)
        if u(text='权限请求').exists:
            u(text='允许').click(timeout=5)
            sleep(2)
        assert not u.xpath('//*[@resource-id="com.yoosee:id/iv_iot_talking"]/android.widget.LinearLayout[1]').exists, '对讲图标未消失'
        sleep(2)
        #多线程
        def run_1():
            u(resourceId='com.yoosee:id/iv_p_speak').long_click(5)
        def run_2():
            sleep(2)
            assert u.xpath(
                '//*[@resource-id="com.yoosee:id/iv_iot_talking"]/android.widget.LinearLayout[1]').exists, '对讲图标不存在'

        t1 = threading.Thread(target=run_1)
        t1.start()
        sleep(1)
        t2 = threading.Thread(target=run_2)
        t2.start()
        sleep(2)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_09(cls, u):  # 更多菜单
        u.app_start('com.yoosee')
        sleep(8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        u(resourceId='com.yoosee:id/more_btn').click(timeout=5)
        sleep(2)
        assert u(resourceId='com.yoosee:id/layout_center').exists, '不存在更多菜单'
        sleep(2)
        u(resourceId='com.yoosee:id/more_btn').click(timeout=5)
        sleep(2)
        assert not u(resourceId='com.yoosee:id/root_view').exists, '收起后仍存在更多菜单'
        sleep(2)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_10(cls, u):  # 监控屏幕全屏图标
        u.app_start('com.yoosee')
        sleep(8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        u(resourceId='com.yoosee:id/more_btn').click(timeout=5)
        sleep(2)
        u.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        sleep(2)
        assert u(resourceId='com.yoosee:id/iv_full_screen').exists, '不显示全屏按钮'
        sleep(6)
        assert not u(resourceId='com.yoosee:id/iv_full_screen').exists, '仍显示全屏按钮'
        sleep(2)
        u.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        sleep(2)
        u(resourceId='com.yoosee:id/iv_full_screen').click(timeout=5)
        sleep(2)
        assert u(resourceId='com.yoosee:id/iv_hangup').exists, '未切换全屏'
        sleep(2)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_11(cls, u):  # 监控屏幕截图图标
        u.app_start('com.yoosee')
        sleep(8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        u(resourceId='com.yoosee:id/iv_p_screenshot').click(timeout=5)
        sleep(2)
        assert u.xpath(
            '//*[@resource-id="com.yoosee:id/layout_p2p"]/android.widget.ImageView[1]').exists, '截图后缩略图不存在'
        u.xpath(
            '//*[@resource-id="com.yoosee:id/layout_p2p"]/android.widget.ImageView[1]').click()
        sleep(2)
        u(resourceId='com.yoosee:id/iv_share').click(timeout=5)
        u(text='取消').click(timeout=5)
        u(resourceId='com.yoosee:id/iv_delete').click(timeout=5)
        u(text='是').click(timeout=5)
        sleep(2)
        assert u(resourceId='com.yoosee:id/center_direction_view').exists, '未删除成功'
        sleep(2)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_12(cls, u):  # 卡回放暂停播放全屏
        u.app_start('com.yoosee')
        sleep(8)
        screen = u.window_size()
        try:
            u(resourceId='com.yoosee:id/tv_playback').click(timeout=6)
            sleep(5)
        except:
            u.drag(screen[0] / 2, screen[1] / 3, screen[0] / 2, (screen[1] - 600), 0.2)
            sleep(5)
            u(resourceId='com.yoosee:id/tv_playback').click(timeout=6)
            sleep(5)
        if u(resourceId='com.yoosee:id/iv_half_screen').exists:
            sleep(3)
            u(resourceId='com.yoosee:id/rl_vedioplayer_area').click(timeout=5)
        else:
            u(resourceId='com.yoosee:id/rl_vedioplayer_area').click(timeout=5)
        sleep(2)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast").info
        sleep(1)
        assert play_status['enabled'] == True,'没有自动播放'
        sleep(1)
        u(resourceId='com.yoosee:id/play_iv').click(timeout=5)
        sleep(1)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast").info
        sleep(2)
        assert play_status['enabled'] == False, '仍在播放'
        sleep(1)
        u(resourceId='com.yoosee:id/play_iv').click(timeout=5)
        sleep(2)
        screen_icon_coordinates = u(resourceId='com.yoosee:id/rl_vedioplayer_area').center()
        u(resourceId='com.yoosee:id/iv_half_screen').click(timeout=5)
        sleep(6)
        u.click(screen_icon_coordinates[0],screen_icon_coordinates[1])
        sleep(3)
        assert u(resourceId='com.yoosee:id/iv_portrait_screen').exists,'没进入全屏界面'
        sleep(1)
        u(resourceId='com.yoosee:id/iv_portrait_screen').click(timeout=5)
        sleep(3)
        assert u(resourceId='com.yoosee:id/fl_videoplayer_parent').exists,'没进入横屏界面'
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)

    @classmethod
    def jwt_13(cls, u):  # 卡回放时间轴
        u.app_start('com.yoosee')
        sleep(8)
        screen = u.window_size()
        try:
            u(resourceId='com.yoosee:id/tv_playback').click(timeout=6)
            sleep(5)
        except:
            u.drag(screen[0] / 2, screen[1] / 3, screen[0] / 2, (screen[1] - 600), 0.2)
            sleep(5)
            u(resourceId='com.yoosee:id/tv_playback').click(timeout=6)
            sleep(5)
        timeline_icon_coordinates = u(resourceId='com.yoosee:id/fl_videoplayer_parent').center()
        u.drag(timeline_icon_coordinates[0]-100,timeline_icon_coordinates[1], timeline_icon_coordinates[0], timeline_icon_coordinates[1], 0.2)
        sleep(5)
        play_time1 = 0
        while True:
            if u(resourceId='com.yoosee:id/iv_play').exists:
                sleep(3)
                play_time1 = play_time1 + 1
            else:
                break
            if play_time1 == 3:
                break
        u.drag(timeline_icon_coordinates[0] + 100, timeline_icon_coordinates[1], timeline_icon_coordinates[0],
               timeline_icon_coordinates[1], 0.2)
        sleep(5)
        play_time2 = 0
        while True:
            if u(resourceId='com.yoosee:id/iv_play').exists:
                sleep(3)
                play_time2 = play_time2 + 1
            else:
                break
            if play_time2 == 3:
                break
        u(resourceId='com.yoosee:id/date_tv')[3].click(timeout=5)
        sleep(5)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
        u.press("back")
        sleep(1)
