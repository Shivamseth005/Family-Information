import tkinter as tk
import tkinter.ttk as ttk
from DAO_File import FileDaoClass

class TableUsingTreeview():

    def __init__(self, widget):
        self.db = FileDaoClass()
        # self.db.setFilePath("db.json")
        # self.db.loadDataSource()
        self.widget = widget

    def clearTable(self):
        self.table.destroy()

    def fillHeaders(self):
        self.table = ttk.Treeview(self.widget)

        # self.table['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')
        self.table['columns'] = ["id", "member name", "nic name", "place", "spouce name", "ParentId", "Children"]

        self.table.column("#0", width=0,  stretch=tk.NO)
        self.table.column("id",anchor=tk.CENTER, width=40)
        self.table.column("member name",anchor=tk.CENTER,width=100)
        self.table.column("nic name",anchor=tk.CENTER,width=100)
        self.table.column("place",anchor=tk.CENTER,width=100)
        self.table.column("spouce name",anchor=tk.CENTER,width=100)
        self.table.column("ParentId",anchor=tk.CENTER,width=100)
        self.table.column("Children",anchor=tk.CENTER,width=100)

        self.table.heading("#0",text="",anchor=tk.CENTER)
        self.table.heading("id",text="Id",anchor=tk.CENTER)
        self.table.heading("member name",text="member name",anchor=tk.CENTER)
        self.table.heading("nic name",text="nic name",anchor=tk.CENTER)
        self.table.heading("place",text="place",anchor=tk.CENTER)
        self.table.heading("spouce name",text="Spouce",anchor=tk.CENTER)
        self.table.heading("ParentId",text="parentId",anchor=tk.CENTER)
        self.table.heading("Children",text="Children",anchor=tk.CENTER)


    def loadSpecificFamiltyDataInTable(self, memberId):
        self.fillHeaders()
        memberList = [memberId]
        j = 0
        for mId in memberList:
            familyInfo = self.db.dataSource[mId]
            memberList.extend(familyInfo['children'])
            data = self.db.dataSource[mId]
            temp = [mId] + [value for key, value in data.items()][:-1] + [len(data["children"])]
            self.table.insert(parent='',index='end',iid=j, values=(tuple(temp)))
            j = j+1
        self.table.grid(row=5, columnspan=5)


    def loadAllDataInTable(self, memberId):
        self.fillHeaders()
        j = 0
        for id, data in self.db.dataSource.items():
            temp = [id] + [value for key, value in data.items()][:-1] + [len(data["children"])]
            self.table.insert(parent='',index='end',iid=j, values=(tuple(temp)))
            j = j+1
        
        self.table.grid(row=5, columnspan=5)
