import logging
import os
import shutil

_logger = logging.getLogger(__name__)


class FilemManagerC:
    """A Class to manage files

    The classe handles differnt **file** operations

    - **BulletpointBold1**, BulletpointNormal1

      which appears as follow:

    - **BulletpointBold1**, BulletpointNormal1

    .. note::
        Some notes
            * Some bulletpoints
            * Another bulletpoint
    .. note::
        Another note

    """

    def __init__(self, loglevel=logging.INFO):
        self._src = []
        self._dst = []
        self._file_list = []
        self._with_subfolder = True
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))

    def set_src_folder(self, foldername):
        """Set source path

        It just sets the source path

            * Bulletpoint1
            * Bulletpoint2

        **Title Test**:

        Test

        :param foldername: input folder
        :type foldername: string
        :returns: nothing
        :rtype: None

        :Example:

        >>> a = [10]
        >>> print(a)
        [10]

        .. note:: What to say here
        .. seealso:: :class:`FitParserC`
        .. warning:: my must be non-zero.
        .. todo:: check that arg2 is non zero.
        """
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

    def process_get_file_list(self,mypath):

        file_list = []
        for (dirpath, dirnames, filenames) in os.walk(mypath):
            file_list.extend(filenames)
            break

        for item in file_list:
            self._file_list.append(mypath + "/" + item)

    def get_file_list(self):
        return self._file_list

    def print_file_list(self):
        for item in self._file_list:
            print(item)
