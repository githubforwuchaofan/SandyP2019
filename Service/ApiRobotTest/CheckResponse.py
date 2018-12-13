# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午5:51
_desc: //ToDo
"""

import re

from Core.Utils.ComparatorUtil import ComparatorUtil
from Core.Utils.HttpUtils import HttpUtils
from Core.Utils.LogUtils import LogUtils
from Core.Utils.ParserUtil import ParserJsonUtil

text_extractor_regexp_compile = re.compile(r".*\(.*\).*")

logUtils = LogUtils()


class CheckResponse(object):

    def __init__(self, resp_obj):
        self.resp_obj = resp_obj
        self.resp_text = resp_obj.text
        self.resp_body = self.parsed_body()

    def parsed_body(self):
        try:
            return self.resp_obj.json()
        except ValueError:
            return self.resp_text

    def parsed_dict(self):
        return {
            'status_code': self.resp_obj.status_code,
            'headers': self.resp_obj.headers,
            'body': self.resp_body
        }

    def validate(self, validators):
        """
        验证response
        :param validators: type：list  format:{"symbol": "not", "value": "responseData.feed", "excepted": False}
        :return:
        """
        for validator in validators:
            route = validator.get("value")

            logUtils.info("根据路径校验")
            check_item = ParserJsonUtil.query_json(route, self.resp_body.replace('\n', ''))

            ComparatorUtil(
                _check_item=check_item,
                _symbol=validator.get('symbol'),
                _excepted=validator.get('excepted')
            ).check()


if __name__ == "__main__":
    req = HttpUtils.send('http://gongyu.qunar.com')
    CheckResponse(req).validate([{"symbol": ">", "expected": 100, "value": ''}])



