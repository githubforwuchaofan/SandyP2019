# -*- coding:utf-8 -*-
import os
from logging.handlers import RotatingFileHandler
import logging
import threading
import configparser

import time


class LogHandler(object):

    def __new__(cls, log_config):
        mutex = threading.Lock()
        mutex.acquire()  # 上锁，防止多线程下出问题
        if not hasattr(cls, 'instance'):
            cls.instance = super(LogHandler, cls).__new__(cls)
            time_str = time.strftime('%Y%m%d%H%M%S', time.localtime())
            config = configparser.ConfigParser()
            config.read(log_config, encoding='utf-8')
            # 组合log文件目录
            cls.instance.log_path = config.get('LOGGING', "log_path")
            if not os.path.exists(cls.instance.log_path):
                os.mkdir(cls.instance.log_path)
            cls.instance.log_filename = os.path.join(cls.instance.log_path, time_str + ".log")
            cls.instance.max_bytes_each = config.getint('LOGGING', 'max_bytes_each')
            cls.instance.backup_count = config.getint('LOGGING', 'backup_count')
            cls.instance.fmt = config.get('LOGGING', 'fmt')
            cls.instance.log_level_in_console = config.getint('LOGGING', 'log_level_in_console')
            cls.instance.log_level_in_logfile = config.getint('LOGGING', 'log_level_in_logfile')
            cls.instance.logger_name = config.get('LOGGING', 'logger_name')
            cls.instance.console_log_on = config.getint('LOGGING', 'console_log_on')
            cls.instance.logfile_log_on = config.getint('LOGGING', 'logfile_log_on')
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release()
        return cls.instance

    def get_logger(self):
        return self.logger

    def __config_logger(self):
        # 设置日志格式
        fmt = self.fmt.replace('|', '%')
        formatter = logging.Formatter(fmt)

        if self.console_log_on == 1:  # 如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.setLevel(self.log_level_in_console)

        if self.logfile_log_on == 1:  # 如果开启文件日志
            rt_file_handler = RotatingFileHandler(
                filename=self.log_filename,
                maxBytes=self.max_bytes_each,
                backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)
            self.logger.setLevel(self.log_level_in_logfile)


log_sign = LogHandler('./Properties/logconfig')
logger = log_sign.get_logger()
