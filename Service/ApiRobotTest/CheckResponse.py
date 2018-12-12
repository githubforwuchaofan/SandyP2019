# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午5:51
_desc: //ToDo
"""

import re
text_extractor_regexp_compile = re.compile(r".*\(.*\).*")


class ResponseObject(object):

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
        :param validators: type：list  format:{"comparator": "not", "route": "responseData.feed", "excepted": False}
        :return:
        """
        for validator in validators:
            pass

        return True


