import os

for video in os.listdir("."):
    if os.path.isdir(video):
        for i, filename in enumerate(os.listdir(video)):
            new_filename = video + "_" + str(i) + ".mp4"
            os.rename(video + "/" + filename, video + "/" + new_filename)
