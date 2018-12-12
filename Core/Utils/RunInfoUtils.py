# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午3:47
_desc: //获取代码运行中信息
"""


import inspect

class InspectIUtil(object):
    @classmethod
    def get_cur_func(cls):
        return inspect.stack()[1][3]

    @classmethod
    def get_cur_class(cls):
        return inspect.stack()[1][1]

    @classmethod
    def get_cur_detail_info(cls):
        return inspect.stack()[1]


if __name__ == '__main__':
    inspectUtil = InspectIUtil()
    class Demo(object):
        @classmethod
        def test(cls):
            print(inspectUtil.get_cur_class())
            print(inspectUtil.get_cur_func())
            print(inspectUtil.get_cur_detail_info())

    Demo().test()

