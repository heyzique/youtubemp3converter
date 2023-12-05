import tkinter
import customtkinter
from pytube import YouTube
import os


def startdownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        out_path = ytObject.streams.filter(only_audio=True).first().download()
        new_name = os.path.splitext(out_path)
        os.rename(out_path, new_name[0]+'.mp3')
        print("Download Complete!")
        finishlabel.configure(text="Downloaded!", text_color="green")
    except:
        print("Youtube link is invalid")
        finishlabel.configure(text="Download Error!", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percentage_completion = bytes_download / total_size * 100
    print(percentage_completion)
    per = str(int(percentage_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_completion) / 100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("Dark")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube-MP3-Converter.py")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert Youtube Link", font=("Helvetica", 18, 'bold'))
title.pack(padx=20, pady=20)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startdownload)
download.pack(padx=10, pady=10)

# Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Run App
app.mainloop()