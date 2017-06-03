import pandas as pd
from cleaner import *


def do_clean(df, filters):
    for filter in filters:
        df = filter(df)
    return df

def parse_args():
    parser = argparse.ArgumentParser(description="Applicate specified filtes to data")
    parser.add_argument('--f','--filters', type=str, nargs='+',
                        dest='filters', help='The list of filters to apply')
    parser.add_argument('--tr','--train', type=str,
                        dest='train_file', help='Name of the file with the train set')
    parser.add_argument('--t','--test', type=str,
                        dest='test_file', help='Name of the file with the test set')
    parser.add_argument('--s','--source', type=str,
                        dest='source', help='File format of the data')
    return parser.parse_args()


if __name__ == '__main__':
    # Configuration
    args = parse_args()

    # Read data
    train = pd.read_csv(input_dir + 'train.csv')
    test = pd.read_csv(input_dir + 'test.csv')

    # Clean data
    train = do_clean(train, args.filters)
    test = do_clean(test, args.filters)

    # Caching results
    train.to_csv(path_or_buf='../cache/cleaned_train.csv', index=False, encoding='utf-8')
    test.to_csv(path_or_buf='../cache/cleaned_test.csv', index=False, encoding='utf-8')
