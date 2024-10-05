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

img_logo = Label(
    frame_cima, image=logo, compound=LEFT, bg=fundo, font=("Ivy 10 bold"), anchor="nw"
)
img_logo.place(x=95, y=15)

pesquisa = Image.open(r"images/lupa.png")
pesquisa = pesquisa.resize((30, 30), Image.Resampling.LANCZOS)
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
def pesquisar(envet=None):
    cont_mp4_hd.clear()
    cont_mp4_sd.clear()
    cont_mp3.clear()

    global teste
    teste = e_url.get()
    status["text"] = ""
    if (e_url.get()==""):
        messagebox.showinfo("Status", "Campo Vazio")
    else:
        global img
        frame3.place_forget()
        yt = YouTube(e_url.get())
    
    #Titulo

# ----------------------------------------------------------
e_url = Entry(frame_cima, width=50, justify="left", relief=SOLID)
e_url.place(x=60, y=80)

b_pesquisar = Button(
    frame_cima,
    text="Pesquisar",
    width=10,
    bg=co2,
    fg=co1,
    font=("Ivy 9 bold"),
    relief=RAISED,
    overrelief=RIDGE,
    command="",
)
b_pesquisar.place(x=390, y=78)

# Operações

l_imagmb = Label(
    frame_abaixo, image="", compound=LEFT, bg=fundo, font=("Ivy 10 bold"), anchor="nw"
)
l_imagmb.place(x=80, y=45)

l_titulob = Label(
    frame_abaixo,
    text="",
    height=2,
    wraplength=355,
    compound=LEFT,
    bg=fundo,
    fg=co1,
    font=("Ivy 10 bold"),
    anchor="nw",
)
l_titulob.place(x=80, y=0)

# aqui
# l_viewsb = Label(frame_baixo, text="", bg=fundo, fg=co1 ,font=('Ivy 8 bold'), anchor='nw')
# l_viewsb.place(x=10,y=340)

l_timeb = Label(
    frame_abaixo, text="", bg=fundo, fg=co1, font=("Ivy 8 bold"), anchor="nw"
)
l_titulob.place(x=80, y=310)

opcao = Label(
    frame_abaixo, text="Downloads", font=("Arial Black", 13), bg=fundo, fg=co1
)

linha_cada = ttk.Separator(frame_abaixo, orient=HORIZONTAL)

hd = Label(frame_abaixo, text="HD - 720p", font=("Arial Black", 9), bg=fundo, fg=co1)

sd = Label(frame_abaixo, text="SD - 360p", font=("Arial Black", 9), bg=fundo, fg=co1)

audio = Label(
    frame_abaixo, text="MP3 - Audio", font=("Arial Black", 9), bg=fundo, fg=co1
)

status = Label(
    frame_abaixo, text="Download Completo", font=("Arial Black", 10), bg=fundo, fg=co1
)

i_download = Image.open(r"images/video.png")
i_download = i_download.resize((30, 30), Image.Resampling.LANCZOS)
i_download = ImageTk.PhotoImage(i_download)

l_download = Button(
    frame_abaixo,
    image=i_download,
    command="",
    compound=LEFT,
    bg=fundo,
    fg=fundo,
    font=("Ivy 10 bold"),
    overrelief=RIDGE,
    activebackground=fundo,
    bd=0,
)

i_download1 = Image.open(r"images/video2.png")
i_download1 = i_download1.resize((30, 30), Image.Resampling.LANCZOS)
i_download1 = ImageTk.PhotoImage(i_download1)

l_download1 = Button(
    frame_abaixo,
    image=i_download1,
    command="",
    compound=LEFT,
    bg=fundo,
    fg=fundo,
    font=("Ivy 10 bold"),
    overrelief=RIDGE,
    activebackground=fundo,
    bd=0,
)

i_download2 = Image.open(r"images/audio.png")
i_download2 = i_download2.resize((30, 30), Image.Resampling.LANCZOS)
i_download2 = ImageTk.PhotoImage(i_download2)

l_download2 = Button(
    frame_abaixo,
    image=i_download2,
    command="",
    compound=LEFT,
    bg=fundo,
    fg=fundo,
    font=("Ivy 10 bold"),
    overrelief=RIDGE,
    activebackground=fundo,
    bd=0,
)


style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background="#00e676")
style.configure("TProgressbar", thickness=6)
bar = Progressbar(frame3, length=190, style="black.Horizontal.TProgressbar")

janela.bind("<Return>")
janela.mainloop()
