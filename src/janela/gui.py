# pylint: disable=C0103,C0114,C0115,C0116
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1366x768")
window.configure(bg = "#090808")
window.title('GueWy - Jogo da Forca')
window.iconbitmap('assets\\icone.ico')

canvas = Canvas(
    window,
    bg = "#090808",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    243.0,
    119.0,
    1123.0,
    648.0,
    fill="#080808",
    outline="")

canvas.create_text(
    494.35107421875,
    15.600006103515625,
    anchor="nw",
    text="GueWy",
    fill="#362B01",
    font=("IrishGrover Regular", 64 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    682.5,
    726.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=312.0,
    y=700.0,
    width=741.0,
    height=50.0
)

window.resizable(False, False)
window.mainloop()