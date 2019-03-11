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
    # with open("test.txt", "wb") as fp:  # Pickling
    #     pickle.dump(result, fp)
    with open("./tests/samples/result_test_process_hearrate_pickle.txt", "rb") as fp:  # Unpickling
        org_data = pickle.load(fp)

    result.data_array[np.isnan(result.data_array)] = -100
    org_data.data_array[np.isnan(org_data.data_array)] = -100
    #org_data.data_array[10] = 10
    assert (result.data_array == org_data.data_array).all()
    assert (result.timestamp_array == org_data.timestamp_array).all()
    print("ok")

def cmp(a, b):
    return (a > b) - (a < b)