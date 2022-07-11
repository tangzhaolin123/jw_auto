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
import configparser


cfgpath = "dbconf.ini"
config = configparser.ConfigParser()
config.read(cfgpath, encoding="gb2312")
phone_num = config.get('sec1', '手机登录的号码')
phone_pwd = config.get('sec1', '手机登录的密码')
class SameOperation:
    def log_out(self,u):
        if not u(text='登录').exists:
            # 退出登录
            for quit_n in range(5):
                if u(resourceId='com.yoosee:id/icon_setting_img').exists:
                    u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                    break
                else:
                    u.press("back")
            # 退出登录
            sleep(1)
            u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
            u(resourceId='com.yoosee:id/iv_headimg').click(timeout=5)
            u(resourceId='com.yoosee:id/btn_logout').click(timeout=5)
            sleep(5)
    def write_off(self,u):
        u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
        sleep(1)
        u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
        sleep(2)
        u(resourceId='com.yoosee:id/iv_headimg').click(timeout=5)
        u(text='注销账户').click(timeout=5)
        u(resourceId='com.yoosee:id/device_cb').click(timeout=5)
        u(resourceId='com.yoosee:id/continueTv').click(timeout=5)
        u(resourceId='com.yoosee:id/next_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/button1_text').click(timeout=5)

    def app_go(self,u):
        u.app_start('com.yoosee')
        gotimes = 0
        while True:
            if u(text="登录").exists:
                sleep(3)
                break
            elif u(text="用户服务协议和隐私政策概要").exists:
                sleep(3)
                break
            elif u(text="有看头",resourceId="com.yoosee:id/tv_contact").exists:
                sleep(3)
                if u(text="警戒中").exists:
                    u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
                break
            else:
                sleep(3)
                gotimes += 1
            if gotimes == 4:
                break
        if u(resourceId="com.yoosee:id/msgLayout").exists:
            sleep(2)
        if u(resourceId='com.yoosee:id/alarming').wait(timeout=10):
            u(resourceId="com.yoosee:id/iv_alarm_close").click(timeout=5)
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        sleep(1)
    def quit_app(self,u):
        for quit_n in range(2):
            sleep(1)
            u.press("back")
            sleep(1)
            if u(resourceId="com.yoosee:id/icon_contact_img").exists:
                u(resourceId="com.yoosee:id/icon_contact_img").click(timeout=5)
                sleep(2)
                break
            else:
                u.press("back")
                u.press("back")
        u.app_stop('com.yoosee')

    def add_wired(self,u,video_camera_name):
        # screen = u.window_size()
        #防止添加设备到其他账号上
        u.swipe_ext("down", scale=0.8)
        u(resourceId='com.yoosee:id/icon_setting_img').wait(timeout=5)
        u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
        sleep(1)
        u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
        if u(text='gw_test01@sina.com').wait(timeout=5):
            SameOperation().log_out(u)
            sleep(2)
            SameOperation().log_in(u, phone_num, phone_pwd)
        else:
            u(resourceId='com.yoosee:id/icon_contact').click(timeout=5)
            sleep(1)
            u(resourceId='com.yoosee:id/icon_contact').click(timeout=5)
        #添加设备
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            u(resourceId="com.yoosee:id/button_add").click(timeout=5)
            sleep(2)
            u(resourceId='com.yoosee:id/line_add').click(timeout=5)
            u(resourceId="com.yoosee:id/config_cb").click(timeout=5)
            u(text='下一步').click(timeout=5)
            for wt in range(0, 20):
                # try:
                #     u.drag(screen[0] / 2, screen[1] / 3, screen[0] / 2, (screen[1] - 600), 0.2)
                #     sleep(8)
                # except:
                #     pass
                u.swipe_ext("down", scale=0.8)
                sleep(3)
                if u(text='加载中').exists:
                    sleep(3)
                if u(text=video_camera_name).exists:
                    u(text=video_camera_name).click(timeout=5)
                    sleep(6)
                    if u(text='正在添加摄像机').exists:
                        u.press("back")
                        u(text='退出').click(timeout=5)
                    else:
                        break
            sleep(2)
            if u(resourceId='com.yoosee:id/et_name').exists:
                u(resourceId='com.yoosee:id/et_name').set_text("有线连接自动化测试")
                u.press("back")
                u(text='确定').click(timeout=5)
                sleep(2)
    def find_deldevices(self,u,set_name):
        # screen = u.window_size()
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            u(resourceId="com.yoosee:id/setting_more_iv").click(timeout=5)
            sleep(2)
            u(resourceId="com.yoosee:id/pop_set_ll").click(timeout=5)
            if u(text='增值服务').wait(timeout=5):
                u(scrollable=True).scroll.to(text=set_name)
            # for del_i in range(0, 5):
            #     if u(text= set_name).exists:
            #         break
            #     else:
            #         try:
            #             u.drag(screen[0] / 2, (screen[1] - 600), screen[0] / 2, screen[1] / 3, 0.3)
            #             sleep(3)
            #         except:
            #             pass
            sleep(1)

    def log_in(self,u,user_name,pw_code):
        # 登录
        u(resourceId="com.yoosee:id/et_account").set_text(user_name)
        sleep(2)
        u(resourceId='com.yoosee:id/et_pwd').click(timeout=5)
        u(resourceId="com.yoosee:id/et_pwd").set_text(pw_code)
        sleep(2)
        u(resourceId='com.yoosee:id/btn_login').click(timeout=5)
        sleep(5)
        # assert not u(text='登录').exists, '密码正确仍在登录界面，可能网络有问题'
        # sleep(2)
    def vivo_kill(self,u):
        u.press("home")
        sleep(1)
        u.press("recent")
        sleep(2)
        u(description="清除全部-按钮").click()
        sleep(6)

    def icon_statuscheck(self,u,control_id):
        # 进入后截取声音图标
        voice_icon_coordinates = u(resourceId=control_id).center()
        u.screenshot("icon_1.png")
        Image.open("icon_1.png").crop((voice_icon_coordinates[0]-10, voice_icon_coordinates[1]-10, voice_icon_coordinates[0] + 10,
                                       voice_icon_coordinates[1] + 10)).save("a.png")
        # 点击声音后截取图标
        u(resourceId=control_id).click(timeout=5)
        u.screenshot("icon_2.png")
        Image.open("icon_2.png").crop((voice_icon_coordinates[0]-10, voice_icon_coordinates[1]-10, voice_icon_coordinates[0] + 10,
                                       voice_icon_coordinates[1] + 10)).save("b.png")
        image_a = Image.open("a.png")
        image_b = Image.open("b.png")
        h1 = image_a.histogram()
        h2 = image_b.histogram()
        rms = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        # print (rms)
        return rms

    def img_statuscheck(self,im_1,im_2):
        image_a = Image.open(im_1)
        image_b = Image.open(im_2)
        h1 = image_a.histogram()
        h2 = image_b.histogram()
        rms = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        # print (rms)
        return rms

    def advertising_develop(self,u):
        Advertising = 0
        while True:
            for i in range(0, 10):
                u.app_start('com.yoosee')
                sleep(2)
                if u(text="摇一摇").exists or u(text="跳过").exists:
                    Advertising = 20
                    break
                elif i == 9:
                    break
                elif u(text="有看头", resourceId="com.yoosee:id/tv_contact").exists:
                    break
                Advertising = Advertising + 1
            if Advertising == 10 or Advertising == 20:
                break
            u.app_stop("com.yoosee")

    def pixel_value(self, u,position):
        u.screenshot('pixel.png')
        img = Image.open('pixel.png')
        return img.getpixel(position)

    def photo_delete(self,u):
        u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
        sleep(1)
        u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
        u(resourceId='com.yoosee:id/rl_album_low').click(timeout=5)
        if u(text='选择').wait(timeout=5):
            u(text='选择').click(timeout=5)
            u(text='全选').click(timeout=5)
            u(resourceId='com.yoosee:id/rl_screenshot_alldelete').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
            u(resourceId='com.yoosee:id/back_btn').click(timeout=5)
            u(resourceId='com.yoosee:id/icon_contact').click(timeout=5)
        else:
            u(resourceId='com.yoosee:id/back_btn').click(timeout=5)
            u(resourceId='com.yoosee:id/icon_contact').click(timeout=5)

    def account_sharing(self,u):
        u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5)
        u(resourceId='com.yoosee:id/setting_more_iv').click(timeout=5)
        u(resourceId='com.yoosee:id/pop_share_ll').click(timeout=5)
        u(resourceId='com.yoosee:id/account_share_tv').click(timeout=5)
        u(resourceId='com.yoosee:id/tx_save').click(timeout=5)
        u.xpath("//android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]").set_text("gw_test01@sina.com")
        u(resourceId='com.yoosee:id/confirm_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/share_confirm_ll').click(timeout=8)
        sleep(3)

class JiWei:
    @classmethod
    def jwt_01(cls, u, video_camera_name):  # 暂不使用用户服务协议
        u.app_clear('com.yoosee')  # 清除应用数据
        # u.watcher.stop()
        SameOperation().app_go(u)
        if u(text='用户服务协议和隐私政策概要').exists:
            u(resourceId='com.yoosee:id/tv_no').click(timeout=5)
            sleep(3)
            assert not u(text='登录').exists, '未进入登录界面'
        else:
            assert u(text='用户服务协议和隐私政策概要').exists, '用户服务协议弹窗不存在'

    @classmethod
    def jwt_02(cls, u,video_camera_name):  # 同意用户服务协议
        u.app_clear('com.yoosee')  # 清除应用数据
        # u.watcher.stop()
        SameOperation().app_go(u)
        if u(text='用户服务协议和隐私政策概要').exists:
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
            sleep(3)
            assert u(text='登录').exists, '未进入登录界面'
        else:
            assert u(text='用户服务协议和隐私政策概要').exists, '用户服务协议弹窗不存在'

    @classmethod
    def jwt_03(cls, u,video_camera_name):  # 正确邮箱登录
        SameOperation().app_go(u)
        if u(text='登录').exists:
            SameOperation().log_in(u,"gw_test01@sina.com","abcd1234")
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        else:
            SameOperation().log_out(u)
            SameOperation().log_in(u,"gw_test01@sina.com","abcd1234")
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        sleep(3)
        u(text="推送消息提醒").wait(timeout=10)
        try:
            u(text="消息通知说明").wait(timeout=5)
        except:
            u.press('back')
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_04(cls, u,video_camera_name):  # 退出登录
        SameOperation().app_go(u)
        sleep(2)
        if not u(text='登录').exists:
            sleep(3)
            SameOperation().log_out(u)
            assert u(text='登录').exists, '未退出登录'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_05(cls, u,video_camera_name):  # 第三方创建新账号
        SameOperation().app_go(u)
        if u(text='登录').exists:
            u(resourceId='com.yoosee:id/iv_wechat').click(timeout=5)
            sleep(5)
            if u(text='我是新用户,直接登录').exists:
                u(resourceId='com.yoosee:id/tv_newuser').click(timeout=5)
                sleep(5)
                assert u(text='添加新设备').exists, '创建新账号失败或设备列表有设备'
                u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                sleep(1)
                u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                assert u(text='天机').exists, '显示微信昵称天机显示不正确'
                #注销
                SameOperation().write_off(u)
                # u(resourceId='com.yoosee:id/getted_btn').click(timeout=5)
            else:
                # 注销
                SameOperation().write_off(u)
                # u(resourceId='com.yoosee:id/getted_btn').click(timeout=5)
                sleep(5)
                u(resourceId='com.yoosee:id/iv_wechat').click(timeout=5)
                u(resourceId='com.yoosee:id/tv_newuser').click(timeout=5)
                sleep(5)
                assert u(text='添加新设备').exists, '创建新账号失败或设备列表有设备'
                u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                sleep(1)
                u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                assert u(text='天机').exists, '显示微信昵称天机显示不正确'

                # 注销
                SameOperation().write_off(u)
                # u(resourceId='com.yoosee:id/getted_btn').click(timeout=5)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_06(cls, u,video_camera_name):  # 微信号登录
        SameOperation().app_go(u)
        if u(text='登录').exists:
            u(resourceId='com.yoosee:id/iv_wechat').click(timeout=5)
            sleep(5)
            if u(text='我是新用户,直接登录').exists:
                u(resourceId='com.yoosee:id/tv_newuser').click(timeout=5)
                sleep(5)
                # 退出登录
                SameOperation().log_out(u)
                u(resourceId='com.yoosee:id/iv_wechat').click(timeout=5)
                sleep(5)
                assert u(resourceId='com.yoosee:id/layout_title').exists, '没有进入首页设备列表'
                sleep(2)
                u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                sleep(1)
                u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                sleep(3)
                assert u(text='天机').exists, '显示微信昵称天机显示不正确'
            else:

                assert u(resourceId='com.yoosee:id/layout_title').exists, '没有进入首页设备列表'
                sleep(2)
                u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                sleep(1)
                u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
                sleep(3)
                assert u(text='天机').exists, '显示微信昵称天机显示不正确'
        else:
            # 退出登录
            SameOperation().log_out(u)
            u(resourceId='com.yoosee:id/iv_wechat').click(timeout=5)
            sleep(5)
            assert u(resourceId='com.yoosee:id/layout_title').exists, '没有进入首页设备列表'
            sleep(2)
            u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
            sleep(1)
            u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
            sleep(3)
            assert u(text='天机').exists, '显示微信昵称天机显示不正确'
        # 退出登录
        SameOperation().log_out(u)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_07(cls, u,video_camera_name):  # 正确手机号登录
        # u.watcher.start()
        SameOperation().app_go(u)
        if u(text='登录').exists:
            SameOperation().log_in(u, phone_num, phone_pwd)
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        else:
            SameOperation().log_out(u)
            SameOperation().log_in(u, phone_num, phone_pwd)
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        sleep(3)
        SameOperation().quit_app(u)


    @classmethod
    def jwt_08(cls, u,video_camera_name):  #有线正常添加-弹窗提示
        SameOperation().app_go(u)
        if not u(text="有线连接自动化测试",resourceId="com.yoosee:id/tv_name").exists and not u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            SameOperation().add_wired(u,video_camera_name)
            sleep(3)
            assert u(text='添加成功').exists, '没有添加成功提示'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_09(cls, u, video_camera_name):  # 有线正常添加-监控界面
        SameOperation().app_go(u)
        if u(text="有线连接自动化测试",resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            u.xpath(
                '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
            sleep(5)
            u(resourceId="com.yoosee:id/center_direction_view").click(timeout=10)
        SameOperation().quit_app(u)


    @classmethod
    def jwt_10(cls, u, video_camera_name):  # 有线正常添加-分享界面
        SameOperation().app_go(u)
        if u(text="有线连接自动化测试",resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            u(resourceId="com.yoosee:id/setting_more_iv").click(timeout=5)
            sleep(2)
            u(resourceId='com.yoosee:id/pop_share_ll').click(timeout=5)
            sleep(3)
            assert u(text='设备分享').wait(timeout=10), '等待10s没进入设备分享界面'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_11(cls, u, video_camera_name):  #删除设备二次弹框
        SameOperation().app_go(u)
        set_name = '删除设备'
        if u(resourceId='com.yoosee:id/setting_more_iv').exists:
            SameOperation().find_deldevices(u,set_name)
            u(text='删除设备').click(timeout=5)
            sleep(2)
            assert '删除摄像机' in u(resourceId="com.yoosee:id/title").get_text(),'没有弹出删除设备二次弹框'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_12(cls, u, video_camera_name):  # 删除设备二次弹框
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_no').click(timeout=5)
            u.press("back")
            assert u(resourceId='com.yoosee:id/setting_more_iv').exists,"不存在要删除的设备"
        SameOperation().quit_app(u)

    @classmethod
    def jwt_13(cls, u, video_camera_name):  # 删除设备二次弹框
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        sleep(5)
        assert not u(resourceId='com.yoosee:id/setting_more_iv').exists, "要删除的设备存在"


    @classmethod
    def jwt_14(cls, u, video_camera_name):  #支持云存设备弹窗-到购买云存储界面“点击“购买云存储”
        SameOperation().app_go(u)
        if u(text="有线连接自动化测试", resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        sleep(5)
        SameOperation().add_wired(u, video_camera_name)
        sleep(3)
        u(text='购买云存储').click(timeout=5)
        sleep(3)
        assert u(text="云服务").wait(timeout=10), '点击购买等了10s没有打开云存储'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_15(cls, u, video_camera_name):  # 支持云存设备弹窗-点击“查看我的设备”
        SameOperation().app_go(u)
        if u(text="有线连接自动化测试", resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        sleep(5)
        SameOperation().add_wired(u, video_camera_name)
        sleep(3)
        u(text='查看我的设备').click(timeout=5)
        u(resourceId="com.yoosee:id/center_direction_view").click(timeout=10)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_16(cls, u, video_camera_name):  #支持云存设备弹窗-点击“分享设备”
        SameOperation().app_go(u)
        if u(text="有线连接自动化测试", resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        sleep(5)
        SameOperation().add_wired(u, video_camera_name)
        sleep(3)
        u(text='分享给亲友').click(timeout=5)
        sleep(3)
        assert u(text='设备分享').wait(timeout=10), '等待10s多没进入设备分享界面'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_17(cls, u, video_camera_name):  #云存储列表入口
        SameOperation().app_go(u)
        if u(text="有线连接自动化测试", resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            u(text='云存储').click(timeout=5)
            assert u(text="云服务").wait(timeout=10), '点击购买等了10s没有打开云存储'
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press("back")
            u(text='云存储').click(timeout=5)
            assert u(text="云服务").wait(timeout=10), '点击购买等了10s没有打开云存储'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_18(cls, u, video_camera_name):  #云存储设置入口云存储状态
        SameOperation().app_go(u)
        set_name = '增值服务'
        if u(text="有线连接自动化测试", resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            SameOperation().find_deldevices(u,set_name)
            tx_vas = u(resourceId="com.yoosee:id/tx_vas").get_text()
            assert tx_vas == '已购买', '不显示已购买状态'
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press("back")
            SameOperation().find_deldevices(u, set_name)
            tx_vas = u(resourceId="com.yoosee:id/tx_vas").get_text()
            assert tx_vas == '已购买', '不显示已购买状态'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_19(cls, u, video_camera_name):  #设备列表有“新手教程
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
            sleep(5)
            assert u(text="新手教程").wait(timeout=5), '设备列表不存在新手教程'
        else:
            assert u(text="新手教程").wait(timeout=5), '设备列表不存在新手教程'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_20(cls, u, video_camera_name):  #前往“帮助中心_添加绑定”H5
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
            sleep(5)
            u(resourceId="com.yoosee:id/rl_question").click(timeout=5)
            sleep(3)
            assert u(text="新手教程",resourceId='com.yoosee:id/tv_title').wait(timeout=5), "没有前往帮助中心_添加绑定H5"
        else:
            sleep(2)
            u(resourceId="com.yoosee:id/rl_question").click(timeout=5)
            sleep(3)
            assert u(text="新手教程",resourceId='com.yoosee:id/tv_title').wait(timeout=5), "没有前往帮助中心_添加绑定H5"
        SameOperation().quit_app(u)

    @classmethod
    def jwt_21(cls, u, video_camera_name):  #国内topon开屏广告-展示
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u,  phone_num, phone_pwd)
        sleep(5)
        u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        u(text="推送消息提醒").wait(timeout=10)
        try:
            u(text="消息通知说明").wait(timeout=5)
        except:
            u(resourceId="com.yoosee:id/iv_back").click(timeout=5)
            # u.press('back')
        sleep(2)
        SameOperation().advertising_develop(u)
        assert u(text="摇一摇").exists or u(text="跳过").exists, "没有广告"
        SameOperation().quit_app(u)

    @classmethod
    def jwt_22(cls, u, video_camera_name):  #国内topon开屏广告-有倒计时5秒展示
        u.app_clear('com.yoosee')  # 清除应用数据
        # u.watcher.stop()
        SameOperation().app_go(u)
        SameOperation().log_in(u,  phone_num, phone_pwd)
        sleep(5)
        u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        u(text="推送消息提醒").wait(timeout=10)
        try:
            u(text="消息通知说明").wait(timeout=5)
        except:
            u(resourceId="com.yoosee:id/iv_back").click(timeout=5)
            # u.press('back')
        sleep(2)
        SameOperation().advertising_develop(u)
        assert u(text="摇一摇").exists or u(text="跳过").exists, "没有广告"
        SameOperation().quit_app(u)

    @classmethod
    def jwt_23(cls, u, video_camera_name):  #倒计时结束后跳到APP设备列表页面
        u.app_clear('com.yoosee')  # 清除应用数据
        # u.watcher.stop()
        SameOperation().app_go(u)
        SameOperation().log_in(u,  phone_num, phone_pwd)
        sleep(5)
        u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        u(text="推送消息提醒").wait(timeout=10)
        try:
            u(text="消息通知说明").wait(timeout=5)
        except:
            u(resourceId="com.yoosee:id/iv_back").click(timeout=5)
            # u.press('back')
        sleep(2)
        SameOperation().advertising_develop(u)
        u(text="有看头",resourceId="com.yoosee:id/tv_contact").wait(timeout=10), "倒计时结束后没有跳到APP设备列表页面"
        SameOperation().quit_app(u)

    @classmethod
    def jwt_24(cls, u, video_camera_name):  #国内topon开屏广告，不等倒计时点击跳过
        u.app_clear('com.yoosee')  # 清除应用数据
        # u.watcher.stop()
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        sleep(5)
        u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        u(text="推送消息提醒").wait(timeout=10)
        try:
            u(text="消息通知说明").wait(timeout=5)
        except:
            u(resourceId="com.yoosee:id/iv_back").click(timeout=5)
            # u.press('back')
        sleep(2)
        SameOperation().advertising_develop(u)
        if u(text="跳过").exists:
            u(text="跳过").click(timeout=5)
        elif u(resourceId="com.byted.pangle:id/tt_splash_skip_btn").exists:
            u(resourceId="com.byted.pangle:id/tt_splash_skip_btn").click(timeout=5)
        u(text="有看头", resourceId="com.yoosee:id/tv_contact").wait(timeout=10), "跳过广告后没有进入到APP设备列表页面"
        SameOperation().quit_app(u)

    @classmethod
    def jwt_25(cls, u, video_camera_name):  #国内topon开屏广告，跳过广告查看监控设备10s
        u.app_clear('com.yoosee')  # 清除应用数据
        # u.watcher.stop()
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        sleep(5)
        u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        u(text="推送消息提醒").wait(timeout=10)
        try:
            u(text="消息通知说明").wait(timeout=5)
        except:
            u(resourceId="com.yoosee:id/iv_back").click(timeout=5)
            # u.press('back')
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        sleep(2)
        SameOperation().advertising_develop(u)
        if u(text="跳过").exists:
            u(text="跳过").click(timeout=5)
        elif u(resourceId="com.byted.pangle:id/tt_splash_skip_btn").exists:
            u(resourceId="com.byted.pangle:id/tt_splash_skip_btn").click(timeout=5)
        u(text="有看头", resourceId="com.yoosee:id/tv_contact").wait(timeout=10)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(12)
        u(resourceId="com.yoosee:id/center_direction_view").click(timeout=10)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_26(cls, u, video_camera_name):  #云回放/卡回放切换
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/tv_download_list").wait(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        sleep(5)
        assert not u(resourceId="com.yoosee:id/tv_download_list").exists,'没有切换到卡回放'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_27(cls, u, video_camera_name):  #卡回放切换切换日期到过去
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/fl_videoplayer_parent").wait(timeout=5)
        u(resourceId='com.yoosee:id/date_tv')[2].click(timeout=5)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_28(cls, u, video_camera_name):  # 安装卸载-卸载成功
        try:
            app_us = u.app_info('com.yoosee')
        except:
            u.app_install('1.apk')
        u.app_uninstall('com.yoosee')
        app_exist= 0
        try:
            app_us = u.app_info('com.yoosee')
        except:
            app_exist = 1
        assert app_exist == 1,'app卸载不成功'

    @classmethod
    def jwt_29(cls, u, video_camera_name):  # 安装卸载-卸载后安装成功
        try:
            app_us = u.app_info('com.yoosee')
        except:
            u.app_install('1.apk')
        u.app_uninstall('com.yoosee')
        u.app_install('1.apk')
        app_exist = 0
        try:
            app_us = u.app_info('com.yoosee')
        except:
            app_exist = 1
        assert app_exist == 0,'app安装不成功'

    @classmethod
    def jwt_30(cls, u, video_camera_name):  # 安装卸载-覆盖安装成功
        try:
            app_us = u.app_info('com.yoosee')
        except:
            u.app_install('1.apk')
            SameOperation().app_go(u)
            SameOperation().log_in(u, phone_num, phone_pwd)
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
            u(text="推送消息提醒").wait(timeout=10)
            try:
                u(text="消息通知说明").wait(timeout=5)
            except:
                u.press('back')
            SameOperation().quit_app(u)
        u.app_install('1.apk')
        app_exist = 0
        try:
            app_us = u.app_info('com.yoosee')
        except:
            app_exist = 1
        assert app_exist == 0, 'app覆盖安装不成功'

    @classmethod
    def jwt_31(cls, u, video_camera_name):  # 安装卸载-覆盖安装成功不需要重新输入账号密码
        try:
            app_us = u.app_info('com.yoosee')
            SameOperation().app_go(u)
            if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
                pass
            else:
                SameOperation().add_wired(u, video_camera_name)
                u.press('back')
            SameOperation().quit_app(u)
        except:
            u.app_install('1.apk')
            SameOperation().app_go(u)
            SameOperation().log_in(u, phone_num, phone_pwd)
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
            u(text="推送消息提醒").wait(timeout=10)
            try:
                u(text="消息通知说明").wait(timeout=5)
            except:
                u.press('back')
            SameOperation().quit_app(u)
        u.app_install('1.apk')
        sleep(5)
        SameOperation().app_go(u)
        assert u(text="有看头",resourceId="com.yoosee:id/tv_contact").exists,'未进入首页即覆盖安装后要输入账号密码'

    @classmethod
    def jwt_32(cls, u, video_camera_name):  # 安装卸载-覆盖安装成功App内绑定设备显示正常
        try:
            app_us = u.app_info('com.yoosee')
            SameOperation().app_go(u)
            if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
                pass
            else:
                SameOperation().add_wired(u, video_camera_name)
                u.press('back')
            SameOperation().quit_app(u)
        except:
            u.app_install('1.apk')
            SameOperation().app_go(u)
            SameOperation().log_in(u, phone_num, phone_pwd)
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
            u(text="推送消息提醒").wait(timeout=10)
            try:
                u(text="消息通知说明").wait(timeout=5)
            except:
                u.press('back')
            if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
                pass
            else:
                SameOperation().add_wired(u, video_camera_name)
                u.press('back')
            SameOperation().quit_app(u)
        u.app_install('1.apk')
        sleep(5)
        SameOperation().app_go(u)
        assert u(resourceId='com.yoosee:id/setting_more_iv').exists,'覆盖安装后绑定设备不存在'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_33(cls, u, video_camera_name):  # 安装卸载-覆盖安装检查进入监控是否正常
        try:
            app_us = u.app_info('com.yoosee')
            SameOperation().app_go(u)
            if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
                pass
            else:
                SameOperation().add_wired(u, video_camera_name)
                u.press('back')
            SameOperation().quit_app(u)
        except:
            u.app_install('1.apk')
            SameOperation().app_go(u)
            SameOperation().log_in(u, phone_num, phone_pwd)
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
            u(text="推送消息提醒").wait(timeout=10)
            try:
                u(text="消息通知说明").wait(timeout=5)
            except:
                u.press('back')
            if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
                pass
            else:
                SameOperation().add_wired(u, video_camera_name)
                u.press('back')
            SameOperation().quit_app(u)
        u.app_install('1.apk')
        SameOperation().app_go(u)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(12)
        u(resourceId="com.yoosee:id/center_direction_view").click(timeout=10)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_34(cls, u, video_camera_name):  # 监控页设置入口
        SameOperation().app_go(u)
        if u(text="有线连接自动化测试", resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,
                                                                               resourceId="com.yoosee:id/tv_name").exists:
            u.xpath(
                '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
            sleep(5)
            u(resourceId="com.yoosee:id/iv_set").click(timeout=10)
            assert u(text="设置", resourceId="com.yoosee:id/tv_setting").wait(timeout=5), "没有进入监控页设置入口"
        SameOperation().quit_app(u)

    @classmethod
    def jwt_35(cls, u, video_camera_name):  # 设备列表页设置入口
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').exists:
            SameOperation().find_deldevices(u,'画面与声音')
            assert u(text="设置", resourceId="com.yoosee:id/tv_setting").wait(timeout=5), "没有进入监控页设置入口"
        SameOperation().quit_app(u)

    @classmethod
    def jwt_36(cls, u, video_camera_name):  # 卡回放-视频播放H265视频
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        sleep(10)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast").info
        sleep(3)
        assert play_status['enabled'] == True, '没有自动播放'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_37(cls, u, video_camera_name):  # 卡回放-时间轴拖动
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        u(resourceId='com.yoosee:id/fl_videoplayer_parent').wait(timeout=5)
        timeline_icon_coordinates = u(resourceId='com.yoosee:id/fl_videoplayer_parent').center()
        u.drag(timeline_icon_coordinates[0] - 100, timeline_icon_coordinates[1], timeline_icon_coordinates[0],
               timeline_icon_coordinates[1], 0.2)
        # u(resourceId="com.yoosee:id/fl_videoplayer_parent").swipe("right", steps=10)
        sleep(5)
        u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        sleep(1)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        sleep(3)
        pix1 = SameOperation().pixel_value(u,timeline_icon_coordinates)
        # print('pix1', pix1)
        if pix1[0] < 120 and pix1[1] < 120:
            play_status = u(resourceId="com.yoosee:id/iv_playback_fast").info
            assert play_status['enabled'] == True, '时间轴向前快速滑动没有自动播放'
        u.drag(timeline_icon_coordinates[0] + 100, timeline_icon_coordinates[1], timeline_icon_coordinates[0],
               timeline_icon_coordinates[1], 0.2)
        # u(resourceId="com.yoosee:id/fl_videoplayer_parent").swipe("left", steps=10)
        sleep(5)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        sleep(3)
        pix2 = SameOperation().pixel_value(u, timeline_icon_coordinates)
        # print ('pix2',pix2)
        if pix2[0] < 120 and pix2[1] < 120:
            play_status = u(resourceId="com.yoosee:id/iv_playback_fast").info
            assert play_status['enabled'] == True, '时间轴向后快速滑动没有自动播放'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_38(cls, u, video_camera_name):  #首次打开云回放，默认播放
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").wait(timeout=5)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(20)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_39(cls, u, video_camera_name):  #播放界面小控件竖屏 - 播放按钮
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").wait(timeout=5)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        # u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
        stop_status = SameOperation().icon_statuscheck(u,"com.yoosee:id/play_iv")
        assert stop_status > 0,'播放状态不对'
        # sleep(8)
        # if not u(resourceId="com.yoosee:id/play_iv").exists:
        #     u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        # u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_40(cls, u, video_camera_name):  #播放界面小控件竖屏 - 暂停时按钮状态
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
        sleep(0.5)
        stop_status = SameOperation().icon_statuscheck(u,"com.yoosee:id/play_iv")
        assert stop_status > 0, '暂停状态不对'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_41(cls, u, video_camera_name):  #播放界面小控件竖屏 - 截图
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
        u(resourceId="com.yoosee:id/iv_palyback_screenshot_btn").click(timeout=5)
        assert u.xpath('//*[@resource-id="com.yoosee:id/rl_vedioplayer_area"]/android.widget.ImageView[1]').wait(timeout=8), '左下角没显示截图缩略图'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_42(cls, u, video_camera_name):  #播放界面小控件下载保存
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        # u(resourceId="com.yoosee:id/tv_playback").wait(timeout=5)
        # sleep(1)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        #清除下载任务
        u(resourceId="com.yoosee:id/tv_download_list").click(timeout=5)
        u(resourceId="com.yoosee:id/rbtn_right").click(timeout=5)
        if u(resourceId="com.yoosee:id/top_tv").exists:
            u(resourceId="com.yoosee:id/top_tv").click(timeout=5)
            u(resourceId="com.yoosee:id/ll_select_all").click(timeout=5)
            u(resourceId="com.yoosee:id/ll_delete").click(timeout=5)
            u(resourceId="com.yoosee:id/tv_yes").click(timeout=5)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        sleep(10)
        if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
        u(resourceId="com.yoosee:id/iv_playback_to_dwonload").click(timeout=5)
        u(resourceId="com.yoosee:id/iv_palyback_dwonload_ok").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_download_list").click(timeout=5)
        try:
            assert u(resourceId="com.yoosee:id/rl_download_start").wait(timeout=5), '下载中无下载任务'
        except:
            assert u(resourceId="com.yoosee:id/rl_download_start").wait(timeout=5), '下载中和已下载都无任务'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_43(cls, u, video_camera_name):  #云回放切换日期到过去
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        # u(resourceId="com.yoosee:id/tv_playback").wait(timeout=5)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        sleep(1)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        u(resourceId='com.yoosee:id/date_tv')[2].click(timeout=5)
        sleep(10)
        if not u(text="暂无录像").exists:
            if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
                u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            # u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
            sleep(1)
            stop_status = SameOperation().icon_statuscheck(u,"com.yoosee:id/play_iv")
            # print (stop_status)
            assert stop_status > 0, '回放播放状态不对'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_44(cls, u, video_camera_name):  #云回放消息列表-播放视频
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        sleep(3)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if not u(text="暂无录像").exists:
            u(resourceId='com.yoosee:id/detection_time_tv')[0].click(timeout=5)
            sleep(5)
            assert u(text="正在预览").wait(timeout=5), '点击后没有正在预览'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_45(cls, u, video_camera_name):  #云回放时间刻度尺横竖屏切换播放
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        u(resourceId="com.yoosee:id/iv_half_screen").click(timeout=5)
        sleep(2)
        if not u(resourceId="com.yoosee:id/ll_landscape_timeline").exists:
            u.xpath('//android.widget.FrameLayout[1]').click()
        u(resourceId="com.yoosee:id/play_land_iv").click(timeout=5)
        assert u(resourceId="com.yoosee:id/ll_landscape_timeline").wait(timeout=5),'切换横屏时，刻度尺不存在'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_46(cls, u, video_camera_name):  #云回放时间刻度尺横竖屏切换播放
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/tv_playback").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        u(resourceId="com.yoosee:id/iv_half_screen").click(timeout=5)
        sleep(2)
        if not u(resourceId="com.yoosee:id/ll_landscape_timeline").exists:
            u.xpath('//android.widget.FrameLayout[1]').click()
        u(resourceId="com.yoosee:id/iv_portrait_screen").click(timeout=5)
        sleep(2)
        if not u(resourceId="com.yoosee:id/rl_functin_bar").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
        assert u(resourceId="com.yoosee:id/fl_videoplayer_parent").exists, '切换竖屏时，刻度尺不存在'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_47(cls, u, video_camera_name):  #banner广告
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        banner_times = 0
        while True:
            if u.xpath('//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.LinearLayout[1]').exists:
                break
            elif banner_times == 5:
                break
            u.swipe_ext("down", scale=0.8)
            sleep(3)
            banner_times = banner_times + 1
        assert u.xpath('//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.LinearLayout[1]').wait(timeout=8), '没有banner广告'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_48(cls, u, video_camera_name):  #设置云存入口
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        SameOperation().find_deldevices(u, '我的云存储')
        u(text='我的云存储').click(timeout=5)
        assert u(text="云服务").wait(timeout=10), '没有跳转到增值业务H5页面，页面标题未出现'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_49(cls, u, video_camera_name):  #设置基础全天/报警录像互切
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        SameOperation().find_deldevices(u, '录像设置')
        u(text='录像设置').click(timeout=5)
        u(text='报警录像').click(timeout=5)
        assert u(resourceId='com.yoosee:id/pt_alarm_record_time').wait(timeout=5), '切换报警录像失败'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_50(cls, u, video_camera_name):  #设置基础全天/报警录像互切
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        SameOperation().find_deldevices(u, '录像设置')
        u(text='录像设置').click(timeout=5)
        u(text='定时录像').click(timeout=5)
        assert u(resourceId='com.yoosee:id/pt_timed_record_time').wait(timeout=5), '切换定时录像失败'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_51(cls, u, video_camera_name):  #设置基础全天/报警录像互切
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        SameOperation().find_deldevices(u, '录像设置')
        u(text='录像设置').click(timeout=5)
        u(text='全天录像').click(timeout=5)
        assert u(resourceId='com.yoosee:id/sv_record_switch').wait(timeout=5), '切换全天录像失败'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_52(cls, u, video_camera_name):  #监控界面/更多-回放
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        u(resourceId='com.yoosee:id/more_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/root_view')[0].click(timeout=5)
        u(resourceId='com.yoosee:id/tv_sdcard_playback').click(timeout=5)
        sleep(5)
        if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        # u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast").info
        sleep(1)
        assert play_status['enabled'] == True, '没有自动播放'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_53(cls, u, video_camera_name):  #监控界面/更多-回放返回重新连接
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        u(resourceId='com.yoosee:id/more_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/root_view')[0].click(timeout=5)
        sleep(5)
        u(resourceId='com.yoosee:id/back_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/center_direction_view').wait(timeout=5)
        u.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click(timeout=5)
        assert u(resourceId='com.yoosee:id/bottom_control_rl').wait(timeout=5),'没有重新连接视频'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_54(cls, u, video_camera_name):  #监控界面/更多-回放返回收起更多菜单
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        sleep(5)
        u(resourceId='com.yoosee:id/more_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/root_view')[0].click(timeout=5)
        sleep(5)
        u(resourceId='com.yoosee:id/back_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/center_direction_view').wait(timeout=5)
        assert not u(resourceId='com.yoosee:id/root_view')[0].wait(timeout=5),'没有收起更多菜单'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_55(cls, u, video_camera_name):  #监控界面更多-报警开关布防状态
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
            u(resourceId='com.yoosee:id/ll_defence_state').wait(timeout=5)
        if u(text='警戒中').exists:
            u(text='警戒中').click(timeout=5)
            sleep(3)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(timeout=5)
        sleep(5)
        u(resourceId='com.yoosee:id/more_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/root_view')[1].click(timeout=5)
        sleep(3)
        u(resourceId='com.yoosee:id/back_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5)
        u.swipe_ext("down", scale=0.8)
        u(resourceId='com.yoosee:id/ll_defence_state').wait(timeout=5)
        assert u(resourceId="com.yoosee:id/tx_defence_state").get_text() == '警戒中','布防状态切换不成功'
        u(text='警戒中').click(timeout=5)
        sleep(2)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_56(cls, u, video_camera_name):  #监控界面更多-关闭报警，设备撤销布防
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
            u(resourceId='com.yoosee:id/ll_defence_state').wait(timeout=5)
        if u(text='警戒中').exists:
            u(text='警戒中').click(timeout=5)
            sleep(3)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(timeout=5)
        sleep(5)
        u(resourceId='com.yoosee:id/more_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/root_view')[1].click(timeout=5)
        sleep(3)
        u(resourceId='com.yoosee:id/root_view')[1].click(timeout=5)
        sleep(3)
        u(resourceId='com.yoosee:id/back_btn').click(timeout=5)
        u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5)
        u.swipe_ext("down", scale=0.8)
        u(resourceId='com.yoosee:id/ll_defence_state').wait(timeout=5)
        assert u(resourceId="com.yoosee:id/tx_defence_state").get_text() == '不报警', '设备撤销布防不成功'
        sleep(2)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_57(cls, u, video_camera_name):  #监控界面--显示全屏按钮，无操作5秒后隐藏后
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        u(resourceId="com.yoosee:id/iv_full_screen").wait(timeout=5)
        sleep(5)
        assert u(resourceId="com.yoosee:id/iv_full_screen").wait_gone(timeout=3.0),'无操作5秒后没隐藏'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_58(cls, u, video_camera_name):  #监控界面--切换到横屏监控
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        u(resourceId="com.yoosee:id/iv_full_screen").click(timeout=5)
        assert u(resourceId='com.yoosee:id/iv_hangup').wait(timeout=5),'没有切换横屏'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_59(cls, u, video_camera_name):  #监控界面--录像显示正在录像状态：REC
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        u(resourceId="com.yoosee:id/iv_p_video").click(timeout=5)
        sleep(2)
        assert u(resourceId='com.yoosee:id/tx_rec').wait(timeout=5), '没有显示正在录像状态：REC'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_60(cls, u, video_camera_name):  #监控界面--录像小于1秒时，再次点击录像
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        u(resourceId="com.yoosee:id/iv_p_video").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/iv_p_video").click(timeout=5)
            # if "视频片段时间太短了" in u.toast.get_message(5.0, 10.0, "default message"):
            #     print ('success')
            #     break
            # elif short_i == 4:
            #     print('fail')
            #     assert "视频片段时间太短了" in u.toast.get_message(5.0, 10.0, "default message"),'无视频太短提示'
            #     sleep(1)
        assert u(resourceId='com.yoosee:id/tx_rec').wait_gone(timeout=5),'停止录像了，仍显示正在录像状态：REC'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_61(cls, u, video_camera_name):  #监控界面--录像大于5秒时，再次点击录像
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        u(resourceId="com.yoosee:id/iv_p_video").click(timeout=5)
        sleep(6)
        u(resourceId="com.yoosee:id/iv_p_video").click(timeout=5)
        assert u(resourceId='com.yoosee:id/tx_rec').wait_gone(timeout=5),'停止录像了，仍显示正在录像状态：REC'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_62(cls, u, video_camera_name):  #监控界面--截图成功和保存
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
        sleep(1)
        assert "截图成功" in u.toast.get_message(5.0, 10.0, "default message"),'没提示截图成功'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_63(cls, u, video_camera_name):  #监控界面--左下角有截图缩略图
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
        assert u.xpath('//*[@resource-id="com.yoosee:id/layout_p2p"]/android.widget.ImageView[1]').wait(
            timeout=8), '左下角没显示截图缩略图'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_64(cls, u, video_camera_name):  #监控界面--点击可以查看截图大图
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
        u.xpath('//*[@resource-id="com.yoosee:id/layout_p2p"]/android.widget.ImageView[1]').click(timeout=5)
        assert u(resourceId="com.yoosee:id/tv_imagegallay_filesize").wait(timeout=5), '点击没能打开查看截图大图'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_65(cls, u, video_camera_name):  #监控界面--无点击操作3秒后隐藏截图
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
        sleep(3)
        assert u.xpath('//*[@resource-id="com.yoosee:id/layout_p2p"]/android.widget.ImageView[1]').wait_gone(
            timeout=3), '左下角没显示截图缩略图'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_66(cls, u, video_camera_name):  #快捷入口--时间轴日期当前播放的录像切换到另一天的录像
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/ll_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/fl_videoplayer_parent").wait(timeout=5)
        u(resourceId='com.yoosee:id/date_tv')[2].click(timeout=5)
        sleep(6)
        if u(text="暂无录像").wait(timeout=5):
            pass
        else:
            if u(resourceId="com.yoosee:id/rl_functin_bar").wait_gone(timeout=3.0):
                u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
                sleep(1)
            play_status = u(resourceId="com.yoosee:id/iv_playback_fast").info
            sleep(3)
            assert play_status['enabled'] == True, '切换到另一天录像没有自动播放'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_67(cls, u, video_camera_name):  #快捷入口--横屏 - 暂停键变成播放键
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/ll_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        sleep(5)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        #竖屏时时间轴
        timeline_icon_coordinates = u(resourceId='com.yoosee:id/fl_videoplayer_parent').center()
        u(resourceId="com.yoosee:id/iv_half_screen").click(timeout=5)
        if u(resourceId="com.yoosee:id/ll_landscape_timeline").wait_gone(timeout=3.0):
            # u.xpath('//android.widget.FrameLayout[1]').click(timeout=5)
            u.click(timeline_icon_coordinates[0], timeline_icon_coordinates[1])
            sleep(1)
        u(resourceId="com.yoosee:id/iv_playback_fast_landscape").wait(timeout=5)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast_landscape").info
        sleep(1)
        if play_status['enabled'] == True:
            u(resourceId="com.yoosee:id/play_land_iv").click(timeout=5)
            sleep(1)
            play_status = u(resourceId="com.yoosee:id/iv_playback_fast_landscape").info
            assert play_status['enabled'] == False, '仍在播放'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_68(cls, u, video_camera_name):  #快捷入口--横屏 - 录像暂停，时间轴不动
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/ll_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        sleep(5)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        # 竖屏时时间轴
        timeline_icon_coordinates = u(resourceId='com.yoosee:id/fl_videoplayer_parent').center()
        u(resourceId="com.yoosee:id/iv_half_screen").click(timeout=5)
        if u(resourceId="com.yoosee:id/ll_landscape_timeline").wait_gone(timeout=3.0):
            # u.xpath('//android.widget.FrameLayout[1]').click(timeout=5)
            u.click(timeline_icon_coordinates[0], timeline_icon_coordinates[1])
            sleep(1)
        u(resourceId="com.yoosee:id/iv_playback_fast_landscape").wait(timeout=5)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast_landscape").info
        sleep(1)
        if play_status['enabled'] == True:
            u(resourceId="com.yoosee:id/play_land_iv").click(timeout=5)
            sleep(1)
        im_1 = u(resourceId="com.yoosee:id/ll_landscape_timeline").screenshot()
        im_1.save("timeline_1.jpg")
        sleep(10)
        im_2 = u(resourceId="com.yoosee:id/ll_landscape_timeline").screenshot()
        im_2.save("timeline_2.jpg")
        im_same = SameOperation().img_statuscheck("timeline_1.jpg","timeline_2.jpg")
        # print (im_same)
        assert im_same == 0.0,'录像暂停时间轴有动'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_69(cls, u, video_camera_name):  #快捷入口--横屏 - 暂停键变成播放键
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/ll_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        sleep(5)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        # 竖屏时时间轴
        timeline_icon_coordinates = u(resourceId='com.yoosee:id/fl_videoplayer_parent').center()
        u(resourceId="com.yoosee:id/iv_half_screen").click(timeout=5)
        if u(resourceId="com.yoosee:id/ll_landscape_timeline").wait_gone(timeout=3.0):
            # u.xpath('//android.widget.FrameLayout[1]').click(timeout=5)
            u.click(timeline_icon_coordinates[0], timeline_icon_coordinates[1])
            sleep(1)
        u(resourceId="com.yoosee:id/iv_playback_fast_landscape").wait(timeout=5)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast_landscape").info
        sleep(1)
        if play_status['enabled'] == True:
            u(resourceId="com.yoosee:id/play_land_iv").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/play_land_iv").click(timeout=5)
        sleep(1)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast_landscape").info
        assert play_status['enabled'] == True, '没有播放'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_70(cls, u, video_camera_name):  #快捷入口--横屏 - 录像暂停，时间轴不动
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/ll_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        sleep(5)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        # 竖屏时时间轴
        timeline_icon_coordinates = u(resourceId='com.yoosee:id/fl_videoplayer_parent').center()
        u(resourceId="com.yoosee:id/iv_half_screen").click(timeout=5)
        if u(resourceId="com.yoosee:id/ll_landscape_timeline").wait_gone(timeout=3.0):
            # u.xpath('//android.widget.FrameLayout[1]').click(timeout=5)
            u.click(timeline_icon_coordinates[0], timeline_icon_coordinates[1])
            sleep(1)
        u(resourceId="com.yoosee:id/iv_playback_fast_landscape").wait(timeout=5)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast_landscape").info
        sleep(1)
        if play_status['enabled'] == True:
            u(resourceId="com.yoosee:id/play_land_iv").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/play_land_iv").click(timeout=5)
        sleep(2)
        im_1 = u(resourceId="com.yoosee:id/ll_landscape_timeline").screenshot()
        im_1.save("timeline_1.jpg")
        sleep(10)
        im_2 = u(resourceId="com.yoosee:id/ll_landscape_timeline").screenshot()
        im_2.save("timeline_2.jpg")
        im_same = SameOperation().img_statuscheck("timeline_1.jpg","timeline_2.jpg")
        # print (im_same)
        assert im_same > 0.0,'录像时间轴有动'
        SameOperation().quit_app(u)


    @classmethod
    def jwt_71(cls, u, video_camera_name):  #快捷入口--竖屏 - 录屏点击录屏后控件上有小红点
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/ll_playback").wait(timeout=5)
        u(resourceId="com.yoosee:id/ll_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        sleep(10)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/iv_playback_to_dwonload").click(timeout=5)
        sleep(2)
        #控件上小红点
        assert u(resourceId='com.yoosee:id/iv_state').wait(timeout=8), '控件没有小红点'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_72(cls, u, video_camera_name):  #快捷入口--竖屏 - 录屏结束后可在我的相册中播放
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            # print ('2')
            if not u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
                u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        SameOperation().photo_delete(u)
        u(resourceId="com.yoosee:id/ll_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        sleep(10)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/iv_playback_to_dwonload").click(timeout=5)
        sleep(10)
        u(resourceId="com.yoosee:id/iv_playback_to_dwonload").click(timeout=5)
        u.press('back')
        u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
        u(resourceId='com.yoosee:id/icon_setting_img').click(timeout=5)
        u(resourceId='com.yoosee:id/rl_album_low').click(timeout=5)
        u(resourceId='com.yoosee:id/iv_play').click(timeout=5)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/viewer"]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]').click(timeout=5)
        sleep(2)
        assert u(resourceId='com.yoosee:id/v_play').wait(timeout=5), '不能播放'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_73(cls, u, video_camera_name):  #快捷入口账户分享显示访客用户的头像，昵称以及有看头账号
        SameOperation().app_go(u)
        # 先判断分享的账号是否已添加分享的设备
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, "gw_test01@sina.com", "abcd1234")
        sleep(3)
        if u(resourceId='com.yoosee:id/ll_device').wait(timeout=5):
            u.press("back")
        SameOperation().find_deldevices(u, '删除设备')
        if u(text='删除设备').wait(timeout=5):
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, phone_num, phone_pwd)

        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        # u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5)
        # u(resourceId='com.yoosee:id/setting_more_iv').click(timeout=5)
        # u(resourceId='com.yoosee:id/pop_share_ll').click(timeout=5)
        # u(resourceId='com.yoosee:id/account_share_tv').click(timeout=5)
        # u(resourceId='com.yoosee:id/tx_save').click(timeout=5)
        # u.xpath("//android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]").set_text("gw_test01@sina.com")
        # u(resourceId='com.yoosee:id/confirm_btn').click(timeout=5)
        # u(resourceId='com.yoosee:id/share_confirm_ll').click(timeout=8)
        # sleep(3)
        SameOperation().account_sharing(u)
        assert u(resourceId='com.yoosee:id/account_tv').get_text() == 'gw_test01@sina.com' and u(resourceId='com.yoosee:id/share_account_tv').get_text() == '有看头账号:025611668','昵称以及有看头账号不正确'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_74(cls, u, video_camera_name):  #快捷入口账户分享提示已发送分享邀请
        SameOperation().app_go(u)
        # 先判断分享的账号是否已添加分享的设备
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, "gw_test01@sina.com", "abcd1234")
        sleep(3)
        if u(resourceId='com.yoosee:id/ll_device').wait(timeout=5):
            u.press("back")
        SameOperation().find_deldevices(u, '删除设备')
        if u(text='删除设备').wait(timeout=5):
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, phone_num, phone_pwd)

        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        # u(resourceId='com.yoosee:id/setting_more_iv').click(timeout=5)
        # u(resourceId='com.yoosee:id/pop_share_ll').click(timeout=5)
        # u(resourceId='com.yoosee:id/account_share_tv').click(timeout=5)
        # u(resourceId='com.yoosee:id/tx_save').click(timeout=5)
        # u.xpath("//android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]").set_text("gw_test01@sina.com")
        # u(resourceId='com.yoosee:id/confirm_btn').click(timeout=5)
        # u(resourceId='com.yoosee:id/share_confirm_ll').click(timeout=8)
        # sleep(3)
        SameOperation().account_sharing(u)
        assert u(text='已发送分享邀请').wait(timeout=5),'没有提示已发送分享邀请'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_75(cls, u, video_camera_name):  #快捷入口账户分享访客账号可在设备列表中看到分享弹窗。
        SameOperation().app_go(u)
        # 先判断分享的账号是否已添加分享的设备
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, "gw_test01@sina.com", "abcd1234")
        sleep(3)
        if u(resourceId='com.yoosee:id/ll_device').wait(timeout=5):
            u.press("back")
        SameOperation().find_deldevices(u, '删除设备')
        if u(text='删除设备').wait(timeout=5):
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, phone_num, phone_pwd)

        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        SameOperation().account_sharing(u)

        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u,"gw_test01@sina.com","abcd1234")
        sleep(3)
        assert u(resourceId='com.yoosee:id/ll_device').wait(timeout=8), '没有收到分享弹窗。'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_76(cls, u, video_camera_name):  #快捷入口账户分享弹框提示“收到xxxx的分享”。
        SameOperation().app_go(u)
        # 先判断分享的账号是否已添加分享的设备
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, "gw_test01@sina.com", "abcd1234")
        sleep(3)
        if u(resourceId='com.yoosee:id/ll_device').wait(timeout=5):
            u.press("back")
        SameOperation().find_deldevices(u, '删除设备')
        if u(text='删除设备').wait(timeout=5):
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, phone_num, phone_pwd)

        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        SameOperation().account_sharing(u)

        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u,"gw_test01@sina.com","abcd1234")
        sleep(3)
        assert '向你分享了一台摄像机' in u(resourceId='com.yoosee:id/content_tv').get_text(), '没有收到好友的分享'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_77(cls, u, video_camera_name):  #快捷入口账户分享分享弹窗点击忽略弹框消失。
        SameOperation().app_go(u)
        # 先判断分享的账号是否已添加分享的设备
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, "gw_test01@sina.com", "abcd1234")
        sleep(3)
        if u(resourceId='com.yoosee:id/ll_device').wait(timeout=5):
            u.press("back")
        SameOperation().find_deldevices(u, '删除设备')
        if u(text='删除设备').wait(timeout=5):
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, phone_num, phone_pwd)

        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        SameOperation().account_sharing(u)

        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u,"gw_test01@sina.com","abcd1234")
        sleep(6)
        u(text='忽略').click(timeout=5)
        assert u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0), '点击忽略弹框未消失'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_78(cls, u, video_camera_name):  #快捷入口账户分享跳转到“添加设备界面”
        SameOperation().app_go(u)
        #先判断分享的账号是否已添加分享的设备
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, "gw_test01@sina.com", "abcd1234")
        sleep(3)
        if u(resourceId='com.yoosee:id/ll_device').wait(timeout=5):
            u.press("back")
        SameOperation().find_deldevices(u,'删除设备')
        if u(text='删除设备').wait(timeout=5):
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u, phone_num, phone_pwd)

        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        SameOperation().account_sharing(u)

        SameOperation().log_out(u)
        sleep(3)
        SameOperation().log_in(u,"gw_test01@sina.com","abcd1234")
        sleep(3)
        u(text='接受').click(timeout=5)
        assert u(text='添加成功').wait(timeout=5), '没有跳转到“添加设备界面”'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_79(cls, u,video_camera_name):  # 设备升级弹框，弹出升级设备的弹框
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        assert u(text='发现新固件').wait(timeout=10),'没有升级设备的弹框'
        u.press("back")
        sleep(6)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_80(cls, u, video_camera_name):  # 设备升级弹框，点击立即更新，升级设备
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        u(text='立即更新').wait(timeout=10)
        u(text='立即更新').click()
        assert u(text='摄像机升级中…').wait(timeout=10), '没有升级中'
        sleep(180)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_81(cls, u, video_camera_name):  # 设备升级弹框，点击后台升级
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        u(text='立即更新').wait(timeout=10)
        u(text='立即更新').click()
        sleep(2)
        u(resourceId='com.yoosee:id/tv_know').click(timeout=5)
        u(resourceId='com.yoosee:id/tv_background').click(timeout=5)
        sleep(1)
        u(resourceId='com.yoosee:id/icon_contact').click(timeout=5)
        sleep(20)
        for offline_1 in range(10):
            u.swipe_ext("down", scale=0.8)
            sleep(6)
            if u(resourceId="com.yoosee:id/tv_offline").wait(timeout=8.0):
                break
        for offline_2 in range(20):
            u.swipe_ext("down", scale=0.8)
            sleep(6)
            if not u(resourceId="com.yoosee:id/tv_offline").exists:
                break
        assert not u(resourceId="com.yoosee:id/tv_offline").exists,'(等了3分钟)设备还是离线'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_82(cls, u, video_camera_name):  # 设备升级弹框，点击弹框右上角“×”
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        u(text='立即更新').wait(timeout=10)
        u(resourceId='com.yoosee:id/iv_close_device_update').click(timeout=5)
        sleep(2)
        assert not u(text="发现新固件").exists, '点击弹框右上角“×”，弹框没消失'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_83(cls, u,video_camera_name):  # 设备列表测到有新的设备固件且设备列表有弹窗提示
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        assert u(text='发现新固件').wait(timeout=10),'设备列表没有升级设备的弹框'
        u.press("back")
        sleep(6)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_84(cls, u, video_camera_name):  # 设备列表可以正常升级设备固件
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        u(text='立即更新').wait(timeout=10)
        u(text='立即更新').click()
        sleep(2)
        u(resourceId='com.yoosee:id/tv_know').click(timeout=5)
        u(resourceId='com.yoosee:id/tv_background').click(timeout=5)
        sleep(1)
        u(resourceId='com.yoosee:id/icon_contact').click(timeout=5)
        sleep(20)
        for offline_1 in range(10):
            u.swipe_ext("down", scale=0.8)
            sleep(6)
            if u(resourceId="com.yoosee:id/tv_offline").wait(timeout=8.0):
                break
        for offline_2 in range(20):
            u.swipe_ext("down", scale=0.8)
            sleep(6)
            if not u(resourceId="com.yoosee:id/tv_offline").exists:
                break
        assert not u(resourceId="com.yoosee:id/tv_offline").exists,'(等了3分钟)设备还是离线'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_85(cls, u, video_camera_name):  #设置-网络设备设置页面，点击“固件更新”弹出弹窗
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        SameOperation().find_deldevices(u, '固件更新')
        u(resourceId='com.yoosee:id/check_device_update').click(timeout=5)
        assert u(text='发现新固件').wait(timeout=6),'没有升级设备的弹框'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_86(cls, u, video_camera_name):  #设置-网络设备设置页面正常升级设备固件
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        SameOperation().find_deldevices(u, '固件更新')
        u(resourceId='com.yoosee:id/check_device_update').click(timeout=5)
        u(text='立即更新').click()
        sleep(2)
        u(resourceId='com.yoosee:id/tv_know').click(timeout=5)
        u(resourceId='com.yoosee:id/tv_background').click(timeout=5)
        sleep(2)
        u.press('back')
        sleep(20)
        for offline_1 in range(10):
            u.swipe_ext("down", scale=0.8)
            sleep(6)
            if u(resourceId="com.yoosee:id/tv_offline").wait(timeout=8.0):
                break
        for offline_2 in range(20):
            u.swipe_ext("down", scale=0.8)
            sleep(6)
            if not u(resourceId="com.yoosee:id/tv_offline").exists:
                break
        assert not u(resourceId="com.yoosee:id/tv_offline").exists, '(等了1分钟)设备还是离线'
        SameOperation().quit_app(u)


    @classmethod
    def jwt_87(cls, u, video_camera_name):  #打开帮助与反馈H5页面
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        u(resourceId="com.yoosee:id/r_online_problem").click(timeout=5)
        assert u(text="帮助中心").wait(timeout=5), '没有打开帮助与反馈H5页面'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_88(cls, u, video_camera_name):  #全屏展示选中的图片
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        for screenshot_i in range(0,3):
            u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_album_low").click(timeout=5)
        u.xpath('//android.widget.GridView/android.widget.RelativeLayout[1]').click(timeout=5)
        assert u(resourceId="com.yoosee:id/iv_delete").wait(timeout=5), '没有全屏展示'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_89(cls, u, video_camera_name):  #左滑动可以查看下一个图片/视频
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        for screenshot_i in range(0,3):
            u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_album_low").click(timeout=5)
        u.xpath('//android.widget.GridView/android.widget.RelativeLayout[1]').click(timeout=5)
        sleep(1)
        u.swipe_ext("left", scale=0.8)
        sleep(2)
        u(resourceId="com.yoosee:id/tv_imagegallay_curprogress").wait(timeout=5)
        assert '2/' in u(resourceId="com.yoosee:id/tv_imagegallay_curprogress").get_text(), '没有切换下一张图片/视频'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_90(cls, u, video_camera_name):  #右滑动可以查看上一个图片/视频
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        for screenshot_i in range(0,3):
            u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_album_low").click(timeout=5)
        u.xpath('//android.widget.GridView/android.widget.RelativeLayout[2]').click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/tv_imagegallay_curprogress").wait(timeout=5)
        u.swipe_ext("right", scale=0.8)
        sleep(2)
        u(resourceId="com.yoosee:id/tv_imagegallay_curprogress").wait(timeout=5)
        assert '1/' in u(resourceId="com.yoosee:id/tv_imagegallay_curprogress").get_text(), '没有切换上一张图片/视频'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_91(cls, u, video_camera_name):  #我的相册单个删除弹出二次确认弹框
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        for screenshot_i in range(0,3):
            u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_album_low").click(timeout=5)
        u.xpath('//android.widget.GridView/android.widget.RelativeLayout[2]').click(timeout=5)
        u(resourceId="com.yoosee:id/iv_delete").click(timeout=5)
        assert u(text="确定删除?").wait(timeout=5), '没有弹出二次确认弹框'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_92(cls, u, video_camera_name):  #我的相册单个删除弹出二次确认弹框，点击否
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        for screenshot_i in range(0,3):
            u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_album_low").click(timeout=5)
        u.xpath('//android.widget.GridView/android.widget.RelativeLayout[2]').click(timeout=5)
        u(resourceId="com.yoosee:id/iv_delete").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_no").click(timeout=5)
        assert not u(text="确定删除?").exists, '点击否二次确认弹框消失'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_93(cls, u, video_camera_name):  # 我的相册单个删除弹出二次确认弹框，点击是
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        for screenshot_i in range(0, 3):
            u(resourceId="com.yoosee:id/iv_p_screenshot").click(timeout=5)
            sleep(1)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        sleep(1)
        u(resourceId="com.yoosee:id/icon_setting").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_album_low").click(timeout=5)
        u.xpath('//android.widget.GridView/android.widget.RelativeLayout[2]').click(timeout=5)
        sleep(2)
        total_img_1 = u(resourceId="com.yoosee:id/tv_imagegallay_curprogress").get_text().strip().split('/')

        u(resourceId="com.yoosee:id/iv_delete").click(timeout=5)
        u(resourceId="com.yoosee:id/tv_yes").click(timeout=5)
        sleep(2)
        total_img_2 = u(resourceId="com.yoosee:id/tv_imagegallay_curprogress").get_text().strip().split('/')
        assert int(total_img_1[1]) > int(total_img_2[1]),'没有删除成功'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_94(cls, u, video_camera_name):  # 设置图像翻转
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        # SameOperation().find_deldevices(u,'画面与声音')
        u.xpath(
            '//*[@resource-id="com.yoosee:id/lv_contact"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click(
            timeout=5)
        sleep(3)
        u(resourceId='com.yoosee:id/bottom_control_rl').wait_gone(timeout=5.0)
        u.screenshot('image_flipping_1.png')
        u(resourceId="com.yoosee:id/iv_set").click(timeout=5)
        u(resourceId="com.yoosee:id/video_control").click(timeout=5)
        u(resourceId="com.yoosee:id/sv_reverse_img").click(timeout=5)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId='com.yoosee:id/center_direction_view').wait(timeout=5)
        u.screenshot('image_flipping_2.png')
        fl = SameOperation().img_statuscheck('image_flipping_1.png','image_flipping_2.png')
        print (fl)
        assert fl >500,'图像没翻转'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_95(cls, u, video_camera_name):  # 触发报警，验证在线报警弹窗页面
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        if u(text="不报警").exists:
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
            sleep(3)
        alarm = 0
        if u(resourceId='com.yoosee:id/alarming').wait(timeout=10):
            u(resourceId="com.yoosee:id/iv_alarm_close").click(timeout=5)
            alarm = 1
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        else:
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        sleep(3)
        if alarm == 0:
            assert 1 == 0,'没有报警弹框页面'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_96(cls, u, video_camera_name):  # 在线接收的报警消息在智能守护本地消息中有记录
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        u(resourceId="com.yoosee:id/icon_keyboard").click(timeout=5)
        if u(resourceId='com.yoosee:id/item_ll').wait(timeout=5):
            u(resourceId="com.yoosee:id/item_ll").long_click()
            u(resourceId="com.yoosee:id/tv_select").click(timeout=5)
            sleep(2)
            if len(u(resourceId="com.yoosee:id/img_choose")) > 1:
                u(resourceId="com.yoosee:id/cl_select_all").click(timeout=5)
            u(resourceId="com.yoosee:id/cl_delete").click(timeout=5)
            u.xpath('//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]').click()
            u(resourceId="com.yoosee:id/iv_close").click(timeout=5)
        sleep(190)
        u(resourceId="com.yoosee:id/icon_contact").click(timeout=5)
        # if u(text="不报警").exists:
        #     u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        #     sleep(3)
        # if u(resourceId='com.yoosee:id/alarming').wait(timeout=10):
        #     u(resourceId="com.yoosee:id/iv_alarm_close").click(timeout=5)
        #     u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        # else:
        #     u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        # sleep(3)

        u(resourceId="com.yoosee:id/icon_keyboard").click(timeout=5)
        assert u(resourceId='com.yoosee:id/item_ll').wait(timeout=5),'在智能守护本地消息中没有记录'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_97(cls, u, video_camera_name):  # 报警推送弹窗忽略本次返回原页面
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        if u(text="不报警").exists:
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
            sleep(3)
        u(resourceId='com.yoosee:id/alarming').wait(timeout=10)
        u(resourceId="com.yoosee:id/iv_alarm_close").click(timeout=5)
        u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        sleep(2)
        assert u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5),'忽略本次返回原页面'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_98(cls, u, video_camera_name):  # 报警推送弹窗测试出现弹窗页面
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        if u(text="不报警").exists:
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
            sleep(3)
        alarm = 0
        if u(resourceId='com.yoosee:id/alarming').wait(timeout=10):
            u(resourceId="com.yoosee:id/iv_alarm_close").click(timeout=5)
            alarm = 1
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        else:
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        sleep(3)
        if alarm == 0:
            assert 1 == 0, '没有报警推送弹窗测试出现弹窗页面'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_99(cls, u, video_camera_name):  # 报警推送弹窗进入到设备监控页面
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        if u(text="不报警").exists:
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
            sleep(3)
        u(resourceId='com.yoosee:id/alarming').wait(timeout=10)
        u(resourceId="com.yoosee:id/iv_alarm_check").click(timeout=5)
        assert u(resourceId='com.yoosee:id/bottom_control_rl').wait(timeout=5),'没有进入设备监控页面'
        u(resourceId="com.yoosee:id/back_btn").click(timeout=5)
        u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        SameOperation().quit_app(u)

    @classmethod
    def jwt_100(cls, u, video_camera_name):  # 报警快捷键收到在线报警推送
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        sleep(2)
        if u(text="不报警").exists:
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
            sleep(3)
        alarm = 0
        if u(resourceId='com.yoosee:id/alarming').wait(timeout=10):
            u(resourceId="com.yoosee:id/iv_alarm_close").click(timeout=5)
            alarm = 1
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        else:
            u(resourceId="com.yoosee:id/ll_defence_state").click(timeout=5)
        sleep(3)
        if alarm == 0:
            assert 1 == 0, '没有收到在线报警推送'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_101(cls, u, video_camera_name):  # 设备主人点击智能气泡消息跳到智能守护页
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        sleep(5)
        u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        u(text="推送消息提醒").wait(timeout=10)
        try:
            u(text="消息通知说明").wait(timeout=10)
        except:
            u(resourceId="com.yoosee:id/iv_back").click(timeout=5)
        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        #sleep(190)
        u.swipe_ext("down", scale=0.8)
        sleep(2)
        u(resourceId="com.yoosee:id/msgLayout").wait(timeout=5)
        u(resourceId="com.yoosee:id/msgLayout").click(timeout=5)

        assert u(resourceId='com.yoosee:id/view_img_video').wait(timeout=5),'没有跳到智能守护页'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_102(cls, u, video_camera_name):  # 跳到智能守护页,关闭卡片显示
        u.app_clear('com.yoosee')  # 清除应用数据
        SameOperation().app_go(u)
        SameOperation().log_in(u, phone_num, phone_pwd)
        sleep(5)
        u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        u(text="推送消息提醒").wait(timeout=10)
        try:
            u(text="消息通知说明").wait(timeout=10)
        except:
            u(resourceId="com.yoosee:id/iv_back").click(timeout=5)

        if u(resourceId='com.yoosee:id/setting_more_iv').wait(timeout=5):
            pass
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press('back')
        if u(resourceId="com.yoosee:id/ll_defence_state").wait_gone(timeout=3.0):
            u.swipe_ext("down", scale=0.8)
        #sleep(190)
        u.swipe_ext("down", scale=0.8)
        sleep(2)
        u(resourceId="com.yoosee:id/msgLayout").wait(timeout=5)
        u(resourceId="com.yoosee:id/msgLayout").click(timeout=5)

        u(resourceId='com.yoosee:id/view_img_video').wait(timeout=5)
        u(resourceId='com.yoosee:id/icon_contact').click(timeout=5)
        assert not u(resourceId="com.yoosee:id/msgLayout").wait(timeout=5), '仍存在卡片消息'
        SameOperation().quit_app(u)
