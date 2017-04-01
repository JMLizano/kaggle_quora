import pandas as pd
from hashlib import md5
import os


def remove_missings(df):
    """
    Remove missing data from the giving df

    Format of the df:
    id | quid1 | quid2 | question1 | question2 | is_duplicate
    """

    # If question or label miss drop it
    return df.dropna(axis=0, subset=['question1', 'question2', 'is_duplicate'])


def remove_repeated_questions(df):
    """
    Removes repeated pair of questions from the dataframe
    """
    # TODO: Implement the method. 2 scenarios:
    #      - Repeated questions with same label->take only 1 record
    #      - Repeated questions with different label->Voting?, remove all?
    return

# TODO: Remove outliers
#   - 1 (or too few) character questions
#   - Too much characters questions
