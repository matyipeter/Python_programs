from pytube import YouTube
import os

DESTINATION = "/home/peter/Music/"

def convert():
    yt = YouTube(
        str(input("Enter the URL of the video you want to download: \n>> ")))

    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=DESTINATION)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")
  
convert()    