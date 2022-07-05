from Enums import TableTypeEnums
from Table_using_Widgets import TableUsingWidgets
from Table_using_Treeview import TableUsingTreeview

class TableFactory:

    @staticmethod
    def createTable(TableType, widget):
        if TableType == TableTypeEnums.UsingWidget:
            return TableUsingWidgets(widget)
        if TableType == TableTypeEnums.UsingTreeView:
            return TableUsingTreeview(widget)
