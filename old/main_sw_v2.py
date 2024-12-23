import utime
import usbcomm
from Switching2x2_v2 import Switching2x2_v2
from ledctl import LED
from seg7ctl import display

def main():
    swm = Switching2x2_v2() 

    led = LED()
    led.on()
    utime.sleep(0.5)
    led.off()
    
    utime.sleep(1) 

    pre = "CH "

    while True:
        try:
            Nsw = usbcomm.listen()
            Nsw = int(Nsw)

            # use 7-segment display to indicate sw number
            line = pre + f"{Nsw}" 
            display(line)

            swm.disable_all_switches()
            swm.enable_switch(Nsw)

        except KeyboardInterrupt:
            break
        except:
            led.indicate_error()


if __name__ == "__main__":
    main()
