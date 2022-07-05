import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText

# from Utility import *

from MainForm import MainForm

class FamilyTreeApp():
    def __init__(self):
        self.mainForm = MainForm()
        self.mainForm.mainloop()
                    

if __name__ == "__main__":
    app = FamilyTreeApp()
    