import logging
import os
import pytest
import shutil

import garminmanager
import garminmanager.utils
import garminmanager.utils.FileManagerC

__author__ = "marco"
__copyright__ = "copyMarco"
__license__ = "mit"

name_of_tst_folder = ['testFolder', 'testFolder/sub1', 'testfolder/sub2', 'testfolder/sub1/subsub1',
                      'testfolder/sub1/subsub2']
test_names = ['test1.txt', 'test2.txt', 'test3.txt',
              'sub1/sub1test1.txt', 'sub1/sub1test2.txt', 'sub2/sub1test1.txt'
              ]
dest_folder = 'testbackup'


@pytest.fixture()
# @pytest.fixture(scope='module')
def setup_files():
    sc = garminmanager.utils.FileManagerC.FilemManagerC()
    print("\nStart--------------------")

    for folder in name_of_tst_folder:
        sc.create_folder(folder)

    for myname in test_names:
        file_create_name = name_of_tst_folder[0] + "/" + myname
        open(file_create_name, 'a').close()

    yield

    print("\nEnd--------------------")


def test_set_src_folder():
    src_folder = os.getcwd()
    print(src_folder)
    sc = garminmanager.utils.FileManagerC.FilemManagerC(loglevel=logging.DEBUG)
    sc.set_src_folder(src_folder)
    assert src_folder == sc._src

def test_process_get_file_list(setup_files):
    sc = garminmanager.utils.FileManagerC.FilemManagerC(loglevel=logging.DEBUG)
    sc.process_get_file_list(name_of_tst_folder[0])
    file_list = sc.get_file_list()

    org_list = []
    for item in test_names[0:3]:
        org_list.append(name_of_tst_folder[0] + "/" + item)
    assert file_list == org_list


def test_set_dst_folder():
    dst_folder = os.getcwd()
    print(dst_folder)
    sc = garminmanager.utils.FileManagerC.FilemManagerC()
    sc.set_dst_folder(dst_folder)
    assert dst_folder == sc._dst


def test_folder_are_ok():
    sc = garminmanager.utils.FileManagerC.FilemManagerC()
    cwd_name = os.getcwd()
    assert (sc.folder_are_ok() is False)
    sc.set_dst_folder(cwd_name)
    assert (sc.folder_are_ok() is False)
    sc.set_src_folder(cwd_name)
    assert (sc.folder_are_ok() is True)


def test_move(setup_files):
    sc = garminmanager.utils.FileManagerC.FilemManagerC()
    sc.set_src_folder(name_of_tst_folder[0])
    sc.set_dst_folder(dest_folder)
    # For coverage purposes
    sc.create_folder(dest_folder)
    file_create_name = dest_folder + "/" + test_names[0]
    open(file_create_name, 'a').close()

    sc.move()
    assert check_files()
    sc.print_file_list()
    shutil.rmtree(dest_folder)


def check_files():
    for myname in test_names:
        file_create_name = dest_folder + "/" + myname
        if not os.path.isfile(file_create_name):
            print("Missing " + file_create_name)
            return False
    return True


def test_copy(setup_files):
    sc = garminmanager.utils.FileManagerC.FilemManagerC()
    sc.set_src_folder(name_of_tst_folder[0])
    sc.set_dst_folder(dest_folder)
    sc.copy()
    my_file_list = sc.get_file_list()
    assert check_files()
    shutil.rmtree(name_of_tst_folder[0])
    i = 0
    for myname in test_names:
        full_file = dest_folder + "/" + myname
        if not full_file == my_file_list[i]:
            assert False
        i = i + 1
    shutil.rmtree(dest_folder)
