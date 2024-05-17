from pytube import YouTube

URL = "https://www.youtube.com/watch?v=ZHJjgF3QekE"

yt = YouTube(URL)
vid_info = yt.vid_info["videoDetails"]
# desc = yt.description

for i in vid_info:
  print(i)