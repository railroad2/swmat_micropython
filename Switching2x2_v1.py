#################################################
# Switching matrix 2x2 ver. 1
#################################################

# see pin_v1.md for pin setup
from PICO_ADG633 import PICO_ADG633
from PICO_ADG1406 import PICO_ADG1406
from pin_v1 import *


class Switching2x2_v1(object):
    self.ADG633 = []
    self.ADG1406 = []

    def __init__(self):
        self.ADG633.append(PICO_ADG633(pin_ADG633_1))
        self.ADG633.append(PICO_ADG633(pin_ADG633_2))
        self.ADG1406.append(PICO_ADG1406(pin_ADG1406_1))
        self.pin_led = Pin("LED", mode=Pin.OUT)

    def __select_path(self, path):
        swi = path["switch"] // 10
        swj = path["switch"] % 10
        muxi = path["mux"] // 100 
        muxj = path["mux"] % 100

        self.ADG633[swi].sw[swj].on()
        self.ADG1406[muxi].select_channel(muxj)
    
    def __find_path(self, name, val):
        for pp in probe_path:
            if pp[name] == val:
                return pp

        print ("WARNING: Cannot find the path for the given input {name}={val}")

        return None

    def enable(self):
        for a in self.ADG633:  a.enable()
        for a in self.ADG1406: a.enable()

    def disable(self):
        for a in self.ADG633:  a.disable()
        for a in self.ADG1406: a.disable()
        
    def select_probe(self, probe):
        path = self.__find_path("probe", probe)
        self.__select_path(self, path)

    def select_mux(self, mux):
        path = self.__find_path("mux", mux)
        self.__select_path(self, path)

    def select_pad(self, pad):
        path = self.__find_path("pad", pad)
        self.__select_path(self, path)
        
    def reset_all_sw(self):
        for sw in ADG633:
            sw.reset()

    # end of class
