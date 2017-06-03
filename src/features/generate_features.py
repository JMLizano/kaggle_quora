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


def get_df(store=None, train_file=None):
    with pd.HDFStore(store) as store:
        try:
            return store.select(train_file)
        except KeyError as ke:
            logging.error("The input file \"%s\" does not exists" % train_file)
            sys.exit(1)


def save_df_with_name(df, store, name, features):
    features_registered = '_'.join(features)
    df.to_csv(path_or_buf=path + '_'.join([features_registered,name]), index=False, encoding='utf-8')


def save_to_hstore(df, store, rootpath, features):
    dist = {}
    available_features = compute_features.available_features_set()
    dist[rootpath + 'data'] = ['id','quid1','quid2','question1','question2','is_duplicate']
    for feature in features:
        dist[rootpath + feature] = available_features[feature]
    with pd.HDFStore(store) as store:
        store.append_to_multiple(dist,df,selector=rootpath + 'data', complib='blosc', complevel=4,index=False)


if __name__ == '__main__':

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # Read features to generate
    args = parse_args()

    # Read data
    train = get_df(args.store, args.train_file)
    test = get_df(args.store, args.test_file)

    # Generate features
    train = generate_features(train, args.features)
    test = generate_features(test, args.features)

    # Caching results
    save_to_hstore(train, args.store, 'datasets/cleaned_train/', args.features)
    save_to_hstore(test, args.store, 'datasets/cleaned_test/', args.features)
