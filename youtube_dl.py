import os

from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar

from pytube import YouTube
from pytube import *
import datetime
import calendar

import requests

from PIL import Image, ImageTk

cont_mp3 = []
cont_mp4_hd = []
cont_mp4_sd = []

# cores usadas ----------------
co0 = "#444466"  # preta
co1 = "#feffff"  # Branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
fundo = "#3b3b3b"
# -------------------------------
janela = Tk()

window_height = 500
window_width = 790

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (screen_height / 3))

janela.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

janela.title("Download Youtube")

janela.iconbitmap(r"images/you.ico")
janela.configure(bg=fundo)

# Dividindo a janela em dois
frame_cima = Frame(janela, width=500, height=110, bg=fundo, pady=5, padx=0)
frame_cima.grid(row=1, column=0)

frame_abaixo = Frame(janela, width=800, height=500, bg=fundo, pady=12, padx=0)
frame_abaixo.grid(row=2, column=0, sticky=NW)

frame3 = Frame(janela, bg=fundo)

# Configurando o frame_cima
logo = Image.open(r"images/youtube.png")
logo = logo.resize((50, 50), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(logo)

img_logo = Label(frame_cima, image=logo, compound=LEFT, bg=fundo, font=("Ivy 10 bold"), anchor="nw")
img_logo.place(x=95, y=15)

pesquisa = Image.open(r"images/pesquisa.png")
pesquisa = pesquisa.resize((35, 35), Image.Resampling.LANCZOS)
pesquisa = ImageTk.PhotoImage(pesquisa)

img_pesquisa = Label(
    frame_cima,
    image=pesquisa,
    compound=LEFT,
    bg=fundo,
    font=("Ivy 10 bold"),
    anchor="nw",
)
img_pesquisa.place(x=0, y=68)

img_nome = Label(
    frame_cima,
    text="Download Youtube",
    width=32,
    bg=fundo,
    fg=co1,
    font=("Ivy 15 bold"),
    anchor="nw",
)
img_nome.place(x=150, y=27)

# Fundo Pesquisar

style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background="#00e676")
style.configure("TProgressbar", thickness=6)
bar = Progressbar(frame3, length=190, style="black.Horizontal.TProgressbar")

janela.bind("<Return>")
janela.mainloop()
