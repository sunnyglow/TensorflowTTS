import numpy as np
import soundfile as sf
import yaml

import tensorflow as tf

from tensorflow_tts.inference import TFAutoModel, AutoConfig
from tensorflow_tts.inference import AutoProcessor

voices_path = "C:/Users/sures/OneDrive/Documents/TamilTTS/TensorFlowTTS/Voices/"
#voice = "Chitra_Voice";
voice = "Charles_Voice";
# initialize fastspeech2 model.
#fastspeech2 = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-ljspeech-en")
config1 = AutoConfig.from_pretrained(voices_path+voice+"/fastspeech2/config.yml")
fastspeech2 = TFAutoModel.from_pretrained(voices_path+voice+"/fastspeech2/model.h5", config=config1)

#config1 = AutoConfig.from_pretrained("C:/Users/sures/Documents/TamilTTS/TensorFlowTTS/Voices/Charles_Voice/fastspeech2/config.yml")
#fastspeech2 = TFAutoModel.from_pretrained("C:/Users/sures/Documents/TamilTTS/TensorFlowTTS/Voices/Charles_Voice/fastspeech2/model-560000.h5", config=config1)


# initialize mb_melgan model
#mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-ljspeech-en")
config2 = AutoConfig.from_pretrained(voices_path+voice+"/multiband_melgan/config.yml")
mb_melgan = TFAutoModel.from_pretrained(voices_path+voice+"/multiband_melgan/generator.h5", config=config2)

#config2 = AutoConfig.from_pretrained("C:/Users/sures/Documents/TamilTTS/TensorFlowTTS/Voices/Charles_Voice/multiband_melgan/config.yml")
#mb_melgan = TFAutoModel.from_pretrained("C:/Users/sures/Documents/TamilTTS/TensorFlowTTS/Voices/Charles_Voice/multiband_melgan/generator-500000.h5", config=config2)


# inference
processor = AutoProcessor.from_pretrained(voices_path+voice+"/fastspeech2/processor.json")


sotry_path = "C:\\Users\\sures\\OneDrive\\Documents\\TamilTTS\\input.txt"
batch = []
bufferLine = ""
batchSize = 150
with open(sotry_path, encoding="utf-8") as bigfile:
    for x, line in enumerate(bigfile):
        if line.strip() == "":
            continue

        words = line.split(" ")
        #print(words)
        wordCounter = 0;
        while wordCounter < len(words):
            if(len(bufferLine) + len(words[wordCounter]) < batchSize):
                bufferLine += words[wordCounter]+str(" ")
                wordCounter += 1
            else:
                bufferLine = bufferLine.replace("\n", ". ")
                bufferLine = bufferLine.strip()
                batch.append([bufferLine])
                bufferLine = ""

if bufferLine != "":
    bufferLine = bufferLine.replace("\n", ". ")
    bufferLine = bufferLine.strip()
    batch.append([bufferLine])
    bufferLine = ""

batchCounter = 0;
buffer_text = " ஆதி அந்தமில்லாத கால வெள்ளத்தில் "
while batchCounter < len(batch) :
    input_ids = processor.text_to_sequence(buffer_text+batch[batchCounter][0]+buffer_text)
    # fastspeech inference

    mel_before, mel_after, duration_outputs, _, _ = fastspeech2.inference(
        input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
        speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
        speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
        f0_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
        energy_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
    )

    # melgan inference
    audio_before = mb_melgan.inference(mel_before)[0, :, 0]
    #audio_after = mb_melgan.inference(mel_after)[0, :, 0]

    # save to file
    #sf.write('C:/Users/sures/Desktop/output/'+str(batchCounter)+'.wav', audio_before, 22050, "PCM_16")
    print("############################## Writing file: "+str(batchCounter)+'.wav')
    print(batch[batchCounter][0])
    sf.write('C:/Users/sures/OneDrive/Documents/TamilTTS/output/' + str(batchCounter) + '.wav', audio_before, 22050, "PCM_16")
    #sf.write('C:/Users/sures/OneDrive/Documents/TamilTTS/output/'+str(batchCounter)+'.wav', audio_after, 22050, "PCM_16")
    batchCounter += 1