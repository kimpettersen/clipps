import pyperclip
import threading
import os

from tkinter import Tk, Listbox, END
from time import sleep
from pynput import keyboard

class KeyboardListener:
    def __init__(self, gui):
        self.gui = gui

    def start(self):
        with keyboard.GlobalHotKeys({
                '<ctrl>+<shift>+c': self.gui.emit_copy_event,
                '<ctrl>+<shift>+x': self.gui.emit_copy_event,
                '<ctrl>+c': self.gui.emit_copy_event,
                '<ctrl>+x': self.gui.emit_copy_event,
                '<ctrl>+q': self.gui.quit
            }) as h:
            h.join()

class GUI:
    def __init__(self, window):
        self.copy_event_name = "<<COPY_EVENT>>"
        self.previous = ""

        self.window = window
        self.window.geometry("1000x600")
        
        dirpath = os.getcwd()

        self.window.iconbitmap(os.path.join(dirpath,'copyicon.icon'))
        self.window.title("Clipboard")
        self.window.bind(self.copy_event_name, self.handle_copy)
        
        self.listbox = Listbox(self.window)
        self.listbox.pack(fill="both", expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.handle_list_select)

    def emit_copy_event(self):
        self.window.event_generate(self.copy_event_name, when="tail")

    def handle_copy(self, c):
        item = pyperclip.paste()
        if item != self.previous:
            self.previous = item
            self.listbox.insert(0, item)

    def handle_list_select(self, event):
        widget = event.widget
        idx = widget.curselection()

        if idx == ():
            return
        idx = idx[0]
        item = widget.get(idx)
        pyperclip.copy(item)

    def quit(self):
        self.window.quit()

if __name__ == "__main__":
    window = Tk()
    gui = GUI(window)

    l = KeyboardListener(gui)    
    k = threading.Thread(target=l.start)
    k.daemon = True
    k.start()
    window.mainloop()

