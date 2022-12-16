from tkinter import *
from tkinter.colorchooser import askcolor
from numpy import pad

from pynput import keyboard
from pynput.keyboard import Key

keys = []

color = 0x00
class GUI:
    
    def __init__(self, title, size="500x500") -> None:
        #constructor
        self.window = Tk()
        self.buttonList = []
        self.window.title(title)
        self.window.geometry(size)
        self.setup_Components()
        
        self.window.mainloop()

    def change_color(self):
        color = askcolor(title="Macropad Color Picker")
        print("Color:",color)

    def on_Press_Listener(self, key):
        
        try:
            name = key.char
        except: 
            name = key.name

        print(name)
        
        if name == "enter":
            self.listener.stop()
            self.w_chooseHotkey.destroy()
            print(keys)
        else:
            keys.append(key)
            Label(self.w_chooseHotkey, text=name, width=2,height=1,padx=1,pady=1).pack(side=LEFT)
    def change_Hotkey(self, button:int):
        print(button)
        self.w_chooseHotkey = Tk()
        self.w_chooseHotkey.geometry("200x70")
        self.w_chooseHotkey.title("Key:"+str(button))
        Label(self.w_chooseHotkey, text="Submit with ENTER").pack(side=BOTTOM)
        self.listener = keyboard.Listener(on_press=self.on_Press_Listener)
        self.listener.start()
        
        self.w_chooseHotkey.mainloop()
    def setup_Components(self):
        self.buttonList.append(Button(self.window, text="Button1",width=10, height=5, command=lambda: self.change_Hotkey(1)).grid(row=0, column= 0,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button2",width=10, height=5, command=lambda: self.change_Hotkey(2)).grid(row=0, column= 1,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button3",width=10, height=5, command=lambda: self.change_Hotkey(3)).grid(row=0, column= 2,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button4",width=10, height=5, command=lambda: self.change_Hotkey(4)).grid(row=1, column= 0,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button5",width=10, height=5, command=lambda: self.change_Hotkey(5)).grid(row=1, column= 1,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button6",width=10, height=5, command=lambda: self.change_Hotkey(6)).grid(row=1, column= 2,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button7",width=10, height=5, command=lambda: self.change_Hotkey(7)).grid(row=2, column= 0,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button8",width=10, height=5, command=lambda: self.change_Hotkey(8)).grid(row=2, column= 1,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button9",width=10, height=5, command=lambda: self.change_Hotkey(9)).grid(row=2, column= 2,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button10",width=10, height=5, command=lambda: self.change_Hotkey(10)).grid(row=3, column= 0,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button11",width=10, height=5, command=lambda: self.change_Hotkey(11)).grid(row=3, column= 1,padx=2,pady=2))
        self.buttonList.append(Button(self.window, text="Button12",width=10, height=5, command=lambda: self.change_Hotkey(12)).grid(row=3, column= 2,padx=2,pady=2))

        #ColorPicker Button
        self.button_ColorPicker = Button(self.window, text="Pick Color", command=self.change_color).grid(row=5, column=1)