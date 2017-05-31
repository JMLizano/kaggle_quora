import pandas as pd
from fuzzywuzzy import fuzz
"""
Length of question1
Length of question2
Difference in the two lengths
Character length of question1 without spaces
Character length of question2 without spaces
Number of words in question1
Number of words in question2
Number of common words in question1 and question2
"""

def available_features_set():  
    features_set = {
        'f1':['len_q1','len_q1','diff_len', 
              'len_q1_nospaces','len_q2_nospaces','diff_len_nospaces',
              'words_q1','words_q2','common_words'],
        'f2':['fuzz_qratio','fuzz_WRatio','fuzz_partial_ratio','fuzz_partial_token_set_ratio',
              'fuzz_partial_token_sort_ratio','fuzz_token_set_ratio','fuzz_token_sort_ratio']
    }
    return features_set

def question_length(df):
    """Computes features related to question length """
    df["len_q1"] = df["question1"].apply(lambda x: len(str(x)))
    df["len_q2"] = df["question2"].apply(lambda x: len(str(x)))
    df["diff_len"] = df.len_q1 - df.len_q2
    return df


def question_length_nospaces(df):
    """Computes features related to question length after removing spaces """
    df["len_q1_nospaces"] = df["question1"].apply(lambda x: len(str(x).replace(' ','')))
    df["len_q2_nospaces"] = df["question2"].apply(lambda x: len(str(x).replace(' ','')))
    df["diff_len_nospaces"] = df.len_q1_nospaces - df.len_q2_nospaces
    return df


def question_words(df):
    """Computes features related to words in each question """
    df["words_q1"] = df["question1"].apply(lambda x: len(str(x).split(' ')))
    df["words_q2"] = df["question2"].apply(lambda x: len(str(x).split(' ')))
    df["common_words"] = df.apply(lambda x: len(set(x["question1"].lower().split(' ')).intersection(set(x["question2"].lower().split(' ')))), axis=1)
    return df


def fuzzywuzzy_features(df):
    """Computes features from fuzzywuzzy library """
    df['fuzz_qratio'] = df.apply(lambda x: fuzz.QRatio(str(x['question1']), str(x['question2'])), axis=1)
    df['fuzz_WRatio'] = df.apply(lambda x: fuzz.WRatio(str(x['question1']), str(x['question2'])), axis=1)
    df['fuzz_partial_ratio'] = df.apply(lambda x: fuzz.partial_ratio(str(x['question1']), str(x['question2'])), axis=1)
    df['fuzz_partial_token_set_ratio'] = df.apply(lambda x: fuzz.partial_token_set_ratio(str(x['question1']), str(x['question2'])), axis=1)
    df['fuzz_partial_token_sort_ratio'] = df.apply(lambda x: fuzz.partial_token_sort_ratio(str(x['question1']), str(x['question2'])), axis=1)
    df['fuzz_token_set_ratio'] = df.apply(lambda x: fuzz.token_set_ratio(str(x['question1']), str(x['question2'])), axis=1)
    df['fuzz_token_sort_ratio'] = df.apply(lambda x: fuzz.token_sort_ratio(str(x['question1']), str(x['question2'])), axis=1)
    return df


def f1(df):
    """Represents the most simple set of features"""
    df = question_length(df)
    df = question_length_nospaces(df)
    df = question_words(df)
    return df


def f2(df):
    """Represents the set of features related to fuzzywuzzy"""
    return fuzzywuzzy_features(df)
