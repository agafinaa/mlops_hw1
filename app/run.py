import os
from pathlib import Path
import pandas as pd
import numpy as np
from src.preprocessing import load_test_csv, make_features_for_inference
from src.scorer import load_model, score_proba

INPUT_DIR = Path(os.getenv("INPUT_DIR", "input"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "output"))
INPUT_FILENAME = "test.csv"
OUTPUT_FILENAME = "sample_submission.csv"


def main():
    INPUT_DIR.mkdir(exist_ok=True, parents=True)
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    input_path = INPUT_DIR / INPUT_FILENAME
    output_path = OUTPUT_DIR / OUTPUT_FILENAME

    df_test = load_test_csv(str(input_path))
    X_test = make_features_for_inference(df_test)
    model = load_model()
    proba = score_proba(model, X_test)

    n = len(proba)
    submission = pd.DataFrame({
        "index": np.arange(n),
        "target": proba
    })
    submission.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
