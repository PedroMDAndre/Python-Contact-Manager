from tkinter import *


def main():
    screen = MainScreen()
    screen.mainloop()


class MainScreen(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("Gestor de contactos")
        self.dados = Frame()
        self.label1 = Label(self.dados, text="sdsdf")
        self.toolbar = ToolBar(self.label1)
        self.toolbar.grid(row=0, column=0)


        self.label1.grid(row=1, column=0)

        self.dados.grid(row=1, column=0)


class ToolBar(Frame):
    def __init__(self, screen):
        Frame.__init__(self)
        self.screen=screen
        self.grid()
        self.icon = PhotoImage(file="contact.png")

        self.bt1 = toolBarBtn(self, "Adicionar contacto", self.icon, addContactWindow)
        self.bt2 = toolBarBtn(self, "Remover contacto", self.icon)
        self.bt3 = toolBarBtn(self, "Ordenar Cres./Decres.", self.icon)
        self.bt4 = toolBarBtn(self, "Procurar", self.icon)
        self.bt5 = toolBarBtn(self, "Todas as entradas", self.icon)
        self.bt6 = toolBarBtn(self, "Mudar de língua", self.icon)
        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=LEFT)
        self.bt3.pack(side=LEFT)
        self.bt4.pack(side=LEFT)
        self.bt5.pack(side=LEFT)
        self.bt6.pack(side=LEFT)
    def fechar(self):
        print("aqui")
        self.screen["text"]="2"

    # Lista de funcionalidades
    # adicionar nome
    # adicionar icon
    # fixar tamanho
    # fazer painel de icons
    # adicionar contacto
    # remover contacto
    # sort
    # search / reset
    # mudar língua
    # ler contactos de ficheiro
    # ver detalhes / alterar


def addContactWindow():
    AddContactWindow = Tk()
    lnome = Label(AddContactWindow, text="Nome")
    ltelefone = Label(AddContactWindow, text="Nome")
    ltelemovel = Label(AddContactWindow, text="Nome")
    lemail = Label(AddContactWindow, text="Nome")
    AddContactWindow.grid()
    AddContactWindow.mainloop()



def toolBarBtn(master, text, icon, command=""):
    return Button(master, text=text, image=icon, width=150, compound="top", command=command,
                  bg="white",
                  border=0)


if __name__ == '__main__':
    main()