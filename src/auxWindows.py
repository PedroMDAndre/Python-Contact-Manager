from tkinter import *
import contactsIO
from translation import Translation
from windowsUtils import centrarJanela
from main import MainScreen


def changeContactWindow(mainFrame: MainScreen, contactoAlterado: list[str], lingua: Translation):
    def actFechar():
        changeContactWindow.destroy()
        mainFrame.master.attributes('-disabled', False)

    def actAlterar():


        actFechar()

    mainFrame.master.attributes('-disabled', True)
    changeContactWindow = Tk()
    changeContactWindow.protocol("WM_DELETE_WINDOW", actFechar)

    changeContactWindow.resizable(False, False)

    lnome = Label(changeContactWindow, text=lingua.traducao("name"))
    ltelefone = Label(changeContactWindow, text=lingua.traducao("phone"))
    ltelemovel = Label(changeContactWindow, text=lingua.traducao("mobile"))
    lemail = Label(changeContactWindow, text=lingua.traducao("email"))

    enomeText = StringVar(value=contactoAlterado[0])
    etelefoneText = StringVar(value=contactoAlterado[0])
    etelemovelText = StringVar(value=contactoAlterado[0])
    eemailText = StringVar(value=contactoAlterado[0])

    enome = Entry(changeContactWindow, width=30)
    etelefone = Entry(changeContactWindow, width=30)
    etelemovel = Entry(changeContactWindow, width=30)
    eemail = Entry(changeContactWindow, width=30)

    bcancelar = Button(changeContactWindow, text=lingua.traducao("cancel"), command=actFechar, width=8)
    balterar = Button(changeContactWindow, text=lingua.traducao("add"), command=actAlterar, width=8)

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
    changeContactWindow.title(lingua.traducao("add_contact_title"))
    changeContactWindow.geometry(centrarJanela(330, 210, changeContactWindow))
    changeContactWindow.mainloop()
