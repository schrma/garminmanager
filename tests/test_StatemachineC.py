from garminmanager.utils.StatemachineC import StateMachineC
from transitions import Machine

import logging

logging.getLogger('transitions').setLevel(logging.INFO)


def start_transitions(txt):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word == "goYellow":
        newState = "Yellow"
        print("changed to yellow")
    else:
        newState = "Green"
        print("Still green")
    return (newState, txt)

def yellow_state_transition(txt):
    splitted_txt = txt.split(None, 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if word == "goRed":
        newState = "Red"
        print("changed to red")
    else:
        newState = "error_state"
        print("Still yellow")
    return (newState, txt)

class SignalStateMachineC(object):
    states =  ['Green', 'Yellow', 'Red', 'error_state']

    def set_text(self,txt):
        self._txt = txt

    def __init__(self, name):
        self.name = name

        # Initialize the state machine
        self.machine = Machine(model=self, states=SignalStateMachineC.states, initial='Green')
        self.machine.add_transition('run', 'Green', 'Yellow', conditions=['is_go_yellow'])
        self.machine.add_transition('run', 'Yellow', 'Red', conditions=['is_go_red'])
        self.machine.add_transition('run', '*', 'error_state', unless=['is_go_red','is_go_yellow'])

    def is_go_yellow(self):
        splitted_txt = self._txt.split(None, 1)
        word, self._txt = splitted_txt if len(splitted_txt) > 1 else (self._txt, "")
        if word == "goYellow":
            return True
        else:
            return False

    def is_go_red(self):
        splitted_txt = self._txt.split(None, 1)
        word, self._txt = splitted_txt if len(splitted_txt) > 1 else (self._txt, "")
        if word == "goRed":
            return True
        else:
            return False

def test_statemachine():
    m = StateMachineC()
    m.add_state("Green", start_transitions)
    m.add_state("Yellow", yellow_state_transition)
    m.add_state("Red", None, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start("Green")
    r1 = m.run("goBlue goYellow goRed")
    r2 = m.run("goBlue goYellow goRed1")
    r3 = m.run("this goes wrong")

    n = SignalStateMachineC("Ampel")
    n.set_text("Ups goYellow goRed")
    n.run()
    print(n.state)
    n.run()
    print(n.state)
    pass







    assert r1
    assert r2
    assert r3 == -1
