from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import contactsIO

def contactTreeView(frame: Frame):

    # columns
    columns = ('#1', '#2', '#3', '#4')

    tree = ttk.Treeview(frame, columns=columns, show='headings')

    # define headings
    tree.heading('#1', text='Name')
    tree.heading('#2', text='Phone')
    tree.heading('#3', text='Mobile')
    tree.heading('#4', text='Email')

    # generate sample data
    contacts: list[list[str]] = contactsIO.loadContactsData()

    # adding data to the treeview
    for contact in contacts:
        tree.insert('', END, values=contact)


    # bind the select event
    def item_selected(event):
        for selected_item in tree.selection():
            # dictionary
            item = tree.item(selected_item)
            # list
            record = item['values']
            print(record)
            #
            showinfo(title='Information',
                    message=record[1])


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid()

    # add a scrollbar
    scrollbary = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    scrollbarx = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscroll=scrollbary.set)
    tree.configure(xscroll=scrollbarx.set)
    scrollbary.grid(row=0, column=1, sticky='ns')
    scrollbarx.grid(row=1, column=0, sticky='we')

    return tree

if __name__ == '__main__':
    print()