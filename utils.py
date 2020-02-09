import numpy as np
import pandas as pd
import xgboost as xgb
import nltk
import math
import seaborn as sns

from sklearn import datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

def letters(input):
    return ''.join(filter(str.isalpha or str.isspace(), input))

def manipulate_string_values(string,is_return_as_list):
    stop_words = set(stopwords.words('english')).union(["please","your"])
    word_tokens = word_tokenize(str(string).lower()) 
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = [] 

    for w in word_tokens: 
        if w not in stop_words: 
            filter_only_letters_w = letters(w)
            if filter_only_letters_w.strip():
                #print('Appending: ' + filter_only_letters_w)
                filtered_sentence.append(filter_only_letters_w) 
            
    if(is_return_as_list):
        return filtered_sentence
    else:
        return ' '.join(filtered_sentence)

def do_one_hot_encoding_with_values(data_df,feature_name,limit,label_tag,positive_class_values,negative_class_values):
    print("One Hot Encoding for "+feature_name)
    data_df_positive = data_df[data_df[label_tag].isin(positive_class_values)]
    features_from_positive_labels = list(dict.fromkeys(data_df_positive[feature_name].values))

    data_df_negative = data_df[data_df[label_tag].isin(negative_class_values)]
    features_from_negative_labels = list(dict.fromkeys(data_df_negative[feature_name].value_counts().head(limit).index.tolist()))

    results_list = [features_from_positive_labels, features_from_negative_labels]
    results_union = list(filter(None, list(set().union(*results_list))))

    data_df_with_relevant_values = data_df[data_df[feature_name].isin(results_union)]
    data_df = pd.get_dummies(data=data_df_with_relevant_values, columns=[feature_name],drop_first=True)
    return data_df
