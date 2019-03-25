import pickle
import numpy as np

import garminmanager.FitParserC
import garminmanager.utils.FileWriterC
from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC


def test_process_hearrate():


    test_files = ['./tests/samples/30731164854.fit',
                  './tests/samples/30763371770.fit'
                  ]
    fit_parser = garminmanager.FitParserC.FitParserC()
    fit_parser.set_file_list(test_files)
    fit_parser.set_type(EnumHealtTypeC.heartrate)
    fit_parser.process()
    result = fit_parser.get_data()
    with open("test.txt", "wb") as fp:  # Pickling
         pickle.dump(result, fp)
    with open("./tests/samples/result_test_process_hearrate_pickle.txt", "rb") as fp:  # Unpickling
        org_data = pickle.load(fp)


    x = result.get_x()
    y = result.get_y()

    org_x = org_data.get_x()
    org_y = org_data.get_y()

    y[np.isnan(y)] = -100
    org_y[np.isnan(org_y)] = -100
    #org_data.y_array[10] = 10

    assert (y == org_y).all()
    assert (x == org_x).all()

def test_parse_file():
    test_files = ['./tests/samples/30731164854.fit',
                  './tests/samples/30763371770.fit'
                  ]
    fit_parser = garminmanager.FitParserC.FitParserC()
    fit_parser.set_file_list(test_files)
    data = fit_parser.parse_file()

    compare_file = "./tests/samples/test_parse_file_FitParser.txt"

    with open(compare_file) as file:
        data_org = file.read()

    assert data_org == data
    # file_writer = garminmanager.utils.FileWriterC.FileWriterC()
    # file_writer.set_text(data)
    # file_writer.set_filename('my.txt')
    # file_writer.write_text_to_file()

def cmp(a, b):
    return (a > b) - (a < b)