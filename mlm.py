#!/usr/bin/env python
from Tkinter import *
from evdev import InputDevice, ecodes
from select import select

import codecs
import re
from local_settings import *

# config section



# http://casa.colorado.edu/~ginsbura/pygrep.htm
def grepf(string, list):
    expr = re.compile(string, flags=re.U | re.I)
    return filter(expr.search, list)



lines = []
for filename in DICS:
    f = codecs.open(filename, 'r', 'utf-8')
    lines += f.readlines()

print lines[26294:26300]


class App:
    def __init__(self):
        self.oldwhat = 'init'

        self.root = Tk()
        self.root.wm_title("mlm")
        self.root.geometry(GEOMETRY)

        self.text = Text(self.root, width=40, height=ROWS)
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
                    if not MIN_WORD_LENGTH <= len(what) <= MAX_WORD_LENGTH:
                        break
                except:
                    if D:
                        print 'either selection was too short or nothing was selected'
                    break
                if self.oldwhat != what:
                    self.oldwhat = what
                    self.text.delete("1.0", END)
                    if CUT_ENDINGS:
                        what = self.strip_plural_endings(what)
                        print 'ending cut', what
                    if REPLACE:
                        what = self.mu_rep(what,
                            # quetsionable
                            {
                            'ida': 'ido',
                            'gua': 'guo'
                            }
                            )
                    if D:
                        inter = ['m:next group']
                    else:
                        inter = []
                    # probably this could be rewritten, one call and sort
                    if KINDLE_MODE:
                        grep_output = grepf('(^|\t)%s\s' % what, lines)
                    else:
                        grep_output = grepf('^%s\s' % what, lines) + \
                                      inter + \
                                      grepf('^%s[^\s]' % what, lines) + \
                                      inter + \
                                      grepf('\s(?<!^)%s\s' % what, lines) + \
                                      inter + \
                                      grepf('\s(?<!^)%s[^\s]' % what, lines)
                    if D:
                        print 'found', len(grep_output), 'matches'
                        print 'grep_output', grep_output
                    for grep in reversed(grep_output[:DISPLAY_RESULTS]):
                        if not 'm:' in grep:
                            head, the_rest = grep.split('\t', 1)
                            derivatives, definition = the_rest.rsplit('\t', 1)
                            if D:
                                print grep
                            self.text.insert("1.0", "%s\n" % definition.replace('; ', '\n'), 'definitions')
                            if D:
                                self.text.insert("1.0", "%s\n" % derivatives, 'linked')
                            self.text.insert("1.0", "%s\n" % head, 'head')

                        else:
                            self.text.insert("1.0", "%s\n" % grep[2:], 'message')
                    self.root.lift()
                else:
                    if D:
                        print "same selection"

        self.root.after(100, self.lop)

    def strip_plural_endings(self, string):
        expr = re.compile('[e]{0,}s$', flags=re.U | re.I)
        return expr.sub('', string)

    def mu_rep(self, string, replacements={}):
        """multiple replace, string, dic => string; ex. dic = {'/*': '\t', '-\t': ''} """
        return reduce(lambda a, (b, c): a.replace(b, c), replacements.items(), string)


app = App()
