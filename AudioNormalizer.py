from pathlib import Path

import os
import subprocess
import soundfile as sf
import pyloudnorm as pyln
import sys

src = "D:\\AudioWorks\\PerumugizhvinPeravai\\ffmpegformatted\\"
target = "D:\\AudioWorks\\PerumugizhvinPeravai\\noramalized"

paths = Path(src).glob("**/*.wav")

for filepath in paths:
    target_filepath=Path(str(filepath).replace("ffmpegformatted", "noramalized"))
    target_dir=os.path.dirname(target_filepath)

    if (str(filepath) == str(target_filepath)):
        raise ValueError("Source and target path are identical: " + str(target_filepath))

    print("From: " + str(filepath))
    print("To: " + str(target_filepath))
    data, rate = sf.read(filepath)

    # peak normalize audio to -1 dB
    peak_normalized_audio = pyln.normalize.peak(data, -1.0)

    # measure the loudness first
    meter = pyln.Meter(rate) # create BS.1770 meter
    loudness = meter.integrated_loudness(data)

    # loudness normalize audio to -25 dB LUFS
    loudness_normalized_audio = pyln.normalize.loudness(data, loudness, -30.0)

    sf.write(target_filepath, data=loudness_normalized_audio, samplerate=22050)

    print("")