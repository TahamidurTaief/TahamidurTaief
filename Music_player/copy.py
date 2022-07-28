from tkinter import *
#import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os


class musicplayer:
    def __init__(self, root):
        self.root=root
        root.title("Music Player")
        root.geometry("920x670+290+85")
        root.config(bg="#0f1a2b")
        root.resizable(False, False)

        mixer.init()

        def open_folder():
            path = filedialog.askdirectory()
            if path:
                os.chdir(path)
                songs = os.listdir(path)
                # print(songs)
                for song in songs:
                    if song.endswith(".mp3"):
                        self.playlist.insert(END, song)

        def play_music():
            music_name = self.playlist.get(ACTIVE)
            mixer.music.load(self.playlist.get(ACTIVE))
            mixer.music.play()
            self.music.config(text=music_name[0:-4])

        def pause():
            mixer.music.pause()
            mixer.music.unpause()

        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)

        # icon
        self.image_icon = PhotoImage(file="logo.png")
        root.iconphoto(False, self.image_icon)

        self.top = PhotoImage(file="thumble.png")
        Label(root, image=self.top, bg="#0f1a2b").pack()

        # logo
        self.logo = PhotoImage(file="logo2.png")
        Label(root, image=self.logo, bg="#0f1a2b").place(x=65, y=70)

        # button
        self.play_button = PhotoImage(file="start.png")
        Button(root, image=self.play_button, bg="#0f1a2b", bd=0, command=play_music).place(x=100, y=400)

        self.stop_button = PhotoImage(file="stop.png")
        Button(root, image=self.stop_button, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)

        self.resume_button = PhotoImage(file="resume.png")
        Button(root, image=self.resume_button, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)

        self.pause_button = PhotoImage(file="pause.png")
        Button(root, image=self.pause_button, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=200, y=500)

        # Label
        self.music = Label(root, text="", font="arial 10", fg="white", bg="#0f1a2b")
        self.music.place(x=600, y=270, anchor=CENTER)

        # music
        self.menu = PhotoImage(file="menu.png")
        Label(root, image=self.menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

        self.music_frame = Frame(root, bd=2, relief=RIDGE)
        self.music_frame.place(x=330, y=350, width=560, height=250)

        Button(root, text="Open Folder", width=15, height=2, font=("arial", 10, "bold"), fg="white", bg="#21b3de",
               command=open_folder).place(x=330, y=300)

        self.scroll = Scrollbar(self.music_frame)
        self.playlist = Listbox(self.music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey",
                           selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.playlist.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.playlist.pack(side=LEFT, fill=BOTH)
        self.scale = Scale(self.root, from_=0, to=100, bg="cyan", orient=HORIZONTAL, length=120, command=volume)
        self.scale.place(x=100, y=600)





root=Tk()
obj=musicplayer(root)
root.mainloop()