import sys
import serial
from serial.tools import list_ports
import argparse

#parser = argparse.ArgumentParser(description='Send an integer to pico')
#parser.add_argument('integer', type=int, nargs='?', default=1, help='an interger to send to pico')
#args = parser.parse_args()

parser = argparse.ArgumentParser(description='Send data to pico')
parser.add_argument('status', type=str, nargs=1, default='ON', help='status of the pin')
parser.add_argument('pin', type=int, nargs=argparse.REMAINDER, help='pin numbers to send to pico')
args = parser.parse_args()

class usbcomm:
    ser = []

    def __init__(self):
        pass

    def connect(self, port):
        self.ser = serial.Serial(port=port, baudrate=115200, timeout=1)

    def listports(self):
        l = list_ports.comports() 
        connected = [] 
        for i in l:
            connected.append(i.device)

        return connected

    def findpico(self):
        l = list_ports.comports()
        pico = []
        for i in l:
            if i.manufacturer == 'MicroPython':
                pico.append(i.device)

        return pico

    def send_data(self, data):
        self.ser.write(f"{data}\r".encode())
        mes = self.ser.read_until().strip()
        return mes.decode()

    def get_pin_status(self, pcfid=0):
        return self.send_data(f"{pinstat} {pcfid}")

    def disconnect(self):
        self.ser.close()


def main():
    comm = usbcomm()
    port = comm.findpico()
    comm.connect(port[0]) 

    data = ' '.join(sys.argv[1:])
    print('Send ', data) 
    ret = comm.send_data(data)
    print (ret)

    comm.disconnect()



if __name__ == "__main__":
    main()
