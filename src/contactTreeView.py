from tkinter import *
from tkinter import ttk
from translation import Translation
import contactsIO
from auxWindows import changeContactWindow


class ContactTreeView(Frame):
    def __init__(self, contacts, lingua: Translation):
        Frame.__init__(self)
        self.frameTop = Frame(self)
        self.frameBottom = Frame(self)

        self.contacts: list[list[str]] = contacts
        self.filteredContacts = []
        self.lingua = lingua
        self.style = ttk.Style()
        self.nomeOrdenarCrescente = True

        self.frameTop.pack(side=TOP, fill=BOTH, expand=YES)
        self.frameBottom.pack(side=BOTTOM, fill=X)

        # columns
        self.columns = ('#1', '#2', '#3', '#4')

        self.tree = ttk.Treeview(self.frameTop,
                                 columns=self.columns,
                                 show='headings',
                                 selectmode="browse",
                                 style="mystyle.Treeview")
        self.tree.bind("<Double-1>", self.onDoubleClick)

        # definir headings
        self.definirHeadings()

        # adding data to the treeview
        # construct filtered/sorted array
        for contact in self.contacts:
            self.tree.insert('', END, values=contact)
            self.filteredContacts.append(contact)

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
            self.filteredContacts.sort()
            self.filteredContacts.reverse()
            self.nomeOrdenarCrescente = True

        self.mostrarResultado()

    def removerContacto(self):
        if len(self.tree.selection()) > 0:
            selectedItem = self.tree.selection()[0]
            contacto = self.tree.item(selectedItem)["values"]
            # eliminar contacto da lista de contactos
            self.removerEntradaNaLista(contacto, self.contacts)
            # eliminar contacto da lista de filtro
            self.removerEntradaNaLista(contacto, self.filteredContacts)
            # apresentar resultado
            self.mostrarResultado()

    def removerEntradaNaLista(self, entrada, lista: list[any]):
        tokenProcurar = ""
        for elemento in entrada:
            tokenProcurar += str(elemento)

        contactoRemover = []
        for a, contacto in enumerate(lista):
            token = "".join(contacto)
            if tokenProcurar.lower() == token.lower():
                contactoRemover = contacto
                break

        if contactoRemover in lista:
            lista.remove(contactoRemover)

    def onDoubleClick(self, event):
        selectedItem = self.tree.selection()[0]
        contactoAntigo = self.tree.item(selectedItem)["values"]
        contactoAlterado = self.tree.item(selectedItem)["values"]
        print(contactoAntigo)

        changeContactWindow(self, contactoAntigo, contactoAlterado, self.lingua)

    def alterarContacto(self, contactoAntigo, contactoAlterado):
        print(contactoAntigo)
        print(contactoAlterado)
        if contactoAlterado != contactoAntigo:
            print("aqui")
            self.removerContacto()
            self.contacts.append(contactoAlterado)
            self.filteredContacts.append(contactoAlterado)
            contactsIO.saveContactsData(self.contacts)
            self.mostrarResultado()
