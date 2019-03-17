import pickle
import numpy as np

import garminmanager.FitParserC
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

def cmp(a, b):
    return (a > b) - (a < b)