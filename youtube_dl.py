import os
import datetime
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Progressbar
from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
import requests
from PIL import Image, ImageTk
from urllib.request import urlopen, Request


class YouTubeDownloaderApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("YouTube Downloader")
        self.window.geometry(self.center_window(790, 500))
        self.window.configure(bg="#3b3b3b")
        self.window.iconbitmap(r"images/you.ico")
        
        self.video_url = ""
        self.thumbnail_image = None
        self.progress_var = IntVar()
        
        self.setup_ui()

    def center_window(self, width, height):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (width / 2))
        y_cordinate = int((screen_height / 2) - (screen_height / 3))
        return f"{width}x{height}+{x_cordinate}+{y_cordinate}"

    def setup_ui(self):
        # Frame superior
        frame_top = Frame(self.window, width=500, height=110, bg="#3b3b3b", pady=5)
        frame_top.grid(row=1, column=0)
        
        # Logotipo e pesquisa
        self.add_logo(frame_top)
        self.add_search_bar(frame_top)

        # Frame inferior
        self.frame_bottom = Frame(self.window, width=800, height=500, bg="#3b3b3b", pady=12)
        self.frame_bottom.grid(row=2, column=0, sticky=NW)

        # Elementos de detalhes do vídeo
        self.video_title = Label(self.frame_bottom, text="", height=2, wraplength=355, bg="#3b3b3b", fg="#feffff", font=("Ivy 10 bold"))
        self.video_title.place(x=80, y=0)

        self.video_duration = Label(self.frame_bottom, text="", bg="#3b3b3b", fg="#feffff", font=("Ivy 8 bold"))
        self.video_duration.place(x=80, y=310)
        
        # Configurações de download
        self.download_options()

    def add_logo(self, frame):
        logo = Image.open(r"images/youtube.png").resize((50, 50), Image.Resampling.LANCZOS)
        logo_img = ImageTk.PhotoImage(logo)
        Label(frame, image=logo_img, bg="#3b3b3b").place(x=95, y=15)
        Label(frame, text="Download YouTube", bg="#3b3b3b", fg="#feffff", font=("Ivy 15 bold")).place(x=150, y=27)

    def add_search_bar(self, frame):
        self.url_entry = Entry(frame, width=50, justify="left", relief=SOLID)
        self.url_entry.place(x=60, y=80)
        
        Button(frame, text="Pesquisar", width=10, bg="#6f9fbd", fg="#feffff", font=("Ivy 9 bold"), command=self.search_video).place(x=390, y=78)
        
    def download_options(self):
        Label(self.frame_bottom, text="Downloads", font=("Arial Black", 13), bg="#3b3b3b", fg="#feffff").place(x=550, y=50)
        
        hd_button = Button(self.frame_bottom, text="HD - 720p", command=self.download_hd, bg="#3b3b3b", fg="#feffff")
        hd_button.place(x=515, y=120)

        sd_button = Button(self.frame_bottom, text="SD - 360p", command=self.download_sd, bg="#3b3b3b", fg="#feffff")
        sd_button.place(x=515, y=170)

        mp3_button = Button(self.frame_bottom, text="MP3 - Audio", command=self.download_mp3, bg="#3b3b3b", fg="#feffff")
        mp3_button.place(x=515, y=220)

        self.progress_bar = Progressbar(self.frame_bottom, variable=self.progress_var, length=190, style="black.Horizontal.TProgressbar")
        self.progress_bar.place(x=500, y=400)

        self.status_label = Label(self.frame_bottom, text="", font=("Arial Black", 10), bg="#3b3b3b", fg="#feffff")

    def search_video(self):
        video_url = self.url_entry.get()
        urlopen(Request(video_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}))
        if not video_url:
            messagebox.showinfo("Status", "Campo Vazio")
            return

        yt = YouTube(video_url, on_progress_callback=self.on_progress)
        self.video_url = video_url
        self.video_title.config(text=yt.title)
        self.video_duration.config(text=f"Duração: {str(datetime.timedelta(seconds=yt.length))}")

        thumbnail_url = yt.thumbnail_url
        self.thumbnail_image = Image.open(requests.get(thumbnail_url, stream=True).raw).resize((375, 250), Image.Resampling.LANCZOS)
        self.thumbnail_image = ImageTk.PhotoImage(self.thumbnail_image)

        Label(self.frame_bottom, image=self.thumbnail_image, bg="#3b3b3b").place(x=80, y=45)

    def download_hd(self):
        self.download_video(resolution='highest')

    def download_sd(self):
        self.download_video(resolution='lowest')

    def download_mp3(self):
        self.download_audio()

    def download_video(self, resolution):
        if not self.video_url:
            messagebox.showinfo("Status", "Nenhum vídeo selecionado")
            return

        yt = YouTube(self.video_url, on_progress_callback=self.on_progress)
        stream = yt.streams.get_highest_resolution() if resolution == 'highest' else yt.streams.get_lowest_resolution()
        
        self.status_label.config(text="Fazendo Download")
        self.status_label.place(x=530, y=320)
        
        download_path = stream.download(output_path=os.path.expanduser("~/Desktop"))
        os.rename(download_path, download_path.replace(".mp4", f" {resolution}.mp4"))
        
        self.status_label.config(text="Download Completo")
        self.progress_var.set(100)
        self.url_entry.delete(0, END)

    def download_audio(self):
        if not self.video_url:
            messagebox.showinfo("Status", "Nenhum vídeo selecionado")
            return

        yt = YouTube(self.video_url, on_progress_callback=self.on_progress)
        stream = yt.streams.get_audio_only()
        
        self.status_label.config(text="Fazendo Download")
        self.status_label.place(x=530, y=320)
        
        download_path = stream.download(output_path=os.path.expanduser("~/Desktop"))
        os.rename(download_path, download_path.replace(".mp4", ".mp3"))
        
        self.status_label.config(text="Download Completo")
        self.progress_var.set(100)
        self.url_entry.delete(0, END)

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress_percentage = int((bytes_downloaded / total_size) * 100)
        
        self.progress_var.set(progress_percentage)
        self.window.update_idletasks()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = YouTubeDownloaderApp()
    app.run()
