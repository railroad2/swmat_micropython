from utime import sleep
from machine import Pin

class PICO_ADG1406(object):
    pins = []
    EN = []
    A0 = []
    A1 = []
    A2 = []
    A3 = []

    def __init__(self, pids=[]):
        # initiate
        self.configure_pins(pids)

    def configure_pins(self, pids):
        if len(pids) != 5:
            print("ADG1406 needs five pins assigned in the following order.")
            print("EN, A0, A1, A2, A3")
            return -1

        self.EN = Pin(pids[0], mode=Pin.OUT)
        self.A0 = Pin(pids[1], mode=Pin.OUT)
        self.A1 = Pin(pids[2], mode=Pin.OUT)
        self.A2 = Pin(pids[3], mode=Pin.OUT)
        self.A3 = Pin(pids[4], mode=Pin.OUT)

        self.disable()
        
        return 0
    
    def set_pins(self, stat=""):
        if len(stat) == 4:
            self.A0.value(self.__conv_to_01(stat[3]))
            self.A1.value(self.__conv_to_01(stat[2]))
            self.A2.value(self.__conv_to_01(stat[1]))
            self.A3.value(self.__conv_to_01(stat[0]))
        elif len(stat) == 5:
            self.EN.value(self.__conv_to_01(stat[4]))
            self.A0.value(self.__conv_to_01(stat[3]))
            self.A1.value(self.__conv_to_01(stat[2]))
            self.A2.value(self.__conv_to_01(stat[1]))
            self.A3.value(self.__conv_to_01(stat[0]))
        else:
            print("Input bits has to be 4 or 5-bit long")
            return -1

        sleep(0.1)
        return 0
        
    def disable(self):
        self.EN.off()
        sleep(0.1)
        return 0
    
    def enable(self):
        self.EN.on()
        sleep(0.1)
        return 0

    def reset(self):
        self.set_pins("0000")

    def select_channel(self, nch):
        bch = self.__nch2bin(nch)
        bch += str(self.EN.value())
        self.set_pins(bch)
        return 0

    def __nch2bin(self, nch):
        if nch < 0:
            raise "Invalid channel number"

        nchb = int(bin(nch-1)[2:])
         
        return f"{nchb:04d}"

    def __conv_to_01(self, anything):
        return int(bool(int(anything)))

    # end of class
    
