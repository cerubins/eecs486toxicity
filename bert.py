from transformers import BertTokenizer
import glob
import time
import math
from pathlib import Path
import datasets
import pandas as pd
import tensorflow as tf
from tqdm.notebook import tqdm

# tokenizer = BertTokenizer.from_pretrained('bert-base-cased')


# for file in glob.glob('comments/*'):
#     with open(file) as f:
#         lines = f.readlines()
#         for line in lines:
#             # preprocessing here
#             bert_input = tokenizer(line, padding='max_length', max_length = 10, truncation=True, return_tensors="pt")
#             #print(tokenizer.tokenize(line))


# TESTING + OUTPUT

# Iterates through subreddit comment files
for file in glob.glob('comments/*'):
    with open(file) as f:
        lines = f.readlines()

        filename = file.lstrip('comments/')

        print(filename)
        
        # preprocessing here
        # TODO: Add Katie's function

        # BERT tokenize here
        tf_batch = tokenizer(lines, max_length=128, padding=True, truncation=True, return_tensors='tf')

        # Run the model on the list
        tf_outputs = model(tf_batch)

        # Runs softmax to get predictions
        tf_predictions = tf.nn.softmax(tf_outputs[0], axis=-1)

        # Label predictions as toxic and non-toxic
        labels = ['Non-Toxic','Toxic']
        
        # Max of predictions gets labelled
        label = tf.argmax(tf_predictions, axis=1)
        label = label.numpy()

        # Prints predictions into output file
        f = open('output/' + filename, 'w')
        for i in range(len(lines)):
            f.write(lines[i], " ", labels[label[i]])
