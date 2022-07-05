import tkinter as tk
import tkinter.ttk as ttk
from DAO_File import FileDaoClass

class TableUsingTreeview():

    def __init__(self, widget):
        self.db = FileDaoClass()
        # self.db.setFilePath("db.json")
        # self.db.loadDataSource()
        self.widget = widget


    def loadSpecificFamiltyDataInTable(self, memberId):
        pass


    def loadAllDataInTable(self, memberId):
        my_game = ttk.Treeview(self.widget)

        # my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')
        my_game['columns'] = ["id", "member name", "nic name", "place", "spouce name", "ParentId", "Children"]

        my_game.column("#0", width=0,  stretch=tk.NO)
        my_game.column("id",anchor=tk.CENTER, width=40)
        my_game.column("member name",anchor=tk.CENTER,width=100)
        my_game.column("nic name",anchor=tk.CENTER,width=100)
        my_game.column("place",anchor=tk.CENTER,width=100)
        my_game.column("spouce name",anchor=tk.CENTER,width=100)
        my_game.column("ParentId",anchor=tk.CENTER,width=100)
        my_game.column("Children",anchor=tk.CENTER,width=100)

        my_game.heading("#0",text="",anchor=tk.CENTER)
        my_game.heading("id",text="Id",anchor=tk.CENTER)
        my_game.heading("member name",text="member name",anchor=tk.CENTER)
        my_game.heading("nic name",text="nic name",anchor=tk.CENTER)
        my_game.heading("place",text="place",anchor=tk.CENTER)
        my_game.heading("spouce name",text="Spouce",anchor=tk.CENTER)
        my_game.heading("ParentId",text="parentId",anchor=tk.CENTER)
        my_game.heading("Children",text="Children",anchor=tk.CENTER)
        j = 0
        for id, data in self.db.dataSource.items():
            temp = [id] + [value for key, value in data.items()][:-1] + [len(data["children"])]
            my_game.insert(parent='',index='end',iid=j, values=(tuple(temp)))
            j = j+1
        
        my_game.grid(row=5, columnspan=5)
