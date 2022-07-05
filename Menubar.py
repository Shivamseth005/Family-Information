import tkinter as tk
from Enums import TableTypeEnums
from TableFactory import TableFactory

class MenuBar:

    def __init__(self, widget):
        self.menubar = tk.Menu(widget)

        self.AllMembers = tk.Menu(self.menubar, tearoff=0)
        self.AllMembers.add_command(label="Tree View", command=self.AllMembersTreeView)
        self.AllMembers.add_separator()
        self.AllMembers.add_command(label="Widgets", command=self.AllMembersWidgets)
        self.menubar.add_cascade(label="All Members", menu=self.AllMembers)

        self.ExitMenu = tk.Menu(self.menubar, tearoff=0)
        self.ExitMenu.add_command(label="Exit", command="tk.destroy")
        self.menubar.add_cascade(label="Exit", menu=self.ExitMenu)

    
    def AllMembersTreeView(self):
        print("AllMembersTreeView called")
        self.new_window = tk.Tk()
        self.new_window.title("View All Members using TreeView")
        self.table = TableFactory.createTable(TableTypeEnums.UsingTreeView, self.new_window)
        self.table.loadAllDataInTable('0')
    
    def AllMembersWidgets(self):
        print("AllMembersWidgets called")
        self.new_window = tk.Tk()
        self.new_window.title("View All Members using Widgets")
        self.table = TableFactory.createTable(TableTypeEnums.UsingWidget, self.new_window)
        self.table.loadAllDataInTable('0')

    def generateTable(self, memberId = '0'):
        if memberId == 0:
            self.table.loadAllDataInTable(memberId)
        else:
            self.table.loadSpecificFamiltyDataInTable(memberId)