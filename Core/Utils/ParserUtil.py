# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午4:18
_desc: //ToDo
"""

from requests.structures import CaseInsensitiveDict

from Core.Utils.LogUtils import LogUtils
from Core.sExceptions.DictExceptions import DictIsEmptyError, KeyNotFoundError, JsonFormatError


logUtils = LogUtils()

class ParserIniUtil(object):
    def __init__(self):
        pass

    def get_option(self, section, option):
        pass

    def get_options(self, section, options):
        pass

    def set_option(self):
        pass

    def get_all_sections(self):
        pass


class ParserYamlUtil(object):
    pass


class ParserJsonUtil(object):
    @classmethod
    def query_json(cls, query, json_content, delimiter='.'):
        logUtils.info('query={0}\ncontent={1}'.format(query, json_content))

        if not json_content:
            DictIsEmptyError("response content is empty!")

        try:
            for key in query.split(delimiter):
                if isinstance(json_content, list):
                    json_content = json_content[int(key)]
                elif isinstance(json_content, (dict, CaseInsensitiveDict)):
                    json_content = json_content[key]
                else:
                    KeyNotFoundError("Query Json失败，key={0}, {0}不存在！\nJson Content={1}!".format(key, json_content))

        except Exception as err:
            JsonFormatError(err)

        return json_content


if __name__ == '__main__':
    response = {"responseData": 12, "data": 11}
    ParserJsonUtil.query_json('responseData.data', response)





