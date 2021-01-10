from pytube import YouTube

video = input(">")

yt = YouTube(video)
yt.streams.all()
stream = yt.streams.first()

stream.download('C:\\Users\ELIZ-VILLA\Desktop')