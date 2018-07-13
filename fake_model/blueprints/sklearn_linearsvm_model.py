#
# model.py
# Fake News Classifier Model
# 
# Trains and saves a classifer model for classifing fake news
#

import pandas as pd
import pickle
import random
import math

import numpy as np

from datetime import datetime
from sklearn import svm, metrics
from sklearn.feature_extraction.text import TfidfVectorizer

# Split data into test and train sets to perform cross validation
# Splis data to test and train sets based on given factor, specifiy test size
# as a ratio of the entire datasetd
def split_test_train(inputs, outputs, test_ratio=0.3, random_state=0):
    data_len = len(inputs)
    
    # Shuffle the data to ensure relatively even distribution of data
    #random.seed(random_state)
    shuffle_order = list(range(data_len))
    random.shuffle(shuffle_order)
    
    shuffle_inputs = []
    shuffle_outputs = []
    for from_i in shuffle_order:
        shuffle_inputs.append(inputs[from_i])
        shuffle_outputs.append(outputs[from_i])
    
    # Split datasets into test and train
    divider = math.floor(data_len * test_ratio)
    
    test_inputs = shuffle_inputs[:divider]
    test_outputs = shuffle_outputs[:divider]
    
    train_inputs = shuffle_inputs[divider:]
    train_outputs = shuffle_outputs[divider:]

    return (train_inputs, train_outputs, test_inputs, test_outputs)

def build_model():
    return svm.LinearSVC()


# Saves model with timestamp in filename
def save_model(model, name_prefix="sklearn_linearsvc_text", suffix=".pickle"):
    # Make filename with timestamp
    now = datetime.now()
    fname = "./models/{}_{}_{}_{}{}".format(name_prefix, now.hour, now.minute, 
            now.second, suffix)
    
    with open(fname, "wb") as f:
        pickle.dump(model, f)
    
vectorizer = TfidfVectorizer()
# Converts text into feature vectors
def preprocess_data(texts):
    return vectorizer.transform(texts)
    
if __name__ == "__main__":
    print("Loading data...")
    # Load data
    df = pd.read_csv("./data/train.csv")
    labels = df.loc[:,"label"].values
    texts = df.loc[:,"text"].values.astype("U")
    titles = df.loc[:,"title"].values.astype("U")
        
    #full_texts = [ "{}\n{}".format(titles[i], texts[i]) for i in range(len(labels)) ]
    
    
    train_inputs, train_outputs, test_inputs, test_outputs = \
            split_test_train(texts, labels)
    
    # Preprocess data
    vectorizer.fit(train_inputs)
    train_inputs = preprocess_data(train_inputs)
    test_inputs = preprocess_data(test_inputs)

    # Train Model 
    print("Training model...")
    model = build_model()
    model.fit(train_inputs, train_outputs)
    save_model(model)
    
    # Test Model
    test_predicts = model.predict(test_inputs)
    
    
    # Display metrics of model
    print("Report:\n ", metrics.classification_report(test_outputs, test_predicts))
    
