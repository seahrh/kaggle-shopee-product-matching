import numpy as np
import pandas as pd


def target_label(df: pd.DataFrame) -> pd.Series:
    tmp = df.groupby("label_group")["posting_id"].unique().to_dict()
    return df["label_group"].map(tmp)


def metric_per_row(prediction: str, target: str = "target"):
    def f1(row):
        n = len(np.intersect1d(row[target], row[prediction]))
        return 2 * n / (len(row[target]) + len(row[prediction]))

    return f1
