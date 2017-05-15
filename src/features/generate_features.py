import sys
import logging
import pandas as pd
import argparse
import compute_features


def generate_features(df, features_list):
    logging.info("Starting generating features for following sets: %s" % str(features_list))
    for features in features_list:
        try:
            logging.info("Generating %s set of features" % features)
            # features is a string, we need to get the corresponding method
            df = getattr(compute_features, features)(df)
        except NameError as e:
            logging.error(e)
            logging.error("The {features} set of features does not exists".format(features=features))
    return df


def parse_args():
    parser = argparse.ArgumentParser(description="Generate specified features")
    parser.add_argument('--f','--features', type=str, nargs='+',
                        dest='features', help='The list of features to generate')
    parser.add_argument('--s','--store', type=str,
                        dest='store', help='Name of the HDFStore file')
    parser.add_argument('--tr','--train', type=str,
                        dest='train_file', help='Name of the file with the train set')
    parser.add_argument('--t','--test', type=str, 
                        dest='test_file', help='Name of the file with the test set')

    return parser.parse_args()


def get_df(store=None, train_file):
    with pd.HDFStore(store) as store:
        return store.select(train_file)


def save_df_with_name(df, store, name, features):
    features_registered = '_'.join(features)
    df.to_csv(path_or_buf=path + '_'.join([features_registered,name]), index=False, encoding='utf-8')


if __name__ == '__main__':

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # Read features to generate
    args = parse_args()

    # Read data
    train = pd.read_csv(args.train_file)
    test = pd.read_csv(args.test_file)

    # Generate features
    train = generate_features(train, args.features)
    test = generate_features(test, args.features)

    # Caching results
    save_with_name(train, '../../cache/with_features/', 'train', args.features)
    save_with_name(test, '../../cache/with_features/', 'test', args.features)
