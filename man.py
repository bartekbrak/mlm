#!/usr/bin/env python
import Tkinter as tk
import tkFont


class App:
    def __init__(self):
        root = tk.Tk()
        # print root.winfo_toplevel()
        self.text = tk.Text(root)
        self.text.pack()
        self.button = tk.Button(root, text="Get Selection", command=self.OnButton)
        self.button['text'] = 's'
        self.button.pack()
        root.mainloop()

    def OnButton(self):
        self.button['text'] += self.text.get("sel.first", "sel.last")
        # print "selected text: '%s'" % self.text.get("sel.first", "sel.last")


app = App()
