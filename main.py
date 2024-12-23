import sys
import utime
import usbcomm
from Switching256ch import Switching256ch
from ledctl import LED
#from seg7ctl import display

DEBUG=0

def main():
    swm = Switching256ch() 

    led = LED()
    led.on()
    utime.sleep(0.5)
    led.off()
    
    utime.sleep(0.5) 
    print ("connected")

    pre = "CH "

    while True:
        try:
            Nsw = usbcomm.listen(swm)
            #Nsw = 'ON 0 1 2 3 4 5'
            Nsw = Nsw.split(' ')

            stat, pins = Nsw[0], Nsw[1:]

            # use 7-segment display to indicate sw number
            #line = pre + f"{Nsw}" 
            #display(line)

            if DEBUG:
                swm.print_connected_pcfs()

            if stat.upper() == 'ON':
                for pin in pins:
                    swm.enable_switch(int(pin))
                if DEBUG:
                    print ('turning ON', Nsw)
            elif stat.upper() == 'OFF':
                for pin in pins:
                    swm.disable_switch(int(pin))
                if DEBUG:
                    print ('turning OFF', Nsw)

            utime.sleep(1)

        except KeyboardInterrupt:
            print ("KeyboardInterrupt")
            break
        except Exception as e:
            print (e)
            led.indicate_error()


if __name__ == "__main__":
    main()

