# src/scorer.py
from pathlib import Path
import numpy as np
from catboost import CatBoostClassifier

MODEL_PATH = Path('models/model.cbm')


def load_model():
    model = CatBoostClassifier()
    model.load_model(MODEL_PATH)
    return model


def score_proba(model, X):
    proba = model.predict_proba(X)[:, 1]
    return proba