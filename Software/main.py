#from pynput.keyboard import Key, Controller
from time import sleep
from GUI import GUI,color

import threading
import serial

def read_serial():
    with serial.Serial('COM3', 9600, timeout=1) as comm:
        while True:
            sleep(1)
            readOneByte = comm.read()
            #print(readOneByte)
            if color != 0:
                print(color)

if __name__=='__main__':
    #GUI("Macropad")
    gui = threading.Thread(target=GUI, args=("Macropad",))


    read_serial_thread = threading.Thread(target=read_serial, args=())
    gui.start()
    read_serial_thread.start()