from tkinter import *
import contactsIO
from translation import Translation
from contactTreeView import ContactTreeView
from tkinter.messagebox import showinfo


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
        self.dadosFrame: ContactTreeView = ContactTreeView(contactos, self.lingua)
        self.toolbar: Frame = ToolBar(self, self.contactos, self.lingua)

        # Configurar Janela Principal
        self.configMainScreen()

    def configMainScreen(self):
        self.master.title("Gestor de contactos")
        self.master.geometry("900x600")
        self.master.resizable(False, False)
        self.toolbar.pack(side=TOP, fill=BOTH)
        self.dadosFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.pack()
        return


class ToolBar(Frame):
    def __init__(self, mainFrame: MainScreen, contactos, lingua: Translation):
        Frame.__init__(self, bg="white")

        self.contactos = contactos
        self.lingua = lingua
        self.pack()
        self.mainFrame = mainFrame

        # Icons dos Butões
        self.iconAdd = PhotoImage(file="../icons/add.png")
        self.iconRemove = PhotoImage(file="../icons/remove.png")
        self.iconSort = PhotoImage(file="../icons/sort.png")
        self.iconFind = PhotoImage(file="../icons/find.png")
        self.iconAll = PhotoImage(file="../icons/all.png")
        self.iconLanguage = PhotoImage(file="../icons/language.png")

        self.bt1 = toolBarBtn(self, lingua.traducao("add_contact"), self.iconAdd,
                              lambda: addContactWindow(self.mainFrame, self.contactos, self.lingua))
        self.bt2 = toolBarBtn(self, lingua.traducao("remove_contact"), self.iconRemove,
                              self.removerContacto)
        self.bt3 = toolBarBtn(self, lingua.traducao("sort_contacts"), self.iconSort,
                              self.ordenarPeloNome)
        self.bt4 = toolBarBtn(self, lingua.traducao("find_contacts"), self.iconFind,
                              lambda: findContactWindow(self.mainFrame, self.contactos, self.lingua))
        self.bt5 = toolBarBtn(self, lingua.traducao("show_all_entries"), self.iconAll,
                              self.mostrarTodosContactos)
        self.bt6 = toolBarBtn(self, lingua.traducao("change_language"), self.iconLanguage,
                              self.mudarLingua)
        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=LEFT)
        self.bt3.pack(side=LEFT)
        self.bt4.pack(side=LEFT)
        self.bt5.pack(side=LEFT)
        self.bt6.pack(side=LEFT)

    def definirTextoButoes(self):
        self.bt1["text"] = self.lingua.traducao("add_contact")
        self.bt2["text"] = self.lingua.traducao("remove_contact")
        self.bt3["text"] = self.lingua.traducao("sort_contacts")
        self.bt4["text"] = self.lingua.traducao("find_contacts")
        self.bt5["text"] = self.lingua.traducao("show_all_entries")
        self.bt6["text"] = self.lingua.traducao("change_language")

    def removerContacto(self):
        #Perguntar se tem a certeza de que deseja eliminar o contacto
        self.mainFrame.dadosFrame.removerContacto()
        contactsIO.saveContactsData(self.contactos)

    def mudarLingua(self):
        self.lingua.trocarLingua()
        self.definirTextoButoes()
        self.mainFrame.dadosFrame.definirHeadings()

    def mostrarTodosContactos(self):
        self.mainFrame.dadosFrame.filteredContacts = self.contactos
        self.mainFrame.dadosFrame.mostrarResultado()

    def ordenarPeloNome(self):
        self.mainFrame.dadosFrame.ordenarPeloNome()

    # Lista de funcionalidades
    # remover contacto
    # sort
    # ver alterar


def addContactWindow(mainFrame: MainScreen, contactos: list[list[str]], lingua: Translation):
    def actFechar():
        AddContactWindow.destroy()
        mainFrame.master.attributes('-disabled', False)

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

    mainFrame.master.attributes('-disabled', True)
    AddContactWindow = Tk()
    AddContactWindow.protocol("WM_DELETE_WINDOW", actFechar)

    AddContactWindow.resizable(False, False)

    lnome = Label(AddContactWindow, text=lingua.traducao("name"))
    ltelefone = Label(AddContactWindow, text=lingua.traducao("phone"))
    ltelemovel = Label(AddContactWindow, text=lingua.traducao("mobile"))
    lemail = Label(AddContactWindow, text=lingua.traducao("email"))

    enome = Entry(AddContactWindow, width=30)
    etelefone = Entry(AddContactWindow, width=30)
    etelemovel = Entry(AddContactWindow, width=30)
    eemail = Entry(AddContactWindow, width=30)

    bcancelar = Button(AddContactWindow, text=lingua.traducao("cancel"), command=actFechar)
    badicionar = Button(AddContactWindow, text=lingua.traducao("add"), command=actAdicionar)

    lnome.grid(row=0, column=0, padx=20, pady=10, sticky=W)
    ltelefone.grid(row=1, column=0, padx=20, pady=10, sticky=W)
    ltelemovel.grid(row=2, column=0, padx=20, pady=10, sticky=W)
    lemail.grid(row=3, column=0, padx=20, pady=10, sticky=W)

    enome.grid(row=0, column=1, padx=20, pady=10)
    etelefone.grid(row=1, column=1, padx=20, pady=10)
    etelemovel.grid(row=2, column=1, padx=20, pady=10)
    eemail.grid(row=3, column=1, padx=20, pady=10)
    bcancelar.grid(row=4, column=0, padx=20, pady=10)
    badicionar.grid(row=4, column=1, padx=20, pady=10)

    AddContactWindow.grid()
    AddContactWindow.mainloop()


def findContactWindow(mainFrame: MainScreen, contactos: list[list[str]], lingua: Translation):
    def actFechar():
        findContactWindow.destroy()
        mainFrame.master.attributes('-disabled', False)

    def actProcurar():
        strProcurar= eprocurar.get().lower()
        result = []
        for contacto in contactos:
            token = "".join(contacto).lower()
            if strProcurar in token:
                result.append(contacto)
        mainFrame.dadosFrame.filteredContacts = result
        mainFrame.dadosFrame.mostrarResultado()

        actFechar()

    mainFrame.master.attributes('-disabled', True)
    findContactWindow = Tk()
    findContactWindow.protocol("WM_DELETE_WINDOW", actFechar)

    findContactWindow.resizable(False, False)

    lprocurar = Label(findContactWindow, text=lingua.traducao("find_contacts"))

    eprocurar = Entry(findContactWindow, width=30)

    bcancelar = Button(findContactWindow, text=lingua.traducao("cancel"), command=actFechar)
    bprocurar = Button(findContactWindow, text=lingua.traducao("find_contacts"), command=actProcurar)

    lprocurar.grid(row=0, column=0, padx=20, pady=10, sticky=W)


    eprocurar.grid(row=0, column=1, padx=20, pady=10)

    bcancelar.grid(row=4, column=0, padx=20, pady=10)
    bprocurar.grid(row=4, column=1, padx=20, pady=10)

    findContactWindow.grid()
    findContactWindow.mainloop()


def toolBarBtn(master, text, icon, command=""):
    return Button(master, text=text, image=icon,
                  width=100, height=60,
                  compound="top", command=command,
                  bg="white",
                  border=0)


if __name__ == '__main__':
    main()
