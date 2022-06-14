from pydub import AudioSegment
import os
source_path = "C:/Users/sures/OneDrive/Documents/TamilTTS/output/"
desti_path = "C:/Users/sures/OneDrive/Documents/TamilTTS/trimmed/"
start_count = 0
end_count = 1141

while(start_count <= end_count):
    path = source_path+str(start_count)+str(".wav")
    print(path)
    newAudio = AudioSegment.from_wav(path)
    print(len(newAudio))
    end = len(newAudio) - 2175
    len(newAudio)
    newAudio = newAudio[2150:end]
    newAudio.export(desti_path+str(start_count)+str(".wav"), format="wav") #Exports to a wav file in the current path.
    start_count += 1
