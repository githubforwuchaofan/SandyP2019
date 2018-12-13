# coding=utf8

"""
_author: wcf
_date: 2018/12/12-下午12:53
_desc: //ToDo
"""
from Core.Utils.LogUtils import LogUtils
from Core.Utils.RegexUtil import RegexUtil

logUtils = LogUtils()


class ComparatorUtil(object):
    def __init__(self, _check_item, _symbol=None, _excepted=None, _text=None):
        self._check_item = _check_item
        self._symbol = _symbol
        self._excepted = _excepted
        self._text = _text

        logUtils.debug('check_item = {0}\n\tsymbol = {1}\n\texcepted = {2}'.format(self._check_item, self._symbol, self._excepted))

        self._SYMBOL_MAP = {
            "正则匹配有结果": ['regex', 're', 'match'],
            "为空": ['null', 'None', 'is null', 'False', 'false'],
            "不为空": ['not null', 'not None', 'True', 'true'],
            "不等于": ['!=', 'not equal'],
            "长度不等于": ['len !=', 'len not equal'],
            "字符串不等于": ['str !=', 'str not equal'],
            "类型不等于": ['type !=', 'type not equal'],
            "等于": ['=', 'equal'],
            "类型等于": ['type ='],
            "字符串等于": ['str ='],
            "长度等于": ['len ='],
            "开始于": ['starts'],
            "结束于": ['ends'],
            "包含": ['contains'],
            "被包含": ['in'],
            "类型包含": ['type contains'],
            "类型被包含": ['type in'],
            "大于": ['gt', '>'],
            "字符串大于": ['str >', 'str gt'],
            "不小于": ['nlt', '>='],
            "小于": ['lt', '<'],
            "字符串小于": ['str <', 'str lt'],
            "不大于": ['ngt', '<='],
            "长度大于": ['len gt', 'len >'],
            "长度不小于": ['len nlt', 'len >='],
            "长度小于": ['len lt', 'len <'],
            "长度不大于": ['len ngt', 'len <='],
        }
        # 去掉map中比较符带有的去掉
        self._SYMBOL_MAP = {key: [symbol.replace(' ', '') for symbol in symbols] for key, symbols in self._SYMBOL_MAP.items()}

    def check(self):
        try:
            # 要检查的内容为空
            if not self._check_item:
                raise ValueError  # ToDo 自定义错误类型

            # 比较器为空，验证要检查的内容是否为真
            if not self._symbol:
                assert self._check_item

            # 去掉比较符带有的空格
            self._symbol = self._symbol.replace(' ', '')

            if self._symbol in self._SYMBOL_MAP.get("正则匹配有结果"):
                assert RegexUtil(_pattern=self._check_item, _text=str(self._text)).match()

            elif self._symbol in self._SYMBOL_MAP.get("为空"):
                assert not self._check_item

            elif self._symbol in self._SYMBOL_MAP.get("不为空"):
                assert self._check_item

            elif self._symbol in self._SYMBOL_MAP.get("不等于"):
                assert self._check_item != self._excepted

            elif self._symbol in self._SYMBOL_MAP.get("类型不等于"):
                assert type(self._check_item).__name__ != str(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("字符串不等于"):
                assert str(self._check_item) != str(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("长度不等于"):
                assert len(self._check_item) != int(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("等于"):
                assert self._check_item == self._excepted

            elif self._symbol in self._SYMBOL_MAP.get("类型等于"):
                assert type(self._check_item).__name__ == str(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("字符串等于"):
                assert str(self._check_item) == str(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("长度等于"):
                assert len(self._check_item) == int(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("开始于"):
                assert str(self._check_item).startswith(str(self._excepted))

            elif self._symbol in self._SYMBOL_MAP.get("结束于"):
                assert str(self._check_item).endswith(str(self._excepted))

            elif self._symbol in self._SYMBOL_MAP.get("包含"):
                assert self._excepted in self._check_item

            elif self._symbol in self._SYMBOL_MAP.get("被包含"):
                assert self._check_item in self._excepted

            elif self._symbol in self._SYMBOL_MAP.get("类型被包含"):
                assert type(self._check_item).__name__ in self._excepted

            elif self._symbol in self._SYMBOL_MAP.get("大于"):
                assert self._check_item > self._excepted

            elif self._symbol in self._SYMBOL_MAP.get("字符串大于"):
                assert str(self._check_item) > str(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("长度大于"):
                assert len(self._check_item) > int(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("不大于"):
                assert self._check_item <= self._excepted

            elif self._symbol in self._SYMBOL_MAP.get("长度不大于"):
                assert len(self._check_item) <= int(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("小于"):
                assert self._check_item < self._excepted

            elif self._symbol in self._SYMBOL_MAP.get("字符串小于"):
                assert str(self._check_item) < str(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("长度小于"):
                assert len(self._check_item) < int(self._excepted)

            elif self._symbol in self._SYMBOL_MAP.get("不小于"):
                assert self._check_item <= self._excepted

            elif self._symbol in self._SYMBOL_MAP.get("长度不小于"):
                assert len(self._check_item) == int(self._excepted)

            else:
                logUtils.error("比较符不存在：symbol = {0}".format(self._symbol))

        except AssertionError:
            logUtils.error(
                msg="比较器验证失败：\n"
                    "\t比较值(check_item)：{0}({1})\n"
                    "\t比较符号(symbol)：{2}\n"
                    "\t期望值(excepted)：{3}({4}）".format(
                self._check_item, type(self._check_item),
                self._symbol,
                self._excepted, type(self._excepted)))

        except Exception as err:
            logUtils.exception(err)


if __name__ == '__main__':
    ComparatorUtil('999', _symbol='str !=', _excepted=999).check()
