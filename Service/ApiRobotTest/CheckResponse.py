# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午5:51
_desc: //ToDo
"""

import re
from Core.sExceptions.HttpExceptions import HttpParameterError

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

    def validate(self, validators, variables_mapping):
        for validator_dict in validators:

            check_item = validator_dict.get("check")
            if not check_item:
                HttpParameterError("invalid check item in testcase validators!")

            if "expected" not in validator_dict:
                raise HttpParameterError("expected item missed in testcase validators!")

            expected = validator_dict.get("expected")
            comparator = validator_dict.get("comparator", "eq")

            if check_item in variables_mapping:
                validator_dict["actual_value"] = variables_mapping[check_item]
            else:
                pass

        return True


