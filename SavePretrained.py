import logging
import os
import tensorflow as tf

from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoConfig
from tensorflow_tts.inference import AutoProcessor

def test_auto_processor(mapper_path):
    processor = AutoProcessor.from_pretrained(pretrained_path=mapper_path)
    processor.save_pretrained("/home/sureshkumar/Documents/TensorFlowTTS/TensorFlowTTS/examples/fastspeech2/exp/train.fastspeech2.v1/pretrained/")

test_auto_processor("/home/sureshkumar/Documents/TensorFlowTTS/TensorFlowTTS/dump_tamilspeech/tamilspeech_mapper.json")

def test_auto_model(config_path):
    config = AutoConfig.from_pretrained(pretrained_path=config_path)
    model = TFAutoModel.from_pretrained(pretrained_path=None, config=config)

    # test save_pretrained
    config.save_pretrained("/home/sureshkumar/Documents/TensorFlowTTS/TensorFlowTTS/examples/multiband_melgan/exp/train.multiband_melgan.v1/pretrained/")
    model.save_pretrained("/home/sureshkumar/Documents/TensorFlowTTS/TensorFlowTTS/examples/multiband_melgan/exp/train.multiband_melgan.v1/pretrained/")

    # test from_pretrained
    config = AutoConfig.from_pretrained("/home/sureshkumar/Documents/TensorFlowTTS/TensorFlowTTS/examples/multiband_melgan/exp/train.multiband_melgan.v1/pretrained/config.yml")
    model = TFAutoModel.from_pretrained("/home/sureshkumar/Documents/TensorFlowTTS/TensorFlowTTS/examples/multiband_melgan/exp/train.multiband_melgan.v1/pretrained/model.h5", config=config)

#test_auto_model("/home/sureshkumar/Documents/TensorFlowTTS/TensorFlowTTS/examples/multiband_melgan/exp/train.multiband_melgan.v1/config.yml");
