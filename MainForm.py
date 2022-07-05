import tkinter as tk
import tkinter.ttk as ttk
from TableFactory import TableFactory
from Enums import TableTypeEnums
from DAO_File import FileDaoClass
from Menubar import MenuBar
from Table_using_Widgets import TableUsingWidgets

class MainForm(tk.Tk):
    

    def __init__(self):
        # bgColor ="#E5E8E8"

        self.db = FileDaoClass()
        # self.db.setFilePath("empty_db.json")
        self.db.setFilePath("db.json")
        self.db.loadDataSource()
        
        tk.Tk.__init__(self)
        self.title('Family Relm Information')
        self.geometry('720x400')

        self.menubar =  MenuBar(self)     
        self.show_custom_field = False

        self.create_BaseFrame()
        self.create_Labels()
        self.create_TextBoxes()
        self.create_Buttons()

        # self.table = TableFactory.createTable(TableTypeEnums.UsingTreeView, self.baseFrame)
        # self.table = TableFactory.createTable(TableTypeEnums.UsingWidget, self.baseFrame)
        self.create_ComboBoxes()
        # self.create_table()
        self.config(menu=self.menubar.menubar)
        style = ttk.Style()
        style.theme_use('clam')

        # This line is needed to call check_for_selection function every 100 ms
        self.after(100, self.check_for_selection)
        self.after(100, self.CheckSelectedMember)


    def create_BaseFrame(self):
        bgColor="#5D6D7E"
        s = ttk.Style()
        s.configure('My.TFrame', background=bgColor)
        self.baseFrame = ttk.Frame(self, height=700, width=900, style='My.TFrame')
        self.baseFrame.grid(padx=25, pady=25)


    def create_Labels(self):
        self.unameLbl = ttk.Label(self.baseFrame, text="Name", width=15)
        self.unameLbl.grid(row=0, column=0, padx=10, pady=10)


    def create_TextBoxes(self):
        self.unameTxt = ttk.Entry(self.baseFrame, width=25)
        self.unameTxt.grid(row = 0, column=1, padx=10, pady=10, ipady=5)
        self.unameTxt.insert(tk.END, "")
        # self.unameTxt.bind('<Double-Button-1>', self.doubleClickHandler)
        # self.unameTxt.config(state=tk.DISABLED)
        

    def doubleClickHandler(self, event):      
        if (self.unameTxt['state'] == tk.NORMAL):
            self.unameTxt['state'] = tk.DISABLED
        else:
            self.unameTxt['state'] = tk.NORMAL
        print(self.unameTxt['state'])


    def create_Buttons(self):
        self.saveBtn = ttk.Button(self.baseFrame, text="Save", width=25, command=self.addNewItem)
        self.saveBtn.grid(row=0, column=2, padx=10, pady=10)


    def addNewItem(self):
        value = self.unameTxt.get()
        if value == "":
            return
        # self.selections['values'] = tuple(list(self.selections['values']).append(value))
        temp = list(self.selections['values'])
        temp.append(value)
        self.selections['values'] = temp
        self.unameTxt.delete(0, tk.END)


    def create_ComboBoxes(self):
        self.selections = ttk.Combobox(self.baseFrame, width=25)
        # self.selections['values'] = ['Select Item', 'Add New Entry', 'Apples', 'Oranges', 'Blueberries', 'Bananas']
        self.selections['values'] = ['Select Item', 'Add New Entry']
        self.selections.current(0)
        self.selections.grid(row=0, column=3, ipadx=10, ipady=5)
        self.selections['state'] = "readonly"

        self.membersList = ttk.Combobox(self.baseFrame, width=25)
        memberMetaData = self.db.getDataSourceDump()
        if (len(memberMetaData) == 0):
            self.membersList['values'] = ['No Member Added']
        else:
            self.membersList['values'] = ['Select Member Name']
        for memberInfo in memberMetaData:
            print(memberInfo)
            print(memberMetaData[memberInfo]['MemberName'])
            self.membersList["values"] = tuple(list(self.membersList['values']) + [memberMetaData[memberInfo]['MemberName']])
        self.membersList.current(0)
        self.membersList.grid(row=1, columnspan=4, ipadx=25, ipady=5)
        self.membersList['state'] = "readonly"
    
    
    def check_for_selection(self):
        value = self.selections.get()

        # If the value is equal to "Custom" and show_field is set to False
        if value == 'Add New Entry' and not self.show_custom_field:

            # Set show_field to True and pack() the custom entry field
            self.show_custom_field = True

            # Create a new window how we did when we made self.root
            self.new_window = tk.Tk()

            # Create the Entry that will go in the window. The previous Entry widget from line 16, can be removed
            self.custom_field = ttk.Entry(self.new_window)
            self.custom_field.pack()

            # Run the new window like we did the original
            self.new_window.mainloop()


        # If the value DOESNT equal "Custom"
        elif value != 'Custom':

            # Destroy the new window that was created if it exists
            if self.show_custom_field:
                self.new_window.destroy()

            # Set show_field to False
            self.show_custom_field = False

        # If the value IS "Custom" and we're showing the custom_feild
        elif value == 'Custom' and self.show_custom_field:
            print('yes')


        # Call this method again to keep checking the selection box
        self.after(100, self.check_for_selection)


    def CheckSelectedMember(self):
        value = self.membersList.get()

        if value not in ['No Member Added', 'Select Member Name']:
            self.table = TableFactory.createTable(TableTypeEnums.UsingTreeView, self.baseFrame)
            self.table.loadAllDataInTable(0)

        # Call this method again to keep checking the selection box
        self.after(100, self.CheckSelectedMember)

