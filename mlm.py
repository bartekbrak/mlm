#!/usr/bin/env python
from Tkinter import *
from evdev import InputDevice, ecodes
from select import select

import subprocess


# config section
DEBUG = False
CUT_ENDINGS = True
MIN_WORD_LENGTH = 3
DISPLAY_RESULTS = 20
DICS = ['csvs/file.csv', 'csvs/my.csv']
DEV = InputDevice('/dev/input/event4')


class App:
    def __init__(self):
        self.oldwhat = 'init'

        self.root = Tk()
        self.root.wm_title("mlm")

        self.text = Text(self.root, width=40, height=80)
        self.text.pack()
        self.text.tag_configure('head', font='helvetica 12 bold', background='green')
        self.text.tag_configure('linked', font='helvetica 8 italic', lmargin1=10, lmargin2=10, rmargin=10)
        self.text.tag_configure('message', font='helvetica 8 italic', background='yellow')
        self.text.tag_configure('definitions', font='helvetica 10', lmargin1=10, lmargin2=10, rmargin=10)
        self.lop()
        self.root.mainloop()

    def lop(self):
        r, w, x = select([DEV], [], [])
        for event in DEV.read():
            if event.type == ecodes.EV_KEY and event.code == 272 and event.value == 00:
                try:
                    what = self.root.selection_get().strip()
                    if CUT_ENDINGS:
                        what = what[:-1]  # what a silly rule
                except:
                    what = ''
                if self.oldwhat != what:
                    self.oldwhat = what
                    self.text.delete("1.0", END)
                    try:
                        # the grep reads anything that matches but in first or second pairs of quotes, don't give me english
                        # ignore case and suppress filenames
                        grep_output = subprocess.check_output(["grep", "-hi", "\".*%s.*\"[^\"]*\"" % what] + DICS)
                    except subprocess.CalledProcessError:
                        self.text.insert("1.0", " %s - nothing found" % what, 'message')
                        break
                    grep_output = grep_output.rstrip("\n").split("\n")
                    for grep in grep_output[:DISPLAY_RESULTS]:
                        grep = grep.replace("\"", "").split(';')
                        if len(what) + int(CUT_ENDINGS) >= MIN_WORD_LENGTH:
                            self.text.insert("1.0", "%s\n\n" % grep[2].replace("\\n", "\n"), 'definitions')
                            if DEBUG:
                                self.text.insert("1.0", "%s\n" % grep[1], 'linked')
                            self.text.insert("1.0", "%s\n" % grep[0], 'head')
        self.root.after(100, self.lop)

app = App()
