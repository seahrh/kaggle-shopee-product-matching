__all__ = [
    "target_label",
    "metric_per_row",
    "combine_as_list",
    "combine_as_string",
    "phash_matches",
    "sbert_matches",
    "preprocess",
]

import re
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sentence_transformers import SentenceTransformer
from typing import Set, List, Callable, Any, Iterable
from scml.nlp import to_ascii_str, expand_contractions


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
    nn = NearestNeighbors(n_neighbors=min(n_neighbors, len(x) - 1), metric="hamming")
    nn.fit(x)
    distances, indices = nn.kneighbors()
    res: List[List[str]] = [[] for _ in range(len(indices))]
    for i in range(len(indices)):
        for j in range(len(indices[0])):
            if distances[i][j] > threshold:
                break
            res[i].append(df.iloc[indices[i][j]]["posting_id"])
    return res


def sbert_matches(
    model_path: str,
    sentences: List[str],
    posting_ids: List[str],
    threshold: float,
    n_neighbors: int = 49,
    max_seq_length: int = 512,
) -> List[List[str]]:
    model = SentenceTransformer(model_path)
    model.max_seq_length = max_seq_length
    em = model.encode(
        sentences,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    nn = NearestNeighbors(
        n_neighbors=min(n_neighbors, len(posting_ids) - 1), metric="euclidean"
    )
    nn.fit(em)
    distances, indices = nn.kneighbors()
    res: List[List[str]] = [[] for _ in range(len(indices))]
    for i in range(len(indices)):
        for j in range(len(indices[0])):
            if distances[i][j] > threshold:
                break
            res[i].append(posting_ids[indices[i][j]])
    return res


_remove_byte_string_syntax_pattern = re.compile(r'^b"(.*)"$')


def _remove_byte_string_syntax(s: str) -> str:
    m = _remove_byte_string_syntax_pattern.match(s)
    if m is None:
        return s
    return m.group(1)


def preprocess(row) -> str:
    res: str = row["title"]
    res = _remove_byte_string_syntax(res)
    res = to_ascii_str(res)
    res = expand_contractions(res)
    return res
