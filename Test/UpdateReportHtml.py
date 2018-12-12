# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午9:15
_desc: //ToDo
"""

import re

pattern = re.compile(r'<div class="empty log">No log output captured.</div>')


def update_report_html(report='./report/report.html'):
    print(pattern.findall(open(report).read()))

    logs = pattern.sub('AAAAA', open(report).read())
    # print(logs)


update_report_html()

