__all__ = [
    "target_label",
    "metric_per_row",
    "combine_as_list",
    "combine_as_string",
    "phash_matches",
]

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from typing import Set, List, Callable, Any, Iterable


def target_label(df: pd.DataFrame) -> pd.Series:
    tmp = df.groupby("label_group")["posting_id"].unique().to_dict()
    return df["label_group"].map(tmp)


def metric_per_row(prediction: str, target: str = "target") -> Callable[[Any], float]:
    def f1(row) -> float:
        n = len(np.intersect1d(row[target], row[prediction]))
        return 2 * n / (len(row[target]) + len(row[prediction]))

    return f1


def combine_as_list(cols: Iterable[str]) -> Callable:
    def fn(row) -> List[str]:
        s: Set[str] = set()
        s.add(row["posting_id"])
        for col in cols:
            s |= set(row[col])
        return list(s)

    return fn


def combine_as_string(cols: Iterable[str]) -> Callable:
    def fn(row) -> str:
        s: Set[str] = set()
        s.add(row["posting_id"])
        for col in cols:
            s |= set(row[col])
        return " ".join(s)

    return fn


def phash_matches(
    df: pd.DataFrame, threshold: float, n_neighbors: int = 49, hash_length: int = 16
) -> List[List[str]]:
    rows = []
    for t in df.itertuples():
        ph = getattr(t, "image_phash")
        if len(ph) != hash_length:
            raise ValueError(f"expected len(ph) is {hash_length} but found {len(ph)}")
        row = {}
        for i in range(hash_length):
            row[f"ph{i}"] = int(ph[i], 16)
        rows.append(row)
    x = pd.DataFrame.from_records(rows)
    x = x.astype(np.int8)
    model = NearestNeighbors(n_neighbors=min(n_neighbors, len(x) - 1), metric="hamming")
    model.fit(x)
    distances, indices = model.kneighbors()
    res: List[List[str]] = [[] for _ in range(len(indices))]
    for i in range(len(indices)):
        for j in range(len(indices[0])):
            if distances[i][j] > threshold:
                break
            res[i].append(df.iloc[indices[i][j]]["posting_id"])
    return res
