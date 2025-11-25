import pandas as pd


def load_test_csv(path):
    return pd.read_csv(path)


def make_features_for_inference(df):
    return df
