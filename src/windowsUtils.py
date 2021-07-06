from tkinter import Tk


def centrarJanela(window_width: int, window_height: int, janela: Tk):
    '''
    Devolve a string a utilizar no método Tk().geometry()
    '''
    # Screen size
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    # Window position
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    return f"{window_width}x{window_height}+{x_position}+{y_position}"
