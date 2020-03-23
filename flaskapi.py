from flask import Flask, json, jsonify, request
from unigram_model import unigram_model
from get_model import get_model
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from datetime import datetime

global unigram_models, tokenizer, label_tokenizer

def load_unigram_model():
    global unigram_models, tokenizer, label_tokenizer, reverse_label_word_index
    PIK='unigram_data/unigrams.dat'
    with open(PIK,"rb") as f:
        pickle_data=pickle.load(f)
    unigram_models, tokenizer, label_tokenizer = pickle_data
    reverse_label_word_index = {v: k for k, v in label_tokenizer.word_index.items()}

def load_dl_model():
    global model, trunc_type, padding_type, max_length, dl_tokenizer, dl_label_tokenizer, reverse_dl_label_word_index
    
    vocab_size = 2000
    embedding_dim = 32
    max_length = 50
    trunc_type='post'
    padding_type='post'

    model = get_model(vocab_size, embedding_dim, max_length)
    model.load_weights("dl_data/gfk_model.h5")

    PIK='dl_data/tokenizers.dat'
    with open(PIK,"rb") as f:
        pickle_data=pickle.load(f)
    dl_tokenizer, dl_label_tokenizer = pickle_data
    reverse_dl_label_word_index = {v: k for k, v in dl_label_tokenizer.word_index.items()}

api=Flask(__name__)

@api.route('/request', methods=['POST'])
def request_category():
    t0 = datetime.now()
    data = request.json
    text=data['description']
    sequence = tokenizer.texts_to_sequences([text])

    label_predict=''
    p_max = 0.0
    for key in unigram_models.keys():
        p = unigram_models[key].get_sequence_probability(sequence[0])
        if p>p_max:
            p_max=p
            label_predict=key
    t2 = datetime.now()
    return jsonify({'category':reverse_label_word_index[label_predict],"inf_time":(t2-t0).microseconds})

@api.route('/request_dl', methods=['POST'])
def request_category_dl():
    t0 = datetime.now()
    data = request.json
    text=data['description']
    sequence = dl_tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, padding=padding_type, maxlen=max_length)

    label_predict=model.predict(padded_sequence)
    label=np.argmax(label_predict[0])
    t2 = datetime.now()
    return jsonify({'category':reverse_dl_label_word_index[label], "inf_time":(t2-t0).microseconds})

if __name__ == '__main__':
    load_unigram_model()
    load_dl_model()
    api.run(host="0.0.0.0", port="5000")
