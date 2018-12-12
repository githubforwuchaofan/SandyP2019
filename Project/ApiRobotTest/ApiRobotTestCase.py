# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午6:46
_desc: //ToDo
"""

from ddt import ddt, file_data
import allure

@allure.MASTER_HELPER.feature('接口验证')
@ddt
class ApiRobotTestCase(object):

    @file_data('./')
    def test_by_json_file(self, parameters, validators):
        # response = '' ToDo 获取response方法实现

        for validator in validators:
            allure.MASTER_HELPER.attach(parameters, validators)
            # check_response()   ToDo 验证response方法实现

