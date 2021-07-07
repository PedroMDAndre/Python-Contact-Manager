from tkinter import *
from translation import Translation
from windowsUtils import centrarJanela


def changeContactWindow(contactTree, contactoAntigo: list[str], contactoAlterado: list[str], lingua: Translation):
    def actFechar():
        changeContactWindow.destroy()
        contactTree.master.attributes('-disabled', False)

    def actAlterar():
        contactoAlterado[0] = enome.get()
        contactoAlterado[1] = etelefone.get()
        contactoAlterado[2] = etelemovel.get()
        contactoAlterado[3] = eemail.get()
        contactTree.alterarContacto(contactoAntigo, contactoAlterado)

        actFechar()

    contactTree.master.attributes('-disabled', True)
    changeContactWindow = Tk()
    changeContactWindow.protocol("WM_DELETE_WINDOW", actFechar)

    changeContactWindow.resizable(False, False)

    # Labels
    lnome = Label(changeContactWindow, text=lingua.traducao("name"))
    ltelefone = Label(changeContactWindow, text=lingua.traducao("phone"))
    ltelemovel = Label(changeContactWindow, text=lingua.traducao("mobile"))
    lemail = Label(changeContactWindow, text=lingua.traducao("email"))

    # Entries
    enome = Entry(changeContactWindow, width=30)
    etelefone = Entry(changeContactWindow, width=30)
    etelemovel = Entry(changeContactWindow, width=30)
    eemail = Entry(changeContactWindow, width=30)

    changeEntry(contactoAlterado[0], enome)
    changeEntry(contactoAlterado[1], etelefone)
    changeEntry(contactoAlterado[2], etelemovel)
    changeEntry(contactoAlterado[3], eemail)

    # Buttons
    bcancelar = Button(changeContactWindow, text=lingua.traducao("cancel"), command=actFechar, width=8)
    balterar = Button(changeContactWindow, text=lingua.traducao("change"), command=actAlterar, width=8)

    # Layout
    lnome.grid(row=0, column=0, padx=20, pady=10, sticky=W)
    ltelefone.grid(row=1, column=0, padx=20, pady=10, sticky=W)
    ltelemovel.grid(row=2, column=0, padx=20, pady=10, sticky=W)
    lemail.grid(row=3, column=0, padx=20, pady=10, sticky=W)

    enome.grid(row=0, column=1, padx=20, pady=10)
    etelefone.grid(row=1, column=1, padx=20, pady=10)
    etelemovel.grid(row=2, column=1, padx=20, pady=10)
    eemail.grid(row=3, column=1, padx=20, pady=10)
    bcancelar.grid(row=4, column=0, padx=20, pady=10)
    balterar.grid(row=4, column=1, padx=20, pady=10)

    changeContactWindow.grid()
    changeContactWindow.title(lingua.traducao("change"))
    changeContactWindow.geometry(centrarJanela(330, 210, changeContactWindow))
    changeContactWindow.mainloop()


def changeEntry(texto: str, entry: Entry):
    entry.delete(0, END)
    entry.insert(0, texto)
