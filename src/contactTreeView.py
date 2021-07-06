from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from translation import Translation


class ContactTreeView(Frame):
    def __init__(self, contacts, lingua: Translation):
        Frame.__init__(self)
        self.frameTop = Frame(self)
        self.frameBottom = Frame(self)
        self.contacts = contacts
        self.filteredContacts = []
        self.lingua = lingua
        self.style = ttk.Style()
        self.nomeOrdenarCrescente = True

        self.frameTop.pack(side=TOP, fill=BOTH, expand=YES)
        self.frameBottom.pack(side=BOTTOM, fill=X)

        # columns
        self.columns = ('#1', '#2', '#3', '#4')

        self.tree = ttk.Treeview(self.frameTop, columns=self.columns, show='headings', style="mystyle.Treeview")

        # definir headings
        self.definirHeadings()

        # adding data to the treeview
        # construct filtered/sorted array

        for contact in self.contacts:
            self.tree.insert('', END, values=contact)
            self.filteredContacts.append(contact)

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

        self.tree.pack(side=LEFT, fill=BOTH, expand=YES)

        self.formatarTreeView()
        self.adicionarScrollbars()

    def definirHeadings(self):
        self.tree.heading('#1', text=self.lingua.traducao("name"), anchor=W)
        self.tree.heading('#2', text=self.lingua.traducao("phone"), anchor=W)
        self.tree.heading('#3', text=self.lingua.traducao("mobile"), anchor=W)
        self.tree.heading('#4', text=self.lingua.traducao("email"), anchor=W)

    def adicionarScrollbars(self):
        self.scrollbary = ttk.Scrollbar(self.frameTop, orient=VERTICAL, command=self.tree.yview)
        self.scrollbarx = ttk.Scrollbar(self.frameBottom, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=self.scrollbary.set)
        self.tree.configure(xscroll=self.scrollbarx.set)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.pack(fill=X)

    def formatarTreeView(self):
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                             font=('Calibri', 10))  # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 10, 'bold'),
                             anchor=LEFT)  # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

    def mostrarResultado(self):
        self.tree.delete(*self.tree.get_children())
        for contact in self.filteredContacts:
            self.tree.insert('', END, values=contact)

    def ordenarPeloNome(self):
        if self.nomeOrdenarCrescente:
            self.filteredContacts.sort()
            self.nomeOrdenarCrescente = False
        else:
            self.filteredContacts.reverse()
            self.nomeOrdenarCrescente = True

        self.mostrarResultado()
