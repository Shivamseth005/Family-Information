# Python program to create a table

import tkinter as tk
from DAO_File import FileDaoClass

class TableUsingWidgets():

    def __init__(self, widget):
        self.db = FileDaoClass()
        # self.db.setFilePath("db.json")
        # self.db.loadDataSource()
        self.widget = widget


    def loadSpecificFamiltyDataInTable(self, memberId):
        pass

    
    def loadAllDataInTable(self, memberId):
        # code for creating table
        i = 20;
        j = 0;

        headers = ["Name", "Nic Name", "Place", "Spouce", "ParentId", "Children"]
        for key in headers:
            self.e = tk.Label(self.widget, text=key, width=12, fg='blue', font=('Arial',12,'bold'))
            self.e.grid(row=i, column=j, padx=1, pady=1, ipady=2)
            j = j+1
        i=i+1

        for id, data in self.db.dataSource.items():
            j = 0
            for key, value in self.db.dataSource[id].items():
                self.e = tk.Entry(self.widget, width=22, fg='blue', font=('Arial',10))
                self.e.grid(row=i, column=j, padx=1, pady=1, ipady=2)
                if key == "children":
                    value = len(value)
                self.e.insert(tk.END, value)
                self.e.config(state=tk.DISABLED)
                j = j+1
            i = i+1

    
