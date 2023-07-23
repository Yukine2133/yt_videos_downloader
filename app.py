import tkinter
from tkinter import filedialog
import customtkinter
from pytube import YouTube
from pathlib import Path


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        # Get the download folder path
        download_folder = Path.home() / "Downloads"

        # Set the download path to the "Downloads" folder
        video.download(output_path=download_folder)

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text='')
        finishLabel.configure(text="Downloaded")
    except Exception as e:
        finishLabel.configure(text="Error: " + str(e), text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # update progress bar
    progressBar.set(float(percentage_of_completion) / 100)


# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# adding ui elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# finished download
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(pady=20)


# run app
app.mainloop()
