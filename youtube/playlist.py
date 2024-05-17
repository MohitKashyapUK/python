from pytube import Playlist, YouTube
import os

url = input("Enter YouTube playlist URL: ")
playlist = Playlist(url)

print(f"Total number of videos: {len(playlist)}\n")

start = input("Start: ")
end = input("End: ")
path = input("Path: ")

print("\nChoose quality:")
print("1. 360p")
print("2. 720p")

quality = int(input("Number: ")) - 1

if start or end:
  if start and end:
    start = int(start) - 1
    end = int(end) - 1
  else:
    if start:
      start = int(start) - 1
      end = len(playlist) - 1
    else:
      start = 0
      end = int(end) - 1
else:
  start = 0
  end = len(playlist) - 1

index = start

while index <= end:
  url = playlist[index]
  os.system("cls")
  print(index + 1)
  while True:
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True)
    if len(streams)<2:
      continue
    else:
      video_stream = streams[quality]
      full_path = os.path.join(path, f"{index+1}. {video_stream.default_filename}")
      command = f'ffmpeg -i "{video_stream.url}" -c copy -y "{full_path}"'
      os.system(command)
      break
  index += 1