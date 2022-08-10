"""
Janelas para usar no GueWy - Sem uso por enquanto
"""
import tkinter as tk

class Janela:
    """
    Janelas do programa
    """

    root = tk.Tk()

    window_width = 300
    window_height = 200

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.title('GueWy - Jogo da Forca')
    root.iconbitmap('.entities/img/icone.ico')

    root.mainloop()

def fecharjanela(root):
    """
    Função pra fechar janela
    """
    return root.withdraw()
