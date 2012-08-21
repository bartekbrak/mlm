#!/usr/bin/env python
from Tkinter import *
from evdev import InputDevice, ecodes
from select import select

import codecs
import subprocess
import re

# config section
D = DEBUG = True
CUT_ENDINGS = False
MIN_WORD_LENGTH = 3
MAX_WORD_LENGTH = 20
DISPLAY_RESULTS = 40
DICS = [
    '/home/bartek/workspace/mlm/dics/wiktionary.tsv',
    '/home/bartek/workspace/mlm/dics/my.tsv'
 ]
DEV = InputDevice('/dev/input/by-path/pci-0000:00:1a.1-usb-0:2:1.0-event-mouse')


# http://casa.colorado.edu/~ginsbura/pygrep.htm
def grepf(string, list):
    expr = re.compile(string, flags=re.U | re.I)
    return filter(expr.search, list)

lines = []
for filename in DICS:
    f = codecs.open(filename, 'r', 'utf-8')
    lines += f.readlines()


class App:
    def __init__(self):
        self.oldwhat = 'init'

        self.root = Tk()
        self.root.wm_title("mlm")
        self.root.geometry("286x1050+1394+0")

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
                    if D:
                        print 'what', what, len(what), type(what)
                    if not MIN_WORD_LENGTH < len(what) < MAX_WORD_LENGTH:
                        break
                    if CUT_ENDINGS:
                        what = what[:-1]  # what a silly rule
                except:
                    if D:
                        print 'either selection was too short or nothing was selected'
                    break
                if self.oldwhat != what:
                    self.oldwhat = what
                    self.text.delete("1.0", END)
                    grep_output = list(set(grepf('^%s' % what, lines) + grepf('\s%s' % what, lines)))
                    if D:
                        print 'found', len(grep_output), 'matches'
                        print 'grep_output', grep_output
                    for grep in reversed(grep_output[:DISPLAY_RESULTS]):
                        head, the_rest = grep.split('\t', 1)
                        derivatives, definition = the_rest.rsplit('\t', 1)
                        if D:
                            print grep
                        self.text.insert("1.0", "%s\n" % definition.replace('; ', '\n'), 'definitions')
                        if D:
                            self.text.insert("1.0", "%s\n" % derivatives, 'linked')
                        self.text.insert("1.0", "%s\n" % head, 'head')
                        self.root.lift()
                else:
                    if D:
                        print "same selection"

        self.root.after(100, self.lop)

app = App()
