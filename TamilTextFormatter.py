
sotry_path = "/home/sureshkumar/Documents/TTSTrainings/GitWaveRNN/input_text/final_input.txt"
batch = []
bufferLine = ""
batchSize = 250
with open(sotry_path) as bigfile:
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
                batch.append([bufferLine])
                bufferLine = ""

#print(batch)
batchCounter = 0;
while batchCounter < len(batch):
    print(batch[batchCounter][0])
    batchCounter += 1