import pandas as pd


def target_label(df: pd.DataFrame) -> pd.Series:
    tmp = df.groupby("label_group")["posting_id"].unique().to_dict()
    return df["label_group"].map(tmp)
