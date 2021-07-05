from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import contactsIO
from translation import Translation


class ContactTreeView(Frame):
    def __init__(self, contacts, lingua: Translation):
        Frame.__init__(self)
        self.lingua = lingua

        # columns
        self.columns = ('#1', '#2', '#3', '#4')

        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')

        # definir headings
        self.definirHeadings()

        # adding data to the treeview
        for contact in contacts:
            self.tree.insert('', END, values=contact)

        # bind the select event
        def item_selected(event):
            for selected_item in self.tree.selection():
                # dictionary
                item = self.tree.item(selected_item)
                # list
                record = item['values']
                print(record)
                #
                showinfo(title='Information',
                         message=record[1])

        self.tree.bind('<<TreeviewSelect>>', item_selected)

        self.tree.grid()

        # add a scrollbar
        self.scrollbary = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.scrollbarx = ttk.Scrollbar(self, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=self.scrollbary.set)
        self.tree.configure(xscroll=self.scrollbarx.set)
        self.scrollbary.grid(row=0, column=1, sticky='ns')
        self.scrollbarx.grid(row=1, column=0, sticky='we')

    def definirHeadings(self):
        self.tree.heading('#1', text=self.lingua.traducao("name"))
        self.tree.heading('#2', text=self.lingua.traducao("phone"))
        self.tree.heading('#3', text=self.lingua.traducao("mobile"))
        self.tree.heading('#4', text=self.lingua.traducao("email"))
