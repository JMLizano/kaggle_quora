import pandas as pd
from cleaner import *


def do_clean(df, filters):
    for filter in filters:
        df = filter(df)
    return df

def save_to_store():
    with pd.HDFStore('duplicate_question_store.h5') as store:
...     tr = pd.read_csv('cleaned_train.csv')
...     t = pd.read_csv('cleaned_test.csv')
...     store.append('datasets/cleaned_train/data',tr)
...     store.append('datasets/cleaned_test/data',t)

if __name__ == '__main__':
    # Configuration
    input_dir = '../input/'
    filters = [remove_missings,
               remove_repeated_questions,
               remove_outliers_questions]

    # Read data
    train = pd.read_csv(input_dir + 'train.csv')
    test = pd.read_csv(input_dir + 'test.csv')

    # Clean data
    train = do_clean(train, filters)
    test = do_clean(test, filters)

    # Caching results
    train.to_csv(path_or_buf='../cache/cleaned_train.csv', index=False, encoding='utf-8')
    test.to_csv(path_or_buf='../cache/cleaned_test.csv', index=False, encoding='utf-8')
