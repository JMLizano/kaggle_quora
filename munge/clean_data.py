import pandas as pd
from cleaner import *


def do_clean(df, filters):
    for filter in filters:
        df = filter(df)
    return df


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
