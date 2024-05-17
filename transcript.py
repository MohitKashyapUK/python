from youtube_transcript_api import YouTubeTranscriptApi
"""from pytube import Playlist, YouTube
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
"""

def seconds_to_srt_time(seconds):
  milliseconds = 0
  if type(seconds) == float:
    seconds = str(seconds)
    split = seconds.split(".")
    seconds = int(split[0])
    milliseconds = int(split[1])
  hours = int(seconds // 3600)
  minutes = int((seconds % 3600) // 60)
  seconds = int(seconds % 60)
  if milliseconds > 0:
    milliseconds = int(str(milliseconds * 10)[:3])
  return "{:02d}:{:02d}:{:02d},{:03d}".format(hours, minutes, seconds, milliseconds)

def convert_json_to_srt(data):
  subtitles = ""
  index = 0
  for entry in data:
    index += 1  # Track subtitle number
    start_time = entry['start']  # Replace with actual key name
    end_time = entry['duration']  # Replace with actual key name
    text = entry['text']  # Replace with actual key name
    subtitle = f"{index}\n{seconds_to_srt_time(start_time)} --> {seconds_to_srt_time(start_time + end_time)}\n{text}\n\n"
    subtitles += subtitle
  return subtitles

def subtitles(video_id):
  list_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
  transcript = transcript_hi = transcript_en = command = None

  try:
    transcript = transcript_hi = list_transcripts.find_transcript(["hi"])
  except:
    try:
      temporary_transcript = list_transcripts.find_transcript(["en", "en-GB"])
      transcript = transcript_en = temporary_transcript
      transcript_hi = temporary_transcript.translate("hi")
    except:
      pass

  srt_subtitles = convert_json_to_srt(transcript.fetch())

  with open("subtitles.srt", "w", encoding="utf-8") as f:
    f.write(srt_subtitles)

  return "subtitles.srt"
"""
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
  index += 1"""