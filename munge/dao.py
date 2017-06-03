import pandas as pd
import logging


def load_dataframe(source, path, **kwargs):
    if source == 'csv':
        try:
            return pd.read_csv(path)
        except:
            logging.error("Could not load dataframe from %s" % path)
    elif source == 'h5':
        if 'h5store' not in kwargs.keys():
            logging.error("""You must provide and store when using
                          a h5 source""")
            raise KeyError
        try:
            with pd.HDFStore(kwargs) as store:
                return store.select_as_multiple(path)
        except KeyError as ke:
            logging.error("Specified path %s does not exists" % path)
            raise ke
    else:
        raise NotImplementedError


def save_dataframe(df, source, path, **kwargs):
    if source == 'csv':
        try:
            df.to_csv(path_or_buf=path, index=False, encoding='utf-8')
        except:
            logging.error("Could not save dataframe at %s" % path)
    elif source == 'h5':
        if 'h5store' not in kwargs.keys():
            logging.error("""You must provide and store when using
                          a h5 source""")
            raise KeyError
        try:
            dist = kwargs['h5dist']
            selector = kwargs['h5selector']
            complib = kwargs['h5complib']
            complevel = kwargs['h5complevel']
            with pd.HDFStore(kwargs) as store:
                store.append_to_multiple(dist, df,
                                         selector=selector,
                                         complib=complib,
                                         complevel=complevel,
                                         index=False)
        except KeyError as ke:
            logging.error("Specified path %s does not exists" % path)
            raise ke
    else:
        raise NotImplementedError
