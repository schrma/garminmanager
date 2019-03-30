import logging
import os
import numpy as np
from transitions import Machine, State

from datetime import datetime
import datetime

from fitparse import FitFile

from garminmanager.enumerators.EnumHealthTypeC import EnumHealtTypeC
import garminmanager.RawDataC
from garminmanager.fitparser.FitParserC import FitParserC

from garminmanager.utils.StatemachineC import StateMachineC



_logger = logging.getLogger(__name__)

class FitParserStepsC(FitParserC):

    def __init__(self, loglevel=logging.INFO):
        FitParserC.__init__(self,loglevel)
        self._process_type = EnumHealtTypeC.steps
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._save_last_state = []
        self._init_state_machine()
        self._raw_data_running_steps = garminmanager.RawDataC.RawDataC(process_type=EnumHealtTypeC.steps_running)
        self._raw_data_walking_steps = garminmanager.RawDataC.RawDataC(process_type=EnumHealtTypeC.steps_walking)
        self._raw_data_walking_distance = garminmanager.RawDataC.RawDataC(process_type=EnumHealtTypeC.distance_walking)
        self._raw_data_running_distance = garminmanager.RawDataC.RawDataC(process_type=EnumHealtTypeC.distance_running)

    def process(self):
        switch_options = {EnumHealtTypeC.heartrate: self._process_hearrate,
                          EnumHealtTypeC.intensity: self._process_intensity,
                          }

        my_type = self._process_type
        # switch_options = {1 : self.printB,
        #     2 : self.printA,
        # }

        try:
            switch_options[my_type]()
        except:
            print("C")

    def get_data(self):
        return self._raw_data

    def _is_walking(self):
        if self._record.name == "activity_type" and self._record.value == "walking":
            return True
        else:
            return False

    def _is_running(self):
        if self._record.name == "activity_type" and self._record.value == "running":
            return True
        else:
            return False

    def _is_step(self):
        if self._record.name == "steps":

            return True
        else:
            return False

    def _is_distance(self):
        if self._record.name == "distance":
            return True
        else:
            return False

    def _init_state_machine(self):
        states = [
            State(name='Init',on_exit=['_save_state']),
            State(name='first_timestamp', on_exit=['_save_state']),
            State(name='timestamp', on_exit=['_save_state']),
            State(name='running', on_exit=['_save_state']),
            State(name='walking', on_exit=['_save_state']),
            State(name='running', on_exit=['_save_state']),
            State(name='distance', on_exit=['_save_state']),
            State(name='steps', on_exit=['_save_state'])]



        self.machine = Machine(model=self, states=states, initial='Init')

        self.machine.add_transition('run', 'Init', 'first_timestamp', conditions=['_is_first_timestamp'])
        self.machine.add_transition('run', 'first_timestamp', 'timestamp', conditions=['_is_timestamp'])
        self.machine.add_transition('run', '*', 'timestamp', conditions=['_is_timestamp'])
        self.machine.add_transition('run', 'timestamp', 'running', conditions=['_is_running'])
        self.machine.add_transition('run', 'timestamp', 'walking', conditions=['_is_walking'])
        self.machine.add_transition('run', 'walking', 'steps', conditions=['_is_step'])
        self.machine.add_transition('run', 'walking', 'distance', conditions=['_is_distance'])
        self.machine.add_transition('run', 'running', 'steps', conditions=['_is_step'])
        self.machine.add_transition('run', 'running', 'distance', conditions=['_is_distance'])

        self.machine.on_enter_distance(self._handle_distance)
        self.machine.on_enter_steps(self._handle_steps)


    def _handle_data(self,raw_data):
        raw_data.add_xy(self._current_timestamp, self._record.value)
        if self._save_last_state == 'walking':
            self.to_walking()
        else:
            self.to_running()

    def _handle_distance(self):

        if self._save_last_state == 'running':
            self._handle_data(self._raw_data_running_distance)
        elif self._save_last_state == 'walking':
            self._handle_data(self._raw_data_walking_distance)
        else:
            raise NotImplementedError

    def _handle_steps(self):
        if self._save_last_state == 'running':
            self._handle_data(self._raw_data_running_steps)
        elif self._save_last_state == 'walking':
            self._handle_data(self._raw_data_walking_steps)
        else:
            raise NotImplementedError

    def _save_state(self):
        self._save_last_state = self.state




    def _process_steps_single_file(self,filename):
        try:
            fitfile = FitFile(filename)
        except:
            _logger.error("File %s not found", filename)
            return

        for record in fitfile.get_messages():
            # Go through all the data entries in this record
            for record_data in record:
                self._record.name = record_data.name
                self._record.value = record_data.value
                self.machine.run()

        return self._raw_data
