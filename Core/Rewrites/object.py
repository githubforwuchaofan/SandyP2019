# coding=utf8

"""
_author: wcf
_date: 2018/12/13-上午11:23
_desc: //ToDo
"""
from Core.Utils.LogUtils import LogUtils


class MyObject(object):

    def __init__(self):
        self.logUtils = LogUtils()


if __name__ == '__main__':
    class Demo(MyObject):

        def __init__(self, inf):
            super().__init__()
            self.inf = inf

        def test(self):
            """
            :return:
            """
            self.logUtils.info(Demo.__name__)
            self.logUtils.info(self.__name__)

    class DemoSub(Demo):
        def __init__(self, inf):
            super().__init__(inf=inf)





