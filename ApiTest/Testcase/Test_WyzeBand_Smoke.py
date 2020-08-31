#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/8/31 16:18
# @Author : Greey
# @FileName: Test_WyzeBand_Smoke.py



'''
测试步骤：
1：登录app（https://test-api.wyzecam.com/app/user/login）
2：生成手环token（https://test-wristband-service.wyzecam.com/app/v2/wristband/generate_token）
3：绑定手环（https://test-wristband-service.wyzecam.com/app/v2/wristband/bind_device）
4：设置默认连接的key（https://test-wristband-service.wyzecam.com/app/v2/wristband/set_defaultconn）
5：获取设备对应的默认自动连接设置（https://test-wristband-service.wyzecam.com/app/v2/wristband/get_defaultconn）
6：获取版本对应的功能列表（不包括基础功能）（https://test-wristband-service.wyzecam.com/app/v2/wristband/get_functions）
7：上传数据（https://test-wristband-service.wyzecam.com/app/v2/wristband/data_upload）
8：


预期结果：
1：登录app成功
2：成功生成token
3：绑定手环成功
4：设置默认连接的key成功
5：获取设备对应的默认自动连接设置成功
6：获取版本对应的功能列表成功
7：上传数据
'''


import pytest
import os
import sys
import allure
from ApiTest.Common.Config import ReadConfig
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Request import Request
from ApiTest.Common.Log import MyLog
from ApiTest.Common.Assert import Assertions
from ApiTest.Common.Session import Session
from ApiTest.Common.Module import Moudle




@allure.feature('解除绑定手环')
@allure.description('验证不同场景解除绑定手环')
class TestClass:
    def setup(self):
        print("Test Start")
        self.log = MyLog()
        self.env2 = "Wristband_Alpha"
        self.moudle = Moudle(self.env2)
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        print("Test End")

    @allure.story("wyzeband smoke test")
    @allure.severity('blocker')
    def test_wyzeband_smoke(self):
        self.moudle.get_token()                                 #获取设备Token
        self.moudle.user_info()                                 #获取用户信息
        Returndata = self.moudle.bind_device()                  #生成设备token
        self.parm['device_token'] = Returndata[0]             #返回device_token
        self.moudle.set_defaultconn()                           #设置默认连接的key
        self.moudle.get_defaultconn()                           #获取设备对应的默认自动连接设置
        self.moudle.get_functions()                             #获取版本对应的功能列表（不包括基础功能）
        self.moudle.data_upload()                               #上传数据


if __name__ == '__main__':
     pytest.main()