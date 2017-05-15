import json
from sklearn.ensemble import RandomForestClassifier


class RandomForest(RandomForestClassifier):
    """ Dummy wrapper around sklearn class to ease the automatic import"""
    
    def __init__(self, n_estimators=10, criterion='gini', max_depth=None,
                 min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0,
                 max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, 
                 bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, 
                 warm_start=False, class_weight=None):

        # Give correct format to each parameter since we are reading all as strings from configparser
        n_estimators = int(n_estimators)
        max_depth = None if max_depth is None else int(max_depth)
        min_samples_split = int(min_samples_split)
        min_samples_leaf = int(min_samples_leaf)
        min_weight_fraction_leaf = float(min_weight_fraction_leaf)
        max_leaf_nodes = None if max_leaf_nodes is None else int(max_leaf_nodes)
        min_impurity_split = float(min_impurity_split)
        bootstrap = bool(bootstrap)
        oob_score = bool(oob_score)
        n_jobs = int(n_jobs)
        random_state = None if random_state is None else int(random_state)
        verbose = int(verbose)
        warm_start = bool(warm_start)
        class_weight = None if class_weight is None else json.loads(class_weight)
        super(RandomForest, self).__init__(n_estimators=n_estimators, criterion=criterion, 
              max_depth=max_depth,min_samples_split=min_samples_split, 
              min_samples_leaf=min_samples_leaf, min_weight_fraction_leaf=min_weight_fraction_leaf,
              max_features=max_features, max_leaf_nodes=max_leaf_nodes, min_impurity_split=min_impurity_split, 
              bootstrap=bootstrap, oob_score=oob_score, n_jobs=n_jobs, random_state=random_state, verbose=verbose, 
              warm_start=warm_start, class_weight=class_weight)
