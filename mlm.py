#!/usr/bin/env python
from Tkinter import *
from evdev import InputDevice, ecodes
from select import select
from unidecode import unidecode

import codecs
import re
from local_settings import *





lines = []
for filename in DICS:
    f = codecs.open(filename, 'r', 'utf-8')
    lines += f.readlines()
if STRIP_ACCENTS:
    lines = [unidecode(x) for x in lines]

print lines[10:20]


def log(*args):
    if DEBUG:
        args = [unicode(x) for x in args]
        print ' '.join(args)


class App:
    def __init__(self):
        self.oldwhat = 'init'

        self.root = Tk()
        self.root.wm_title("mlm")
        self.root.geometry(GEOMETRY)

        self.text = Text(self.root, width=40, height=ROWS)
        self.text.pack()
        self.text.tag_configure('head', font='helvetica 12 bold', background='#b4e5c4')
        self.text.tag_configure('line', font='helvetica 8 bold', background='#50C878')
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
                    # log('what', what, len(what), type(what))
                    if not MIN_WORD_LENGTH <= len(what) <= MAX_WORD_LENGTH:
                        break
                except:
                    log('either selection was too short or nothing was selected')
                    break
                if self.oldwhat != what:
                    self.oldwhat = what
                    self.text.delete("1.0", END)
                    if STRIP_ACCENTS:
                        what = unidecode(what)
                    if CUT_ENDINGS:
                        what = self.strip_plural_endings(what)
                        if IZPLURALS and what[-1] == 'c':
                            what = what[:-1] + 'z'
                    if DEFEMINIZE:
                        what = self.mu_rep(what,
                            # quetsionable
                            {
                            'ida': 'ido',
                            'gua': 'guo',
                            'ada': 'ado',
                            'ana': 'ano',
                            'ora': 'or'
                            }
                            )

                    # probably this could be rewritten, one call and sort
                    if KINDLE_MODE:
                        grep_output = self.grepf('(^|\t)%s\s' % what, lines)
                        no_of_matches = len(grep_output)
                    else:
                        grep_output = ['?:exact head hits'] + \
                                      self.grepf('^%s\s' % what, lines) + \
                                      ['?:partial head hits'] + \
                                      self.grepf('^%s[^\s]' % what, lines) + \
                                      ['?:exact derivativative hits'] + \
                                      self.grepf('\s(?<!^)%s\s' % what, lines) + \
                                      ['?:partial derivativative hits'] + \
                                      self.grepf('\s(?<!^)%s[^\s]' % what, lines)
                        no_of_matches = len(grep_output) - 3
                    log('found', no_of_matches, 'matches')
                    log('grep_output', grep_output)

                    for grep in reversed(grep_output[:DISPLAY_RESULTS]):
                        if not '?:' in grep:
                            head, the_rest = grep.split('\t', 1)
                            derivatives, definition = the_rest.rsplit('\t', 1)
                            log(grep)
                            self.text.insert("1.0", "%s\n" % definition.replace('; ', '\n'), 'definitions')
                            if D:
                                self.text.insert("1.0", "%s\n" % derivatives, 'linked')
                            if '{v' in head:
                                try:
                                    index = derivatives.split('\t').index(what)
                                    log('index', index)
                                    self.text.insert("1.0", "%s\n" % index, 'linked')
                                except:
                                    pass
                            self.text.insert("1.0", "%s\n" % head, 'head')

                        else:
                            self.text.insert("1.0", "%s\n" % grep[2:], 'line')
                    self.root.lift()
                else:
                    log("same selection")

        self.root.after(100, self.lop)

    def strip_plural_endings(self, string):
        expr = re.compile('[e]{0,}s$', flags=re.U | re.I)
        ret = expr.sub('', string)
        print ret
        if len(ret) != len(string):
            log('ending cut %s > %s' % (string, ret))
        return ret

    def mu_rep(self, string, replacements={}):
        """multiple replace, string, dic => string; ex. dic = {'/*': '\t', '-\t': ''} """
        return reduce(lambda a, (b, c): a.replace(b, c), replacements.items(), string)

    def strip_accents(self, s):
        # http://stackoverflow.com/a/518232/1472229
        return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

    # http://casa.colorado.edu/~ginsbura/pygrep.htm
    def grepf(self, string, list):
        expr = re.compile(string, flags=re.I)
        return filter(expr.search, list)

app = App()
