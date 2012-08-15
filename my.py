#!/usr/bin/env python
from evdev import InputDevice, categorize, ecodes
from select import select

from Tkinter import Tk

wind = Tk()
# wind.withdraw()


dev = InputDevice('/dev/input/event4')
while True:
    r, w, x = select([dev], [], [])
    for event in dev.read():
        if event.type == ecodes.EV_KEY and event.code == 272 and event.value == 00:
            # print(categorize(event)), event
            print wind.selection_get()
            # wind.clipboard_clear()


