
import garminmanager.RawDataC

def create_raw_data(my_date,process_type):
    raw_data = garminmanager.RawDataC.RawDataC()
    for key, value in my_date.items():
        raw_data.add_x(key)
        raw_data.add_y(value)

    raw_data.set_data_type(process_type)

    return raw_data