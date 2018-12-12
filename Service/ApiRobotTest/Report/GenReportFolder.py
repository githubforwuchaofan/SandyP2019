# coding=utf8

"""
_author: wcf
_date: 2018/12/12-上午11:30
_desc: //ToDo
"""
import datetime
import time

from Core.Utils.PathUtil import PathUtil

class GenReport(object):
    def __init__(self, project_name, file_name=None, abs_report_path='./'):
        self.project_name = project_name
        self.file_name = file_name
        self.abs_report_path = abs_report_path

    def gen_report_folder(self):
        now = datetime.date.today()
        year_month = '{0}{1}'.format(now.year, now.month)
        day = str(now.day)
        folder_path = PathUtil.join_paths(self.abs_report_path, self.project_name, year_month, day)
        PathUtil.deep_mkdir(folder_path)
        return folder_path

    def gen_report(self, mode='w'):
        if not self.file_name:
            self.file_name = 'report_{}.log'.format(int(time.time()))

        return open(PathUtil.join_paths(self.gen_report_folder(), self.file_name), mode=mode)


if __name__ == '__main__':
    GenReport('ApiRobotTest').gen_report()

