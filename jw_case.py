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
        screen = u.window_size()
        u(resourceId="com.yoosee:id/button_add").click(timeout=5)
        sleep(2)
        u(resourceId='com.yoosee:id/line_add').click(timeout=5)
        u(resourceId="com.yoosee:id/config_cb").click(timeout=5)
        u(text='下一步').click(timeout=5)
        for wt in range(0, 12):
            try:
                u.drag(screen[0] / 2, screen[1] / 3, screen[0] / 2, (screen[1] - 600), 0.2)
                sleep(8)
            except:
                pass
            if u(text=video_camera_name).exists:
                u(text=video_camera_name).click(timeout=5)
                sleep(5)
                if u(text='正在添加摄像机').exists:
                    u.press("back")
                    u(text='退出').click(timeout=5)
                else:
                    break
        sleep(2)
        u(resourceId='com.yoosee:id/et_name').set_text("有线连接自动化测试")
        u.press("back")
        u(text='确定').click(timeout=5)
        sleep(2)
    def find_deldevices(self,u,set_name):
        screen = u.window_size()
        u(resourceId="com.yoosee:id/setting_more_iv").click(timeout=5)
        sleep(2)
        u(resourceId="com.yoosee:id/pop_set_ll").click(timeout=5)
        for del_i in range(0, 5):
            if u(text= set_name).exists:
                break
            else:
                try:
                    u.drag(screen[0] / 2, (screen[1] - 600), screen[0] / 2, screen[1] / 3, 0.3)
                    sleep(3)
                except:
                    pass
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
            SameOperation().log_in(u, "17722618662", "@tang123")
            sleep(5)
            u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        else:
            SameOperation().log_out(u)
            SameOperation().log_in(u, "17722618662", "@tang123")
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
        sleep(3)
        assert not u(resourceId='com.yoosee:id/setting_more_iv').exists, "要删除的设备存在"


    @classmethod
    def jwt_14(cls, u, video_camera_name):  #支持云存设备弹窗-到购买云存储界面“点击“购买云存储”
        SameOperation().app_go(u)
        if u(text="有线连接自动化测试", resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
        sleep(3)
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
        sleep(3)
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
        sleep(3)
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
    def jwt_18(cls, u, video_camera_name):  #云存储设置入口
        SameOperation().app_go(u)
        set_name = '增值服务'
        if u(text="有线连接自动化测试", resourceId="com.yoosee:id/tv_name").exists or u(text=video_camera_name,resourceId="com.yoosee:id/tv_name").exists:
            SameOperation().find_deldevices(u,set_name)
            assert u(resourceId="com.yoosee:id/tx_vas").get_text() == '未购买', '显示状态错误'
        else:
            SameOperation().add_wired(u, video_camera_name)
            u.press("back")
            SameOperation().find_deldevices(u, set_name)
            assert u(resourceId="com.yoosee:id/tx_vas").get_text() == '未购买', '显示状态错误'
        SameOperation().quit_app(u)

    @classmethod
    def jwt_19(cls, u, video_camera_name):  #设备列表有“新手教程
        SameOperation().app_go(u)
        if u(resourceId='com.yoosee:id/setting_more_iv').exists:
            SameOperation().find_deldevices(u,'删除设备')
            u(text='删除设备').click(timeout=5)
            u(resourceId='com.yoosee:id/tv_yes').click(timeout=5)
            sleep(2)
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
            sleep(2)
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
        # u.watcher.stop()
        SameOperation().app_go(u)
        SameOperation().log_in(u, "17722618662", "@tang123")
        sleep(5)
        u(resourceId='com.yoosee:id/tv_contact').click(timeout=5)
        u(text="推送消息提醒").wait(timeout=10)
        sleep(3)

        u.app_stop('com.yoosee')
        u.app_start('com.yoosee')
        SameOperation().app_go(u)
