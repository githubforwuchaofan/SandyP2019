# coding=utf8

"""
_author: wcf
_date: 2018/12/11-下午4:42
_desc: //ToDo
"""

import os


class PathUtil(object):

    @staticmethod
    def mkdir(_dir):
        if not os.path.exists(_dir):
            os.mkdir(_dir)

    # def touch(self, file_path):
    #     open(file_path)

    @classmethod
    def deep_mkdir(cls, _dir):
        if not os.path.isdir(_dir):
            cls.deep_mkdir(os.path.split(_dir)[0])
        else:
            return
        cls.mkdir(_dir)


    @staticmethod
    def join_paths(*paths):
        return os.path.join(*paths)

    @staticmethod
    def is_path_exist(_path):
        return os.path.exists(_path)

    @staticmethod
    def is_dir(_dir):
        return os.path.isdir(_dir)

    def load_folder_files(self, folder_path, suffix=('.yml', '.yaml', '.json', 'py'), recursive=True):
        if isinstance(folder_path, (list, set)):
            _files = []
            for path in set(folder_path):
                _files.extend(self.load_folder_files(path, recursive))

            return _files

        if not os.path.exists(folder_path):
            return []

        _file_list = []

        for dir_path, dir_names, file_names in os.walk(folder_path):
            file_names_list = []

            for filename in file_names:
                if not filename.endswith(suffix):
                    continue

                file_names_list.append(filename)

            for filename in file_names_list:
                file_path = os.path.join(dir_path, filename)
                _file_list.append(file_path)

            if not recursive:
                break

        return _file_list


if __name__ == '__main__':
    f = PathUtil().load_folder_files('/Users/wuchaofan/PycharmProjects/from_github/sandy2019/Core')
    __dir = './2018/12/12/app.log'
    PathUtil().deep_mkdir(__dir)


