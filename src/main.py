from tkinter import *
import contactsIO
from translation import Translation
import contactTreeView
from contactTreeView import ContactTreeView


def main():
    contactos = contactsIO.loadContactsData()
    screen = MainScreen(contactos)
    screen.mainloop()


class MainScreen(Frame):
    def __init__(self, contactos):
        Frame.__init__(self)
        self.lingua = Translation()
        self.contactos = contactos
        self.dadosFrame: ContactTreeView = ContactTreeView(contactos, self.lingua)

        self.toolbar: Frame = ToolBar(self, self.contactos, self.lingua)

        self.toolbar.grid(row=0, column=0, sticky='we')
        self.dadosFrame.grid(row=1, column=0, sticky='we')
        self.configMainScreen()

    def configMainScreen(self):
        self.master.title("Gestor de contactos")
        self.master.geometry("800x600")
        self.grid()
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
                              lambda: addContactWindow(self.contactos, self.lingua))
        self.bt2 = toolBarBtn(self, lingua.traducao("remove_contact"), self.iconRemove)
        self.bt3 = toolBarBtn(self, lingua.traducao("sort_contacts"), self.iconSort)
        self.bt4 = toolBarBtn(self, lingua.traducao("find_contacts"), self.iconFind)
        self.bt5 = toolBarBtn(self, lingua.traducao("show_all_entries"), self.iconAll)
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

    def mudarLingua(self):
        self.lingua.trocarLingua()
        self.definirTextoButoes()
        self.mainFrame.dadosFrame.definirHeadings()

    # Lista de funcionalidades
    # adicionar nome
    # fixar tamanho
    # remover contacto
    # sort
    # search / reset
    # ler contactos de ficheiro
    # ver detalhes / alterar


def addContactWindow(contactos: list[list[str]], lingua: Translation):
    def actFechar():
        AddContactWindow.destroy()

    def actAdicionar():
        contacto: list[str] = [
            enome.get(),
            etelefone.get(),
            etelemovel.get(),
            eemail.get()]
        contactos.append(contacto)
        contactsIO.saveContactsData(contactos)
        print(contacto)
        actFechar()

    AddContactWindow = Tk()
    lnome = Label(AddContactWindow, text=lingua.traducao("name"))
    ltelefone = Label(AddContactWindow, text=lingua.traducao("phone"))
    ltelemovel = Label(AddContactWindow, text=lingua.traducao("mobile"))
    lemail = Label(AddContactWindow, text=lingua.traducao("email"))

    enome = Entry(AddContactWindow)
    etelefone = Entry(AddContactWindow)
    etelemovel = Entry(AddContactWindow)
    eemail = Entry(AddContactWindow)

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


def toolBarBtn(master, text, icon, command=""):
    return Button(master, text=text, image=icon,
                  width=100, height=60,
                  compound="top", command=command,
                  bg="white",
                  border=0)


def createDadosFrame(contactos: list[list[str]]) -> Frame:
    dadosFrame = Frame()

    lbContactos = Listbox(dadosFrame)
    lbContactos.pack()

    for contacto in contactos:
        lbContactos.insert(END, contacto[0])

    return dadosFrame


if __name__ == '__main__':
    main()
