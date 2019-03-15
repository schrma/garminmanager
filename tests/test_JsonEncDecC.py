import datetime
import numpy as np

import garminmanager.utils.JsonEncDecC
import garminmanager.utils.FileWriterC

from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC



def test_encode_decode():

    raw_data = garminmanager.RawDataC.RawDataC()
    my_dates1 = {
        datetime.datetime(2019,4,11,1,00) : 100,
        datetime.datetime(2019,4,11,2,00) : 100,
        datetime.datetime(2019,4,11,3,00) : 100
            }
    for key, value in my_dates1.items():
        raw_data.add_x(key)
        raw_data.add_y(value)

    raw_data.set_data_type(EnumHealtTypeC.heartrate)
    json_enc_dec = garminmanager.utils.JsonEncDecC.JsonEncDecC()
    json_enc_dec.set_input_data(raw_data)
    json_string = json_enc_dec.encode()
    json_enc_dec.set_input_json(json_string)
    file_writer = garminmanager.utils.FileWriterC.FileWriterC()
    file_writer.set_filename('test.json')
    file_writer.set_text(json_string)
    file_writer.write_text_to_file()
    d = file_writer.read_json()
    json_enc_dec.set_input_json(d)
    json_enc_dec.decode()
    raw_data_output = json_enc_dec.get_data()
    assert raw_data == raw_data_output
