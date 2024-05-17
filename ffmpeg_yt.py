from pytube import YouTube
import os

url = input("Enter YouTube video URL: ")
yt = YouTube(url)
streams = yt.streams.filter(progressive=True)

for index, i in enumerate(streams):
  filesize = None
  filesize_kb = i.filesize_kb

  if filesize_kb>=1000:
    filesize_mb = i.filesize_mb
    if filesize_mb>=1000:
      filesize = f"{i.filesize_gb}GB"
    else:
      filesize = f"{filesize_mb}MB"
  else:
    filesize = f"{filesize_kb}KB"

  print(f"{index + 1}. {i.resolution}, {filesize}")

stream_index = int(input("Enter index: ")) - 1
video_stream = streams[stream_index]
file_name = os.path.join(r"C:\Users\mohit\Class 9th science", video_stream.default_filename)
command = f'ffmpeg -i "{video_stream.url}" -c copy -y "{file_name}"'

os.system(command)