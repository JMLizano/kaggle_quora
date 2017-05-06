import pandas as pd
import os


def remove_missings(df):
    """
    Remove missing data from the giving df

    Format of the df:
    id | quid1 | quid2 | question1 | question2 | is_duplicate
    """

    # If question or label miss drop it
    return df.dropna(axis=0, subset=['question1', 'question2'])


def remove_repeated_questions(df):
    """
    Removes repeated pair of questions from the dataframe
    """
    # TODO: Check if there are not duplicated pairs of questions with different
    #       labels really, since some posts on kaggle claim to have found it

    # From the first_EDA notebook we know that there are no duplicate questions
    # with different labels, so just drop them
    return df.drop_duplicates(subset=['question1', 'question2'])


def filter_by_length(df, columns, lengths):
    for column, length in zip(columns, lengths):
        df = df[df[column].apply(lambda x: len(x) > length)]
    return df


def remove_outliers_questions(df):
    """
    Remove questions with length less than 11, see first_EDA for reason on this
    """
    return filter_by_length(df, ['question1', 'question2'], [11, 11])

    # TODO: Maybe fix those duplicated questions that not share id? (See first_EDA)
