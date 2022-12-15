from tkinter import *
from pynput.keyboard import Key, Controller

import serial

class GUI:

    def __init__(self) -> None:
        #constructor
        self.window = Tk()
        self.buttonList = []
        self.window.title("Macropad")
        self.window.geometry("500x500")

        self.window.mainloop()
if __name__ == '__main__':
    GUI()