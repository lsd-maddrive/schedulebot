import pickle

import yaml


def read_yaml(fpath: str) -> dict:
    with open(fpath) as fp:
        data = yaml.safe_load(fp)
    return data


def load_graph(fpath: str):
    with open(fpath, 'rb') as f:
        graph_obj = pickle.load(f)
    return graph_obj
