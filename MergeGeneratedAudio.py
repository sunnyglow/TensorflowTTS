import os

audio_path = "C:/Users/sures/Desktop/output/"
fileCount = 0
fileCount = len(os.listdir(audio_path))

i = 0
f = open(audio_path + str("fileList.txt"), "w")
while i < fileCount:
    f.write(str("file '"+str(i)+str(".wav'\n")))
    i += 1
f.close()
command = "cmd /c start /min /wait cmd.exe /K  \"cd " + audio_path + " && ffmpeg -f concat -safe 0 -i fileList.txt -c copy -ar 48000 -rf64 auto input.wav && exit\""
os.system(command)

command = "cmd /c start /min /wait cmd.exe /K \"cd "+audio_path+" && ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 FinalOutput.mp3 && exit\""
os.system(command)