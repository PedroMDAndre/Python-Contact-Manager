from tkinter import *
import contactsIO
from translation import Translation


def main():
    contactos = contactsIO.loadContactsData()
    screen = MainScreen(contactos)
    screen.mainloop()


class MainScreen(Frame):
    def __init__(self, contactos):
        Frame.__init__(self)
        self.grid()
        self.lingua = Translation()
        self.contactos = contactos
        self.master.title("Gestor de contactos")
        self.dados = Frame()
        self.label1 = Label(self.dados, text="sdsdf")
        self.toolbar = ToolBar(self.label1, self.contactos, self.lingua)
        self.toolbar.grid(row=0, column=0)

        self.label1.grid(row=1, column=0)

        self.dados.grid(row=1, column=0)


class ToolBar(Frame):
    def __init__(self, screen, contactos, lingua: Translation):
        Frame.__init__(self)
        self.screen = screen
        self.contactos = contactos
        self.grid()
        self.icon = PhotoImage(file="../icons/contact.png")

        self.bt1 = toolBarBtn(self, lingua.traducao("add_contact"), self.icon, lambda: addContactWindow(self.contactos))
        self.bt2 = toolBarBtn(self, lingua.traducao("remove_contact"), self.icon)
        self.bt3 = toolBarBtn(self, lingua.traducao("sort_contacts"), self.icon)
        self.bt4 = toolBarBtn(self, lingua.traducao("find_contacts"), self.icon)
        self.bt5 = toolBarBtn(self, lingua.traducao("show_all_entries"), self.icon)
        self.bt6 = toolBarBtn(self, lingua.traducao("change_language"), self.icon)
        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=LEFT)
        self.bt3.pack(side=LEFT)
        self.bt4.pack(side=LEFT)
        self.bt5.pack(side=LEFT)
        self.bt6.pack(side=LEFT)

    def fechar(self):
        print("aqui")
        self.screen["text"] = "2"

    def mudarLingua(self):
        return

    # Lista de funcionalidades
    # adicionar nome
    # adicionar icon
    # fixar tamanho
    # fazer painel de icons
    # remover contacto
    # sort
    # search / reset
    # mudar língua
    # ler contactos de ficheiro
    # ver detalhes / alterar


def addContactWindow(contactos: list[list[str]]):
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
    lnome = Label(AddContactWindow, text="Nome")
    ltelefone = Label(AddContactWindow, text="Telefone")
    ltelemovel = Label(AddContactWindow, text="Telemóvel")
    lemail = Label(AddContactWindow, text="E-mail")

    enome = Entry(AddContactWindow)
    etelefone = Entry(AddContactWindow)
    etelemovel = Entry(AddContactWindow)
    eemail = Entry(AddContactWindow)

    bcancelar = Button(AddContactWindow, text="Cancelar", command=actFechar)
    badicionar = Button(AddContactWindow, text="Adicionar", command=actAdicionar)

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
    return Button(master, text=text, image=icon, width=150, compound="top", command=command,
                  bg="white",
                  border=0)


if __name__ == '__main__':
    main()
