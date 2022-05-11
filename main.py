from moviepy.editor import *

mp4 = "somemovie.mp4"
mp3 = "audio.mp4"
videoclip = VideoFileClip(mp4)
audioclip = videoClip.audio.write_audiofile(mp3)
audio.clip.close()
videoclip.close()