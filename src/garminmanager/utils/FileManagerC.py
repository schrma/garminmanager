import logging
import os
import shutil

_logger = logging.getLogger(__name__)


class FilemManagerC:

    def __init__(self, loglevel=logging.INFO):
        self._src = []
        self._dst = []
        self._file_list = []
        self._with_subfolder = True
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))

    def set_src_folder(self, foldername):
        self._src = foldername

    def set_dst_folder(self, foldername):
        self._dst = foldername

    def move(self):
        self._move_or_copy('move')

    def copy(self):
        self._move_or_copy('copy')

    # noinspection PyTypeChecker
    def _move_or_copy(self, operation='copy'):
        root_src_dir = self._src
        root_target_dir = self._dst
        self._file_list = []
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_target_dir)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                self._file_list.append(dst_file.replace("\\", "/"))
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                if operation is 'copy':
                    shutil.copy(src_file, dst_dir)
                else:
                    shutil.move(src_file, dst_dir)

    def folder_are_ok(self):
        if self._src == [] or self._dst == []:
            return False
        else:
            return True

    @staticmethod
    def create_folder(name):
        if not os.path.exists(name):
            os.makedirs(name)

    def get_file_list(self):
        return self._file_list

    def print_file_list(self):
        for item in self._file_list:
            print(item)
