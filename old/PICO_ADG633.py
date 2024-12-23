from machine import Pin

class PICO_ADG633(object):
    pins = []
    EN = []
    A0 = []
    A1 = []
    A2 = []
    sw = []

    def __init__(self, pids=[]):
        # initiate
        self.configure_pins(pids)
        self.configure_switches()
    
    class switch:
        def __init__(self, pin):
            self.pin = pin
        
        def on(self):
            self.pin.off()
        
        def off(self):
            self.pin.on()

        def __call__(self):
            return int(not(self.pin.value()))


    def configure_pins(self, pids):
        if len(pids) != 4:
            print("ADG633 needs four pins assigned in the following order.")
            print("EN, A0, A1, A2")
            return -1

        self.EN = Pin(pids[0], mode=Pin.OUT)
        self.A0 = Pin(pids[1], mode=Pin.OUT)
        self.A1 = Pin(pids[2], mode=Pin.OUT)
        self.A2 = Pin(pids[3], mode=Pin.OUT)

        self.disable()
        
        return 0
    
    def configure_switches(self):
        self.s1 = self.switch(self.A0)
        self.s2 = self.switch(self.A1)
        self.s3 = self.switch(self.A2)
        self.sw = [self.s1, self.s2, self.s3]
    
    def set_pins(self, stat=""):
        if len(stat) == 4:
            self.EN.value(self.__conv_to_01(stat[3]))
            self.A0.value(self.__conv_to_01(stat[2]))
            self.A1.value(self.__conv_to_01(stat[1]))
            self.A2.value(self.__conv_to_01(stat[0]))
        elif len(stat) == 3:
            self.A0.value(self.__conv_to_01(stat[2]))
            self.A1.value(self.__conv_to_01(stat[1]))
            self.A2.value(self.__conv_to_01(stat[0]))
        else:
            print("Input bits has to be 4-bit long")
            return -1

        return 0
        
    def disable(self):
        self.EN.on()
        return 0
    
    def enable(self):
        self.EN.off()
        return 0

    def reset(self): # set all switches to off (B state)
        self.set_pins("111")
        return 0

    def __conv_to_01(self, anything):
        return int(bool(int(anything)))

    # end of class
    
