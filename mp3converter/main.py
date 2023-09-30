from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
import os


class GUI():
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text='MP3 converter', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Convert', font=('Arial', 18), command=self.convert)
        self.button.pack(padx=15, pady=10)

        self.root.mainloop()

    def convert(self):
        yt = YouTube(str(self.textbox.get('1.0', tk.END)))

        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        messagebox.showinfo(title='Success!',message = yt.title + " has been successfully downloaded.")
  
GUI()



    


