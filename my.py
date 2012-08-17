#!/usr/bin/env python
from evdev import InputDevice, ecodes
from select import select

import Tkinter as tk

import subprocess

dev = InputDevice('/dev/input/event4')


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.text = tk.Text(self.root)
        self.text.pack()
        self.button = tk.Button(self.root, text="Get Selection", command=self.OnButton)
        self.button['text'] = 's'
        self.button.pack()
        self.root.mainloop()

    def OnButton(self):
        while True:
            r, w, x = select([dev], [], [])
            for event in dev.read():
                if event.type == ecodes.EV_KEY and event.code == 272 and event.value == 00:
                    try:
                        self.text['text'] = self.root.selection_get()
                    except:
                        self.text['text'] = 'nothing selected'
    #     self.text['text'] += self.root.selection_get()
    #     # self.text.get("sel.first", "sel.last")
        # print "selected text: '%s'" % self.text.get("sel.first", "sel.last")

app = App()