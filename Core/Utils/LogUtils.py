# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午1:50
_desc: //LogUtils类
"""

import logging

import logging.config



class LogUtils(object):
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)s %(name)s: %(message)s',
            # filemode='a',
            # filename='ApiRobotTest.log'
        )
        self.handler = logging.StreamHandler()
        self.logger = logging.getLogger(__name__)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def exception(self, msg):
        self.logger.exception(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    logUtil = LogUtils()
    try:
        int('aa')
    except Exception as err:
        logUtil.exception(err)
