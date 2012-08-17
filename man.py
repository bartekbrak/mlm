#!/usr/bin/env python
import Tkinter as tk
import tkFont


class App:
    def __init__(self):
        self.root = tk.Tk()
        # print root.winfo_toplevel()
        self.text = tk.Text(self.root)
        self.text.pack()
        self.button = tk.Button(self.root, text="Get Selection", command=self.OnButton)
        self.button['text'] = 's'
        self.button.pack()
        self.root.mainloop()

    def OnButton(self):
        self.text['text'] += self.root.selection_get()
        # self.text.get("sel.first", "sel.last")
        # print "selected text: '%s'" % self.text.get("sel.first", "sel.last")


app = App()
