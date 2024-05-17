from pytube import YouTube

yt = YouTube("https://youtu.be/R99e3fRTFmc?si=G4M0Dmz5m7LMJ87V")

# print(dir(yt))
print(yt.caption_tracks)