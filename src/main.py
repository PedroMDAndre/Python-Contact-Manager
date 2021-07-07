from tkinter import *
import contactsIO
from translation import Translation
from contactTreeView import ContactTreeView
from windowsUtils import centrarJanela
from tkinter import messagebox as msgBox


def main():
    contactos = contactsIO.loadContactsData()
    screen = MainScreen(contactos)
    screen.mainloop()


class MainScreen(Frame):
    def __init__(self, contactos):
        # Iniciar atributos
        Frame.__init__(self)
        self.lingua = Translation()
        self.contactos = contactos
        self.dadosFrame: ContactTreeView = ContactTreeView(self.contactos, self.lingua)
        self.toolbar: Frame = ToolBar(self, self.contactos, self.lingua)

        # Configurar Janela Principal
        self.configMainScreen()

    def configMainScreen(self):
        self.master.title("Gestor de contactos")
        self.master.geometry(centrarJanela(900, 600, self))
        self.master.resizable(False, False)
        self.master.iconbitmap("../icons/app.ico")
        self.toolbar.pack(side=TOP, fill=BOTH)
        self.dadosFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.pack()


class ToolBar(Frame):
    def __init__(self, mainFrame: MainScreen, contactos, lingua: Translation):
        # Iniciar Janela
        Frame.__init__(self, bg="white")
        self.contactos = contactos
        self.lingua = lingua
        self.pack()
        self.mainFrame = mainFrame

        # Icons dos Botões
        self.iconAdd = PhotoImage(file="../icons/add.png")
        self.iconRemove = PhotoImage(file="../icons/remove.png")
        self.iconSort = PhotoImage(file="../icons/sort.png")
        self.iconFind = PhotoImage(file="../icons/find.png")
        self.iconAll = PhotoImage(file="../icons/all.png")
        self.iconLanguage = PhotoImage(file="../icons/language.png")

        self.btAddContact = toolBarBtn(self, lingua.traducao("add_contact"), self.iconAdd,
                                       lambda: addContactWindow(self.mainFrame, self.contactos, self.lingua))
        self.btRemoveContact = toolBarBtn(self, lingua.traducao("remove_contact"), self.iconRemove,
                                          self.removerContacto)
        self.btSortContacts = toolBarBtn(self, lingua.traducao("sort_contacts"), self.iconSort,
                                         self.ordenarPeloNome)
        self.btFindContacts = toolBarBtn(self, lingua.traducao("find_contacts"), self.iconFind,
                                         lambda: findContactWindow(self.mainFrame, self.contactos, self.lingua))
        self.btAllEntries = toolBarBtn(self, lingua.traducao("show_all_entries"), self.iconAll,
                                       self.mostrarTodosContactos)
        self.btChangeLanguage = toolBarBtn(self, lingua.traducao("change_language"), self.iconLanguage,
                                           self.mudarLingua)

        # Layout
        self.btAddContact.pack(side=LEFT)
        self.btRemoveContact.pack(side=LEFT)
        self.btSortContacts.pack(side=LEFT)
        self.btFindContacts.pack(side=LEFT)
        self.btAllEntries.pack(side=LEFT)
        self.btChangeLanguage.pack(side=LEFT)

    def definirTextoBotoes(self):
        self.btAddContact["text"] = self.lingua.traducao("add_contact")
        self.btRemoveContact["text"] = self.lingua.traducao("remove_contact")
        self.btSortContacts["text"] = self.lingua.traducao("sort_contacts")
        self.btFindContacts["text"] = self.lingua.traducao("find_contacts")
        self.btAllEntries["text"] = self.lingua.traducao("show_all_entries")
        self.btChangeLanguage["text"] = self.lingua.traducao("change_language")

    def removerContacto(self):
        # Perguntar se tem a certeza de que deseja eliminar o contacto
        choice = msgBox.askyesno(title="", message=self.lingua.traducao("msg_confirm_remove"))

        if choice:
            self.mainFrame.dadosFrame.removerContacto()
            contactsIO.saveContactsData(self.contactos)

    def mudarLingua(self):
        self.lingua.trocarLingua()
        self.definirTextoBotoes()
        self.mainFrame.dadosFrame.definirHeadings()

    def mostrarTodosContactos(self):
        self.mainFrame.dadosFrame.filteredContacts = self.contactos
        self.mainFrame.dadosFrame.mostrarResultado()

    def ordenarPeloNome(self):
        self.mainFrame.dadosFrame.ordenarPeloNome()


def addContactWindow(mainFrame: MainScreen, contactos: list[list[str]], lingua: Translation):
    def actFechar():
        AddContactWindow.destroy()
        mainFrame.master.attributes('-disabled', False)
        mainFrame.focus_force()

    def actAdicionar():
        contacto: list[str] = [
            enome.get(),
            etelefone.get(),
            etelemovel.get(),
            eemail.get()]
        contactos.append(contacto)
        contactsIO.saveContactsData(contactos)
        mainFrame.dadosFrame.tree.insert('', END, values=contacto)

        actFechar()

    # Iniciar Janela
    mainFrame.master.attributes('-disabled', True)
    AddContactWindow = Tk()
    AddContactWindow.after(1, lambda: AddContactWindow.focus_force())
    AddContactWindow.protocol("WM_DELETE_WINDOW", actFechar)
    AddContactWindow.bind('<Return>', (lambda event: actAdicionar()))

    AddContactWindow.resizable(False, False)

    # Labels
    lnome = Label(AddContactWindow, text=lingua.traducao("name"))
    ltelefone = Label(AddContactWindow, text=lingua.traducao("phone"))
    ltelemovel = Label(AddContactWindow, text=lingua.traducao("mobile"))
    lemail = Label(AddContactWindow, text=lingua.traducao("email"))

    # Entries
    enome = Entry(AddContactWindow, width=30)
    etelefone = Entry(AddContactWindow, width=30)
    etelemovel = Entry(AddContactWindow, width=30)
    eemail = Entry(AddContactWindow, width=30)

    enome.focus()

    bcancelar = Button(AddContactWindow, text=lingua.traducao("cancel"), command=actFechar, width=8)
    badicionar = Button(AddContactWindow, text=lingua.traducao("add"), command=actAdicionar, width=8)

    # Labels
    lnome.grid(row=0, column=0, padx=20, pady=10, sticky=W)
    ltelefone.grid(row=1, column=0, padx=20, pady=10, sticky=W)
    ltelemovel.grid(row=2, column=0, padx=20, pady=10, sticky=W)
    lemail.grid(row=3, column=0, padx=20, pady=10, sticky=W)

    # Layout
    enome.grid(row=0, column=1, columnspan=2, padx=20, pady=10)
    etelefone.grid(row=1, column=1, columnspan=2, padx=20, pady=10)
    etelemovel.grid(row=2, column=1, columnspan=2, padx=20, pady=10)
    eemail.grid(row=3, column=1, columnspan=2, padx=20, pady=10)
    bcancelar.grid(row=4, column=1, padx=20, pady=10)
    badicionar.grid(row=4, column=2, padx=20, pady=10)

    AddContactWindow.grid()
    AddContactWindow.title(lingua.traducao("add_contact_title"))
    AddContactWindow.geometry(centrarJanela(330, 210, AddContactWindow))
    AddContactWindow.mainloop()


def findContactWindow(mainFrame: MainScreen, contactos: list[list[str]], lingua: Translation):
    def actFechar():
        findContactWindow.destroy()
        mainFrame.master.attributes('-disabled', False)
        mainFrame.focus_force()

    def actProcurar():
        strProcurar = eprocurar.get().lower()
        result = []
        for contacto in contactos:
            token = "".join(contacto).lower()
            if strProcurar in token:
                result.append(contacto)
        mainFrame.dadosFrame.filteredContacts = result
        mainFrame.dadosFrame.mostrarResultado()

        actFechar()

    # Iniciar Janela
    findContactWindow = Tk()
    findContactWindow.after(1, lambda: findContactWindow.focus_force())
    mainFrame.master.attributes('-disabled', True)

    findContactWindow.bind('<Return>', (lambda event: actProcurar()))
    findContactWindow.protocol("WM_DELETE_WINDOW", actFechar)

    findContactWindow.resizable(False, False)

    # Labels
    lprocurar = Label(findContactWindow, text=lingua.traducao("find_contacts"))

    # Entries
    eprocurar = Entry(findContactWindow, width=30)
    eprocurar.focus()

    # Buttons
    bcancelar = Button(findContactWindow, text=lingua.traducao("cancel"), command=actFechar, width=8)
    bprocurar = Button(findContactWindow, text=lingua.traducao("find_contacts"), command=actProcurar, width=8)

    # Layout
    lprocurar.grid(row=0, column=0, padx=20, pady=10, sticky=W)
    eprocurar.grid(row=0, column=1, columnspan=2, padx=20, pady=10)
    bcancelar.grid(row=4, column=1, padx=20, pady=10)
    bprocurar.grid(row=4, column=2, padx=20, pady=10)
    findContactWindow.grid()

    findContactWindow.title(lingua.traducao("find_contacts"))
    findContactWindow.geometry(centrarJanela(330, 90, findContactWindow))
    findContactWindow.mainloop()


def toolBarBtn(master, text, icon, command=""):
    return Button(master, text=text, image=icon,
                  width=100, height=60,
                  compound="top", command=command,
                  bg="white",
                  border=0)


if __name__ == '__main__':
    main()
