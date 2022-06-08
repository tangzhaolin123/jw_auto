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
                break
            else:
                sleep(3)
                gotimes += 1
            if gotimes == 4:
                break
        if u(resourceId="com.yoosee:id/msgLayout").exists:
            sleep(2)
        sleep(1)
    def quit_app(self,u):
        for quit_n in range(2):
            sleep(1)
            u.press("back")
            sleep(1)
            if u(resourceId="com.yoosee:id/icon_contact_img").exists:
                u(resourceId="com.yoosee:id/icon_contact_img").click(timeout=5)
                break
            else:
                u.press("back")
                u.press("back")
        u.app_stop('com.yoosee')

    def add_wired(self,u,video_camera_name):
        # screen = u.window_size()
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
        u(resourceId="com.yoosee:id/setting_more_iv").click(timeout=5)
        sleep(2)
        u(resourceId="com.yoosee:id/pop_set_ll").click(timeout=5)
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
        u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_sdcard_playback").click(timeout=5)
        u(resourceId='com.yoosee:id/fl_videoplayer_parent').wait(timeout=5)
        timeline_icon_coordinates = u(resourceId='com.yoosee:id/fl_videoplayer_parent').center()
        u.drag(timeline_icon_coordinates[0] - 100, timeline_icon_coordinates[1], timeline_icon_coordinates[0],
               timeline_icon_coordinates[1], 0.2)
        sleep(5)
        u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        sleep(1)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        sleep(3)
        play_status = u(resourceId="com.yoosee:id/iv_playback_fast").info
        assert play_status['enabled'] == True, '时间轴向前快速滑动没有自动播放'
        u.drag(timeline_icon_coordinates[0] + 100, timeline_icon_coordinates[1], timeline_icon_coordinates[0],
               timeline_icon_coordinates[1], 0.2)
        sleep(5)
        if not u(resourceId="com.yoosee:id/iv_playback_fast").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
            sleep(1)
        sleep(3)
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
        u.swipe_ext("down", scale=0.8)
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
        u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if not u(resourceId="com.yoosee:id/rl_functin_bar").exists:
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
        u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if not u(resourceId="com.yoosee:id/rl_functin_bar").exists:
            u(resourceId="com.yoosee:id/rl_vedioplayer_area").click(timeout=5)
        u(resourceId="com.yoosee:id/play_iv").click(timeout=5)
        sleep(1)
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
        u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if not u(resourceId="com.yoosee:id/rl_functin_bar").exists:
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
        u.swipe_ext("down", scale=0.8)
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
        if not u(resourceId="com.yoosee:id/rl_functin_bar").exists:
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
        u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        u(resourceId='com.yoosee:id/date_tv')[2].click(timeout=5)
        sleep(10)
        if not u(text="暂无录像").exists:
            if not u(resourceId="com.yoosee:id/rl_functin_bar").exists:
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
        u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
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
        u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if not u(resourceId="com.yoosee:id/rl_functin_bar").exists:
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
        u.swipe_ext("down", scale=0.8)
        u(resourceId="com.yoosee:id/tv_playback").click(timeout=8)
        u(resourceId="com.yoosee:id/tv_cloud_playback").click(timeout=5)
        u(resourceId="com.yoosee:id/rl_functin_bar").wait(timeout=8)
        sleep(10)
        if not u(resourceId="com.yoosee:id/rl_functin_bar").exists:
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